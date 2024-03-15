:: end-app.ps1
:: Script for deleting everything

docker compose down

docker image rm todo-web-app-web

@echo off
echo.
echo.
echo.
echo.
echo Run the rm-db.bat script to remove the 'db' folder or remove it manually.
echo.
echo.
echo.
echo.
