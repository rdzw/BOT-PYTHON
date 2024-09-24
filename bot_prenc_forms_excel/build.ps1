$exclude = @("venv", "bot_prenc_forms_excel.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_prenc_forms_excel.zip" -Force