# end-app.ps1
# Script for deleting everything except database ("./db" folder)

docker compose down

docker image rm todo-web-app-web

Write-Host "`n`n`n`n`nRun the rm-db.ps1 script to remove the 'db' folder or remove it manualy.`n`n`n`n`n"
