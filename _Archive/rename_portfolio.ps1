<# 
Run from: C:\Users\beall\OneDrive\Documents\Portfolio
Usage:
  .\rename_portfolio.ps1           # Preview
  .\rename_portfolio.ps1 -Apply    # Apply changes
#>

param([switch]$Apply)

$Root = Get-Location
$Log  = Join-Path $Root "rename_log_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
$changes = @()

function Pad2($n){ '{0:D2}' -f [int]$n }

function Normalize-Slug($text){
  $t = $text -replace '[^\p{L}\p{Nd}]+','_'
  $t = $t -replace '_+','_'
  $t = $t.Trim('_').ToLower()
  return $t
}

function Build-NewName($prefix, $num, $rest){
  $num2  = Pad2 $num
  $slug  = Normalize-Slug $rest
  return "$prefix-$num2" + ($(if($slug){ "_$slug" } else { "" }))
}

function Get-ParentDir($item){
  # Prefer the .Parent property for DirectoryInfo/FileInfo objects
  if ($item -is [System.IO.FileSystemInfo] -and $item.Parent) {
    return $item.Parent.FullName
  }
  # Fallback to Split-Path using -Path (NOT -LiteralPath) with -Parent
  $p = Split-Path -Path $item.FullName -Parent
  if ([string]::IsNullOrWhiteSpace($p)) { return (Get-Location).Path }
  return $p
}

function Maybe-Rename($item, $newName){
  if ($item.Name -ceq $newName) { return }

  $parent = Get-ParentDir $item
  $src = $item.FullName
  $dst = Join-Path -Path $parent -ChildPath $newName

  $rec = [pscustomobject]@{
    Folder  = $parent
    OldName = $item.Name
    NewName = $newName
    PathOld = $src
    PathNew = $dst
    Applied = $false
  }
  $changes += $rec

  if ($Apply){
    try {
      Rename-Item -LiteralPath $src -NewName $newName
      $rec.Applied = $true
    } catch {
      Write-Warning "Failed: $src -> $newName : $($_.Exception.Message)"
    }
  } else {
    Write-Host "[PREVIEW] $src -> $newName"
  }
}

# skip list
$skipRoot = @('_Archive','_Portfolio_AnswerKey','_Reference','.devcontainer','.vscode','services')

# category -> prefix
$prefixMap = @{
  'AI'                 = 'AI'
  'Blockchain'         = 'BLK'
  'Business_Analytics' = 'BA'
  'Logistics'          = 'LOG'
  'SCM_AI'             = 'SCM'
}

Get-ChildItem -Force -Directory | Where-Object {
  $_.Name -in $prefixMap.Keys -and $_.Name -notin $skipRoot
} | ForEach-Object {
  $top = $_
  $prefix = $prefixMap[$top.Name]

  Get-ChildItem -LiteralPath $top.FullName -Force -Directory | ForEach-Object {
    $d = $_
    $name = $d.Name

    if ($name -match "^(?<pre>$prefix)-(?<n>\d{1,2})(?:[_\s-](?<rest>.*))?$"){
      $n    = $matches['n']; $rest = $matches['rest']
      $new  = Build-NewName $prefix $n $rest
      Maybe-Rename $d $new; return
    }

    if ($name -match "^(?<n>\d{1,2})[ _-](?<rest>.+)$"){
      $n    = $matches['n']; $rest = $matches['rest']
      $new  = Build-NewName $prefix $n $rest
      Maybe-Rename $d $new; return
    }

    if ($name -match "^(?<anypre>[A-Za-z]+)-(?<n>\d{1,2})(?:[_\s-](?<rest>.*))?$"){
      $n    = $matches['n']; $rest = $matches['rest']
      $new  = Build-NewName $prefix $n $rest
      Maybe-Rename $d $new; return
    }

    # No number: leave as-is (set $assignZero=$true to number as 00)
    $assignZero = $false
    if ($assignZero){
      $new = Build-NewName $prefix 0 $name
      Maybe-Rename $d $new; return
    }
  }
}

$changes | Export-Csv -NoTypeInformation -Path $Log
if ($Apply){
  Write-Host "Applied $(($changes | ? {$_.Applied}).Count) / $($changes.Count) renames."
} else {
  Write-Host "Preview only. To apply, rerun with -Apply"
}
Write-Host "Log: $Log"
