
# Python Executable Definition
$Python = "python.exe"


# Python Scrip that I wish to execute
$Script = "C:\Users\marle\Downloads\PS y Python\pyExif.py"


$files = Get-ChildItem C:\Users\marle\Downloads\images\*.jpg 
$jpegList = $files | Select-Object FullName | Format-Table -HideTableHeaders

$jpegList | & $Python $Script
