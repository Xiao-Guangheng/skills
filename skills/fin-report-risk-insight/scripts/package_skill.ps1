param(
    [string]$SourceDir = (Split-Path -Parent $PSScriptRoot),
    [string]$OutputPath = $(Join-Path (Split-Path -Parent $SourceDir) ((Split-Path $SourceDir -Leaf) + ".zip"))
)

$resolvedSourceDir = Resolve-Path $SourceDir

if (Test-Path $OutputPath) {
    Remove-Item $OutputPath -Force
}

Compress-Archive -Path (Join-Path $resolvedSourceDir "*") -DestinationPath $OutputPath

Write-Host "Packaged skill to $OutputPath"