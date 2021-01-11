task default: %W[bundle]

task bundle: %W[dist/controller-list.exe dist/controller-list-installer.exe]

%W[controller-lister/__init__.py].each do |pyfile|
    sh "pyinstaller --noconsole --onefile --icon icon.ico #{pyfile}"
end

%W[installer.nsi].each do |installerscript|
   sh "makensis #{installerscript}"
end
