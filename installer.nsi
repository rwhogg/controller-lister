!define VERSION "1.0.0"
Name "Controller Lister ${VERSION}"
OutFile "dist\controller-lister-installer.exe"
Icon "icon.ico"

InstallDir "$PROGRAMFILES64\Controller Lister"

Section "Controller List"
    SetOutPath $INSTDIR
    File "dist\controller-lister.exe"
SectionEnd
