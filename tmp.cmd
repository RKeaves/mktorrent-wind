@echo off
for /F "delims=" %%A in ('echo prompt $E^| cmd') do set "ESC=%%A"
echo.
echo %ESC%[1;37mcygwin path: 123
echo.
echo %ESC%[1;36m  The above command has been copied to your clipboard
echo %ESC%[1;36m  Please paste it into the mktorrent bash window.
echo.
echo.
echo.
pause
