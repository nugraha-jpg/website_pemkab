$port = 8000
$path = $PSScriptRoot
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()
Write-Host "Server running on http://localhost:$port"

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response
    
    $localPath = Join-Path $path ([Uri]::UnescapeDataString($request.Url.LocalPath).TrimStart('/'))
    if ($localPath -eq $path -or -not (Test-Path $localPath)) {
        $localPath = Join-Path $path 'index.html'
    }
    
    if (Test-Path $localPath -PathType Leaf) {
        $content = [System.IO.File]::ReadAllBytes($localPath)
        $ext = [System.IO.Path]::GetExtension($localPath)
        $response.ContentType = switch ($ext) {
            '.js' { 'text/javascript' }
            '.css' { 'text/css' }
            '.html' { 'text/html' }
            '.png' { 'image/png' }
            '.jpg' { 'image/jpeg' }
            '.gif' { 'image/gif' }
            default { 'application/octet-stream' }
        }
        $response.OutputStream.Write($content, 0, $content.Length)
    }
    else {
        $response.StatusCode = 404
    }
    
    $response.Close()
}
