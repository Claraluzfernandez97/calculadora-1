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
# NOTA: Eliminamos la versión fija de kivy para evitar conflictos con KivyMD y la versión de python3 de las Actions.
requirements = python3,kivy,kivymd,pillow

# (list) The Android archs to build for.
# NOTA: Agregamos armeabi-v7a junto a arm64-v8a para que sea compatible con casi cualquier celular Android actual.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Accept SDK license
android.accept_sdk_license = True
