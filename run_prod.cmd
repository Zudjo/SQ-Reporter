@echo off
CALL cls

echo.
CALL sass template/css/sass/main.sass template/css/main.css && echo sass code compiled
echo ___________________________________________________________________________
echo.
CALL main.py
echo ___________________________________________________________________________
echo.

PAUSE
