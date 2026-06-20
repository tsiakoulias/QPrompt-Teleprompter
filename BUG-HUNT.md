# Prompter.qml Bug Hunt Audit

**File:** `src/prompter/Prompter.qml`
**Lines:** 1–3139
**Date:** 2026-06-20

---

## Bug 1 — Typo in property name `__possitiveDirection`

**Severity:** Low  
**Line:** 115  
**Type:** Spelling / readability

The readonly property is named `__possitiveDirection` (extra "s") instead of `__positiveDirection`. It is used on line 119 in the `__velocity` calculation. Correct behavior is unaffected, but any future code that references the correct spelling will silently fail.

```qml
// Line 115
readonly property bool __possitiveDirection: __i>=0

// Line 119
readonly property real __velocity: (__possitiveDirection ? 1 : -1) * __speed
```

---

## Bug 2 — `rewind()` and `fastForward()` crash on non-key-event invocation  

**Severity:** High  
**Lines:** 552, 565  
**Type:** Crash / TypeError

Both functions access `event.key` to set `keyBeingPressed`:

```qml
function rewind() {
    if (!winding) {
        // ...
        keyBeingPressed = event.key;   // line 552
```

```qml
function fastForward() {
    if (!winding) {
        // ...
        keyBeingPressed = event.key;   // line 565
```

`event` is the parameter from `Keys.onPressed`, available only in the key-handler scope chain. When these functions are invoked from **non-key contexts**, `event` is `undefined` → **TypeError: Cannot read property 'key' of undefined**.

**Reproduction path:** `AppController` connections at lines 324–331 call `prompter.rewind()` / `prompter.fastForward()` with no event:

```qml
function onRewind() {
    if (!interalFocusElsewhere())
        prompter.rewind();    // event is undefined → CRASH
}
```

`keyBeingPressed` is also set to `undefined`, which breaks the `Keys.onReleased` check at line 2874 that compares `event.key===keyBeingPressed` to detect key release.

---

## Bug 3 — `setVelocity(0)` creates a brief negative-velocity animation before stopping  

**Severity:** Medium  
**Lines:** 606–609  
**Type:** Logic / visual glitch

```qml
function setVelocity(velocity: int, event: var) {
    this.__i = velocity - 1        // when velocity=0: __i = -1
    this.position = this.__destination
    this.__i = velocity             // __i = 0
    this.__play = true
    this.position = this.__destination
}
```

The `velocity - 1` intermediate value exists solely to guarantee `on__IChanged` fires. For `velocity = 0`, it sets `__i = -1` temporarily, triggering a `Behavior on position` animation scrolling **backward** before being overridden to `__i = 0`. This causes a visible flicker/jump when stopping the teleprompter via the numbered velocity keys.

---

## Bug 4 — Division by zero in `__timeToEnd` when `__relativeSpeed` is zero  

**Severity:** Medium  
**Lines:** 121–123  
**Type:** Arithmetic / NaN

```qml
readonly property real __relativeSpeed: (__speed * fontSize/2 * ((__vw-__evw/2) / __vw))
readonly property real __timeToEnd: 2 * (editor.height + fontSize - __travelDistance) / __relativeSpeed
readonly property real __timeToArival: __i ? ((__possitiveDirection ? __timeToEnd : 2 * __travelDistance / __relativeSpeed)) * 1000 : 0
```

When any factor in `__relativeSpeed` is zero (e.g., `fontSize == 0`, `__speed == 0`, or `__vw == __evw/2`), the result is `0`. Division by zero produces `Infinity` (or `NaN` if numerator is also zero). These properties feed into `timeToArival` which drives the `NumberAnimation` duration (line 844). An `Infinity` duration may freeze the animation, while `NaN` can cause undefined behavior in the Qt animation engine.

---

## Bug 5 — `onMovementEnded` restarts animation without boundary checks  

**Severity:** Medium  
**Lines:** 788–798  
**Type:** Logic / overscroll

```qml
onMovementEnded: {
    __i = __iBackup
    if (parseInt(prompter.state)===Prompter.States.Prompting) {
        __iBackup = 0
        position = __destination
    }
    else
       position = position
}
```

After the user manually flicks/scrolls the prompter in Prompting state, `position = __destination` restarts the velocity-driven animation regardless of whether the current position is at or beyond `__atStart` / `__atEnd`. If the user has scrolled past the document end, the animation will start driving `position` toward `__destination` based on the velocity formula, potentially attempting to animate beyond document bounds before the `onRunningChanged` handler (line 846) finally fires the end-of-document action.

---

## Bug 6 — `onCursorPositionChanged` does not guard against `dragTarget.manualDrag`  

**Severity:** Medium  
**Lines:** 1908–1918  
**Type:** Logic / unwanted UI update during drag

```qml
Connections {
    target: editor
    function onCursorPositionChanged() {
        if (!dragTarget.internalDrag && !dragTarget.containsDrag) {
            if (editor.selectionStart === editor.selectionEnd) {
                imageResizeOverlay.tryShow(editor.cursorPosition);
            } else if (imageResizeOverlay.visible) {
                const imgPos = imageResizeOverlay.imagePosition
                if (editor.selectionStart !== imgPos || editor.selectionEnd !== imgPos + 1)
                    imageResizeOverlay.hide()
            }
        }
    }
}
```

The guard checks `internalDrag` and `containsDrag` but omits `dragTarget.manualDrag`. During a manual drag operation (text or image repositioning initiated from `textDragArea` or `imageResizeOverlay` body drag), the cursor position changes as the editor repositions the drop indicator. This triggers `tryShow()` or `hide()` on the image resize overlay mid-drag, causing incorrect overlay visibility/position.

---

## Bug 7 — Null/unchecked `spellSuggestions` from `spellCheckInfoAt` causes crash in context menu  

**Severity:** High  
**Lines:** 1389–1396, 2519, 2588  
**Type:** Crash / null dereference

```qml
const info = document.spellCheckInfoAt(pos)
if (info && info.misspelled) {
    prompter.spellSuggestions = info.suggestions   // may be null
```

If `document.spellCheckInfoAt()` returns `{ misspelled: true, suggestions: null }`, then `prompter.spellSuggestions` is set to `null`. Later, the context menu visibility binding evaluates:

```qml
// nativeContextMenu (line 2519)
visible: prompter.spellSuggestions.length > 0   // TypeError on null.length

// contextMenu (line 2588)
visible: prompter.spellSuggestions.length > 0    // TypeError on null.length
```

Accessing `.length` on `null` throws a **TypeError** in QML, crashing the UI when the context menu tries to render. The `applySpellSuggestion()` function (line 156) also accesses `prompter.spellSuggestions` indirectly via parameters but is only called from the menu, which would already be unreachable after the crash.

---

## Summary

| # | Severity | Line(s) | Category |
|---|----------|---------|----------|
| 1 | Low | 115 | Typo |
| 2 | High | 552, 565 | Crash |
| 3 | Medium | 606–609 | Visual glitch |
| 4 | Medium | 121–123 | NaN |
| 5 | Medium | 788–798 | Logic |
| 6 | Medium | 1908–1918 | Logic |
| 7 | High | 1389–1396, 2519, 2588 | Crash |
