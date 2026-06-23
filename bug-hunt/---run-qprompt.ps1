# Launches a locally-built QPrompt inside the Craft environment.
# Usage:
#   .\run-qprompt.ps1                       # runs build-craft\bin\QPrompt.exe
#   .\run-qprompt.ps1 QPrompt-buggy.exe     # runs a specific exe in build-craft\bin
#   .\run-qprompt.ps1 C:\full\path\to.exe   # or an absolute path
# craftenv.ps1, given arguments, runs them via `craft --run` so Qt6/KF6 DLLs and
# QML import paths resolve -- without clobbering your current shell.

param([string]$Exe = 'QPrompt.exe')

$bin = 'C:\Users\User\Repositories\External\QPrompt-Teleprompter\build-craft\bin'

if (Test-Path $Exe) { $target = (Resolve-Path $Exe).Path }
else { $target = Join-Path $bin $Exe }

if (-not (Test-Path $target)) {
    Write-Error "Not found: $target`nBuild it first (cmake --build build-craft)."
    exit 1
}

& 'C:\CraftRoot\craft\craftenv.ps1' $target
