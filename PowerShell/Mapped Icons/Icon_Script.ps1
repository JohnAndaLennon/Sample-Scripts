Copy-Item "\\example\filepath\put\in\your\own" -Destination "C:\Program Files\Network Drives" -Recurse
$ComObj = New-Object -ComObject WScript.Shell
$ShortCut = $ComObj.CreateShortcut("C:\Users\Public\Desktop\Network Drives.lnk")
$ShortCut.TargetPath = "C:\Program Files\Network Drives\Network Drives.bat"
$ShortCut.Description = "Updates Network Drives"
$ShortCut.WindowStyle = 7
$ShortCut.IconLocation = "C:\Program Files\Network Drives\TFCU.ico"
$ShortCut.Save()
