!define VERSION "1.0.0"
Name "Controller Lister ${VERSION}"
OutFile "dist\controller-list-installer.exe"

Section "Controller List"
    SetOutPath $INSTDIR
    File "dist\controller-list.exe"
SectionEnd
