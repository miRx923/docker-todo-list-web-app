# start-app.ps1
# Script for setting everything up

Write-Host "`n`n`n`n`nIn browser go to: http://127.0.0.1:5000/ to access TODO list application.`n`n`n`n`n"

docker compose up --build
