@echo off
cd %~dp0

:loop
rem Get current date and time in EST for the filename
for /f "tokens=1-2 delims=. " %%a in ('wmic os get localdatetime ^| find "."') do (
    set dt=%%a
)
set dt=%dt:~0,4%-%dt:~4,2%-%dt:~6,2%_%dt:~8,2%-%dt:~10,2%-%dt:~12,2%

rem Create a filename that includes both date and time in EST
set filename=license_status_%dt%_EST.txt

rem Run the lmutil command and save output to the uniquely named file
lmutil lmstat -a -c 27000@flexnet-prod-1 > %filename%

rem Wait for 60 seconds (1 minute)
timeout /t 0 /nobreak



