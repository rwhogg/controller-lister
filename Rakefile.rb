task default: %w[bundle]

task bundle: do
    pyinstaller controller-list.py
end
