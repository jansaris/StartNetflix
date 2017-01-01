import subprocess
import xbmc
import os

root = os.getcwd().replace(";","")+"\\"
executable = root+"lib\\NetflixRemoteController.exe"

if xbmc.Player().isPlaying()
	xbmc.log(msg="Stop current video", level=xbmc.LOGNOTICE)
	xbmc.Player().stop()

xbmc.log(msg=("Start " + executable), level=xbmc.LOGNOTICE)
child = subprocess.call([executable, "-k"])