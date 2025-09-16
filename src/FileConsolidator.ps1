<#
.SYNOPSIS
    Moves all files from a source to a destination, then cleans up the empty source folders.

.DESCRIPTION
    This script first flattens a directory structure by moving all files into a single destination folder.
    After the move is complete, it performs a second pass to find and delete any now-empty subfolders in the source directory.

.PARAMETER Source
    The source directory to scan for files and clean up.

.PARAMETER Destination
    The destination directory where all files will be moved.
#>
param(
    [string]$Source = "D:\CODING\ARCHIVES\DATABASE",
    [string]$Destination = "D:\Downloads"
)

# Safety Check
$resolvedSource = (Resolve-Path -LiteralPath $Source).ProviderPath
$resolvedDestination = (Resolve-Path -LiteralPath $Destination).ProviderPath

if ($resolvedDestination.StartsWith($resolvedSource, [System.StringComparison]::InvariantCultureIgnoreCase)) {
    Write-Host "Error: The destination folder cannot be inside the source folder." -ForegroundColor Red
    return
}

# --- Phase 1: Move All Files ---

Write-Host ""
Write-Host "--- Phase 1: Moving Files ---" -ForegroundColor Cyan

if (-not (Test-Path -Path $Destination)) {
    New-Item -Path $Destination -ItemType Directory | Out-Null
}

Get-ChildItem -Path $Source -Recurse -File -Force | ForEach-Object {
    $sourceFile = $_
    $destinationPath = Join-Path -Path $Destination -ChildPath $sourceFile.Name

    $counter = 1
    $baseName = $sourceFile.BaseName
    $extension = $sourceFile.Extension

    while (Test-Path -Path $destinationPath) {
        $newName = "{0}_{1}{2}" -f $baseName, $counter, $extension
        $destinationPath = Join-Path -Path $Destination -ChildPath $newName
        $counter++
    }

    try {
        Move-Item -LiteralPath $sourceFile.FullName -Destination $destinationPath -ErrorAction Stop
        Write-Host "Moved: $($sourceFile.FullName) -> $($destinationPath)" -ForegroundColor Green
    }
    catch {
        Write-Host "Error moving $($sourceFile.FullName): $_" -ForegroundColor Red
    }
}

Write-Host "File move complete."
Write-Host ""


# --- Phase 2: Clean Up Empty Folders ---

Write-Host "--- Phase 2: Cleaning Up Empty Folders ---" -ForegroundColor Cyan

$folders = Get-ChildItem -Path $Source -Recurse -Directory | Sort-Object -Property {$_.FullName.Length} -Descending
$deletedCount = 0

foreach ($folder in $folders) {
    if ((Get-ChildItem -Path $folder.FullName -Force).Count -eq 0) {
        try {
            Remove-Item -LiteralPath $folder.FullName -ErrorAction Stop
            Write-Host "Deleted empty folder: $($folder.FullName)" -ForegroundColor Yellow
            $deletedCount++
        }
        catch {
            Write-Host "Error deleting $($folder.FullName): $_" -ForegroundColor Red
        }
    }
}

Write-Host "---"
Write-Host "Consolidation and cleanup complete. Deleted $deletedCount empty folder(s)." -ForegroundColor Green