import vlc 
import time 
p = vlc.MediaPlayer(r"C:\Users\BapiTripathy\Desktop\Python\Chapter_01\test\play.mp3")
p.play()
time.sleep(17)
p.stop()
