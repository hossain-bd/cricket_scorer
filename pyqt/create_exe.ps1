## create_exe.ps1

Write-Host 'Hello There \n'


rm -r __pycache__
rm -r build
rm -r dist
rm C:\Users\Hossain\AppData\Local\Continuum\anaconda3\cricket_scorer.ui


pyinstaller .\main.py
py .\copy_to_main.py
