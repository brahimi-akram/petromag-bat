
set filename=%~1
set filepath=%~2

if not exist "%filename%" (
    echo Error: File "%filename%" not found
    exit /b 2
)

echo Processing file: %filename%

soffice --headless --convert-to pdf --outdir "%filepath%" "%filename%"

if %errorlevel% neq 0 (
    echo Conversion failed
    exit /b %errorlevel%
)

echo Conversion complete

exit /b 0

