$exclude = @("venv", "bot_converte_valor.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_converte_valor.zip" -Force