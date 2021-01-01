task default: %W[bundle]

task bundle: %W[dist/controller-list.exe dist/controller-list-installer.exe]

%W[controller-list.py].each do |pyfile|
    sh "pyinstaller.exe --noconsole --onefile #{pyfile}"
end

%W[installer.nsi].each do |installerscript|
   sh "makensis #{installerscript}"
end
