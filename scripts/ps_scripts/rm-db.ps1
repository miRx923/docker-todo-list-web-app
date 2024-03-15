# rm-db.ps1
# Script for deleting database

Remove-Item -Path "db" -Recurse

Write-Host "`n`n`nDatabase was deleted succesfully.`n`n`n"
