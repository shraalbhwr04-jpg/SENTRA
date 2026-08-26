[app]

# (str) Title of your application
title = SENTRA

# (str) Package name
package.name = sentra

# (str) Package domain (needed for android packaging)
package.domain = org.sentra

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
