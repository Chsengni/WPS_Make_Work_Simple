import win32api
import win32gui

import win32con


def setWallpaper(path):
    reg_key=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")
#    win32api.RegSetValueEx(reg_key,"Wallpaper")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)

setWallpaper("C:\\Users\\xiaolin\\Pictures\\Camera Roll\\001.jpg")
