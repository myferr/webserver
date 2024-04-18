@echo off

set arg=%1

if "%arg%"=="--run" (
    python announce.py
    node server.js
)

if "%arg%"=="" (
    python ./errors/error1.py
)