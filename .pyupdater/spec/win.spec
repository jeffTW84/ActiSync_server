# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\User\\Desktop\\0_non\\ActiSync_server\\test.py'],
             pathex=['C:\\Users\\User\\Desktop\\0_non\\ActiSync_server', 'C:\\Users\\User\\Desktop\\0_non\\ActiSync_server\\.pyupdater\\spec'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\User\\anaconda3\\envs\\IMM_ActiSync\\lib\\site-packages\\pyupdater\\hooks'],
             hooksconfig={},
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
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='win')
