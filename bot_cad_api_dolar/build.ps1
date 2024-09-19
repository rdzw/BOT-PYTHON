$exclude = @("venv", "bot_cad_api_dolar.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cad_api_dolar.zip" -Force