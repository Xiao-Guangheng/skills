param(
    [string]$SourceDir = (Split-Path -Parent $PSScriptRoot),
    [string]$OutputZip
)

if (-not $OutputZip) {
    $parentDir = Split-Path -Parent $SourceDir
    $skillName = Split-Path $SourceDir -Leaf
    $OutputZip = Join-Path $parentDir ($skillName + '.zip')
}

if (Test-Path $OutputZip) {
    Remove-Item $OutputZip -Force
}

Compress-Archive -Path $SourceDir -DestinationPath $OutputZip
Write-Host "Created ZIP: $OutputZip"
