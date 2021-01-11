task default: %W[bundle]

task bundle: %W[dist/controller-lister.exe dist/controller-lister-installer.exe]

%W[controller-lister/__init__.py].each do |pyfile|
    sh "pyinstaller --noconsole --onefile --icon icon.ico #{pyfile}"
    sh "mv dist/__init__.exe dist/controller-lister.exe"
end

%W[installer.nsi].each do |installerscript|
   sh "makensis #{installerscript}"
end
