# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/jeseo/Works/user-group-csv-cleaner'],
             binaries=[],
             datas=[],
             hiddenimports=['cmath'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='User Group CSV Cleaner',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='User Group CSV Cleaner')
app = BUNDLE(coll,
             name='User Group CSV Cleaner.app',
             icon='icon.icns',
             bundle_identifier=None)
