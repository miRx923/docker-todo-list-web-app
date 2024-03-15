# end-app.ps1
# Script for deleting everything

docker compose down

docker image rm todo-web-app-web

echo
echo
echo
echo
echo Run the rm-db.sh script to remove the 'db' folder or remove it manually.
echo
echo
echo
echo
