$exclude = @("venv", "bot_cadastro_json.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cadastro_json.zip" -Force