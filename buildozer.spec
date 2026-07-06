[app]

# (str) Title of your application
title = Calculadora del Yavirac

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android packaging)
package.domain = org.yavirac

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (include extension)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application icon
icon.filename = calcu.png

# (list) Application requirements
# NOTA: Dejamos solo kivy porque tu código actual de la calculadora no usa KivyMD. Esto acelera la compilación en un 50%.
requirements = python3,kivy

# (list) The Android archs to build for.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Accept SDK license
android.accept_sdk_license = True
