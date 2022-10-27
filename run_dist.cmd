@ECHO off
CALL cls

ECHO.
ECHO 1. Define project key
ECHO 2. Use default project key
ECHO.
SET /P _choice=
ECHO.

IF %_choice% EQU 1 (
  SET /P _project_key=Insert project key:
) ELSE (
  SET _project_key=
)

ECHO ___________________________________________________________________________
ECHO.
CALL main.py %_project_key%
ECHO ___________________________________________________________________________
ECHO.

PAUSE
