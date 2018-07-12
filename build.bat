RMDIR /S /Q "dist"
pyinstaller "--clean" "--onefile" "--log-level" "ERROR" "digimon_randomize.py"
COPY "settings.ini" "dist"
COPY "README.md" "dist"
"C:\Program Files\7-Zip\7za.exe" a -tzip "dist/digimon_randomizer.zip" dist