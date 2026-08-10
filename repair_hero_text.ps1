$files = Get-ChildItem -Filter '*.html' | Where-Object { $_.Name -ne 'index.html' }
$updated = @()
foreach ($file in $files) {
  $text = Get-Content -Path $file.FullName -Raw
  $titleMatch = [regex]::Match($text, '<title>(.*?)</title>', 'IgnoreCase')
  if (-not $titleMatch.Success) { continue }
  $pageTitle = $titleMatch.Groups[1].Value.Trim()
  $heroTitle = if ($pageTitle -match ' - ') { $pageTitle -replace ' - .*$', '' } else { $pageTitle }
  $h2Match = [regex]::Match($text, '<h2>(.*?)</h2>', 'IgnoreCase')
  $firstH2 = if ($h2Match.Success) { $h2Match.Groups[1].Value.Trim() } else { '' }
  if ($firstH2 -and $firstH2 -ne $heroTitle) { $subText = $firstH2 } else { $subText = "Informasi dan detail tentang $heroTitle di Kabupaten Bandung Barat." }

  $pattern = '(?ms)<div class="hero-text">\s*(<div class="eyebrow">.*?</div>)\s*</div>'
  $replacement = '<div class="hero-text">`n  $1`n  <h1>' + $heroTitle + '</h1>`n  <p class="sub">' + $subText + '</p>`n</div>'
  $new = [regex]::Replace($text, $pattern, $replacement)

  if ($new -ne $text) {
    Set-Content -Path $file.FullName -Value $new
    $updated += $file.Name
  }
}
Write-Output "updated: $($updated -join ', ')"
