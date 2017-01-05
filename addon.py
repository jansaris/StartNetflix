import subprocess
import xbmc
import xbmcaddon

addondir = xbmcaddon.Addon(id='script.StartNetflix').getAddonInfo('path')
executable = addondir + "\\resources\\lib\\NetflixRemoteController.exe"

if xbmc.Player().isPlaying():
	xbmc.log(msg="Stop current video", level=xbmc.LOGNOTICE)
	xbmc.Player().stop()

xbmc.log(msg=("Start " + executable), level=xbmc.LOGNOTICE)
child = subprocess.call([executable, "smstextentry"])
xbmc.log(msg=("Finished " + executable), level=xbmc.LOGNOTICE)