import vlc

import sys
import time

print(sys.platform)

if sys.platform == "darwin":
  from PyQt5 import QtCore
  from PyQt4 import QtGui
  # import sys

  vlcApp =QtGui.QApplication(sys.argv)
  vlcWidget = QtGui.QFrame()
  vlcWidget.resize(700,700)
  vlcWidget.show()
  player.set_nsobject(vlcWidget.winId())

player.play()

# Create Player Object and set MRL (your_video.mp4)
# player = vlc.MediaPlayer('hill.mov')

# Basic Commands associated with the class object
# player.play()

# time.sleep(2.4)

# player.pause()

# time.sleep(2.4)

# player.play()

# time.sleep(2.4)

# player.payse()


