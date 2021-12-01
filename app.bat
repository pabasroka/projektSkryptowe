@echo off
setlocal enabledelayedexpansion

:menu
echo =============
echo 1. Start
echo 2. Informacje
echo 3. Backup
echo 4. Zakoncz
echo =============

set /p input=Wybierz opcje: 
if %input% EQU 1 goto start
if %input% EQU 2 goto info
if %input% EQU 3 goto backup
if %input% EQU 4 (
    exit
) else (
    cls
    goto menu
) 

:start
call app.py
call web.py
cls
goto menu

:info 
echo Program wykonuje podstawowe dzialania arytmetyczne w dziedzinie liczb zespolonych
echo Program pobiera dane wejsciowe z pliku
echo a nastepnie zwraca wynik w postaci strony
echo Program jest zadaniem konkursowym z konkursu Algorytmion 2017 
echo Autor: Patryk Sroczynski
set /p c=Nacisnij enter
cls 
goto menu

:backup
mkdir backup%date%
echo %cd%
xcopy %cd% backup%date% /S

pause