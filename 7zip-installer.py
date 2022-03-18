import win32api,win32con
import time
msg = '''Cannot install Seven Zip Services,

The system cannot find the file specified. 0x0002(win32:2
ERROR_FILE_NOT_FOUND)
'''
time.sleep(2)
win32api.MessageBox(0,'The version of Windows Defender Service is too low.','7zip - Warn',win32con.MB_ICONWARNING)
time.sleep(10)
win32api.MessageBox(0,msg,'7zip - Fatal error',win32con.MB_ICONERROR)