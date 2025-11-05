param(
    [string]$RepoUrl = "https://github.com/Karrion1987/detective-zero.git",
    [string]$ProjectDir = ".\detective-zero"
)

Write-Host "Introduce tu token de GitHub (no se mostrará):"
$token = Read-Host -AsSecureString | ConvertFrom-SecureString -AsPlainText

Set-Location $ProjectDir

git init
git branch -M main
git add .
git commit -m "Inicialización del proyecto Detective Zero"
git remote add origin $RepoUrl

# Crea una URL temporal con el token embebido (solo en memoria)
$authUrl = $RepoUrl -replace "https://", "https://Karrion1987:$token@"
Write-Host "Subiendo a GitHub..."
git push -u $authUrl main

# Limpieza del token de memoria
$token = $null
[System.GC]::Collect()
Write-Host "Proyecto subido correctamente."
