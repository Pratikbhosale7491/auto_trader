@echo off
REM === Create directories ===
mkdir backend
mkdir backend\services
mkdir scripts

REM === Create empty files ===
type nul > backend\main.py
type nul > backend\Dockerfile
type nul > backend\services\smartapi_service.py
type nul > scripts\auth_test.py
type nul > .env.template
type nul > requirements.txt
type nul > docker-compose.yml

echo.
echo ✅ Project structure created!
echo.
