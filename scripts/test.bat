@echo off
REM Calculator API - Windows Test Runner
REM Usage: scripts\test.bat [target]

setlocal

if "%1"=="" goto all
if "%1"=="all" goto all
if "%1"=="unit" goto unit
if "%1"=="integration" goto integration
if "%1"=="e2e" goto e2e
if "%1"=="help" goto help
goto help

:all
echo Running all tests (unit + integration)...
poetry run pytest tests/unit tests/integration -v
goto end

:unit
echo Running unit tests...
poetry run pytest tests/unit -v
goto end

:integration
echo Running integration tests...
poetry run pytest tests/integration -v
goto end

:e2e
echo Running E2E tests (ensure server is running)...
poetry run pytest tests/e2e -v
goto end

:help
echo.
echo Calculator API Test Runner
echo ==========================
echo.
echo Usage: scripts\test.bat [target]
echo.
echo Targets:
echo   all          Run unit + integration tests (default)
echo   unit         Run unit tests only
echo   integration  Run integration tests only
echo   e2e          Run E2E tests (requires running server)
echo   help         Show this help message
echo.
goto end

:end
endlocal
