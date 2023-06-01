@echo off
:: Check for Python Installation
echo Checking for Python installtion...
python --version
if errorlevel 1 goto errorNoPython

:: Check for Pillow
:checkPillow
echo.
echo Checking for Pillow library...
pip show pillow
if errorlevel 1 goto errorNoPillow

:: Check for Pyglet
:checkPyglet
echo.
echo Checking for Pyglet library...
pip show pyglet
if errorlevel 1 goto errorNoPyglet

::Start Program
:startProgram
echo.
echo Checking for Tkinter library...
pip install tk
start pythonw main.py

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed. Please visit https://www.python.org/downloads/
pause

:errorNoPillow
python3 -m pip install --upgrade Pillow
goto checkPyglet

:errorNoPyglet
pip install --upgrade --user pyglet
goto startProgram