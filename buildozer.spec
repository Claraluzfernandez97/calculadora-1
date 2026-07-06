[app]

# (str) Title of your application
title = Calculadora

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yavirac

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# NOTA: Usamos solo kivy porque tu main.py no requiere KivyMD. Esto acelera el pipeline y evita fallos.
requirements = python3,kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/calcu.png

# (str) Icon of the application
icon.filename = %(source.dir)s/calcu.png

# (list) Supported orientations
orientation = portrait

# ==========================================
# Android specific
# ==========================================

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25c

# (int) Android NDK API to use.
android.ndk_api = 24

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True
