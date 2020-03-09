RMDIR /S /Q "dist"
RMDIR /S /Q "gui\digimon_randomize-win32-x64"
pyinstaller "--clean" "--onefile" "--log-level" "ERROR" "digimon_randomize.py"
CD "gui"
call npm install
call npm run-script build
call npm run package
CD ".."
xcopy "gui\digimon_randomize-win32-x64" "dist\gui\" /E /H /C /R /Q /Y
COPY "settings.ini" "dist\gui\resources\app"
COPY "README.md" "dist\gui\resources/app"
MOVE "dist\digimon_randomize.exe" "dist\gui\resources\app"
"C:\Program Files\7-Zip\7za.exe" a -tzip "dist/digimon_randomizer.zip" dist