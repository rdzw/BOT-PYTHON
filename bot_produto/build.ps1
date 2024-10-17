$exclude = @("venv", "bot_produto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_produto.zip" -Force