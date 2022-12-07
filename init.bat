@echo off
echo Create new application configuration

echo Enter database name: 
set /p db_name=
echo Your database name is %db_name%

echo Enter database user name: 
set /p db_user=
echo Your user name is: %db_user%

echo Set database password: 
set /p db_pass=
echo Your password is: %db_pass%

echo Set database host: 
set /p db_host=
echo Your database host is %db_host%

echo Set database port: 
set /p db_port=
echo Your database port: %db_port%

(echo from app import app & echo app.run^(debug=True, host="0.0.0.0"^)) > app.py

(echo db_name = "%db_name%" & echo db_user = "%db_user%" & echo db_pass = "%db_pass%" & echo db_host = "%db_host%" & echo db_port = "%db_port%") > "data\init.py"

echo You create new configuration:
pause