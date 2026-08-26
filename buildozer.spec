[app]

# (str) Title of your application
title = SENTRA

# (str) Package name
package.name = sentra

# (str) Package domain (needed for android packaging)
package.domain = org.sentra

# (str) Source where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
