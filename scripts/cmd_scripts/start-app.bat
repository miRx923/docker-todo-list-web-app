:: start-app.ps1
:: Script for setting everything up

@echo off
echo.
echo.
echo.
echo.
echo.
echo In browser go to: http://127.0.0.1:5000/ to access TODO list application.
echo.
echo.
echo.
echo.

docker compose up --build
