$files = Get-ChildItem -Filter '*.html' | Where-Object { $_.Name -ne 'index.html' }
foreach ($file in $files) {
  $text = Get-Content -Path $file.FullName -Raw
  $heroSection = [regex]::Match($text, '(?is)<section\s+class="page-hero">.*?</section>')
  if (-not $heroSection.Success) { continue }

  $heroText = $heroSection.Value
  $eyebrowMatch = [regex]::Match($heroText, '(?is)<div\s+class="eyebrow">.*?</div>')
  $eyebrow = if ($eyebrowMatch.Success) { $eyebrowMatch.Value.Trim() } else { '<div class="eyebrow"><span class="rule"></span></div>' }

  $titleMatch = [regex]::Match($heroText, '(?is)<h1>(.*?)</h1>')
  $pageTitleMatch = [regex]::Match($text, '(?is)<title>(.*?)</title>')
  $pageTitle = if ($pageTitleMatch.Success) { $pageTitleMatch.Groups[1].Value.Trim() } else { '' }

  if ($titleMatch.Success) {
    $heroTitle = $titleMatch.Groups[1].Value.Trim()
  } elseif ($pageTitle -match ' - ') {
    $heroTitle = ($pageTitle -split ' - ')[0].Trim()
  } else {
    $heroTitle = $pageTitle
  }
  if (-not $heroTitle) { $heroTitle = 'Kabupaten Bandung Barat' }

  $subMatch = [regex]::Match($heroText, '(?is)<p\s+class="sub">(.*?)</p>')
  $h2Match = [regex]::Match($text, '(?is)<h2>(.*?)</h2>')
  if ($subMatch.Success) {
    $heroSub = $subMatch.Groups[1].Value.Trim()
  } elseif ($h2Match.Success -and $h2Match.Groups[1].Value.Trim() -ne $heroTitle) {
    $heroSub = $h2Match.Groups[1].Value.Trim()
  } else {
    $heroSub = "Informasi dan detail tentang $heroTitle di Kabupaten Bandung Barat."
  }

  $newHero = '<section class="page-hero">' + [Environment]::NewLine
  $newHero += '  <div class="page-hero-bg"></div>' + [Environment]::NewLine
  $newHero += '  <div class="page-hero-inner">' + [Environment]::NewLine
  $newHero += '    <div class="hero-text">' + [Environment]::NewLine
  $newHero += '      ' + $eyebrow + [Environment]::NewLine
  $newHero += '      <h1>' + $heroTitle + '</h1>' + [Environment]::NewLine
  $newHero += '      <p class="sub">' + $heroSub + '</p>' + [Environment]::NewLine
  $newHero += '    </div>' + [Environment]::NewLine
  $newHero += '  </div>' + [Environment]::NewLine
  $newHero += '</section>' + [Environment]::NewLine

  $newText = $text.Substring(0, $heroSection.Index) + $newHero + $text.Substring($heroSection.Index + $heroSection.Length)
  if ($newText -ne $text) {
    Set-Content -Path $file.FullName -Value $newText
    Write-Output "updated: $($file.Name)"
  }
}
