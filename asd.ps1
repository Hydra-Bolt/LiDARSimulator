# Loop through all Python files in the current directory
Get-ChildItem -Filter *.py | ForEach-Object {
    $filename = $_.Name
    Write-Host "==================================================="
    Write-Host "Filename: $filename"
    Write-Host "==================================================="
    Write-Host ""
    
    # Read and display the content of the file
    Get-Content $_.FullName | ForEach-Object { Write-Host $_ }

    Write-Host ""
    Write-Host "==================================================="
    Write-Host ""
}

# Pause the script at the end (if desired)
Read-Host -Prompt "Press Enter to exit"
