@echo off
REM Double-clickable launcher. Pass an exe name to pick which build, e.g.:
REM   run-qprompt.cmd QPrompt-buggy.exe
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0---run-qprompt.ps1" %*
