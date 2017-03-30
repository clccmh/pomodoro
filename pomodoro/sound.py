import winsound
import platform

if platform.system() == "Windows":
  for i in range(2):
    winsound.Beep(800, 250)
    winsound.Beep(600, 250)
    winsound.Beep(1000, 250)
  winsound.Beep(800, 250)
