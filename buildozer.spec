# (str) Title of your application
title = Calculadora

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android packaging)
package.domain = org.tuusuario

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (include extension)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application icon
icon.filename = calcu.png

# (list) Application requirements
# Asegúrate de incluir kivy y cualquier otra librería que uses (ej: kivymd, pillow)
requirements = python3,kivy==2.3.0,kivymd

# (str) Android architecture (puedes dejarlo por defecto o usar armeabi-v7a)
android.archs = arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True
