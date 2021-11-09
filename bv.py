from pywinauto.application import Application
import time

app = Application ().Start (cmd_line=u'putty -ssh user_name@10.70.15.175')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (1)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("ls")
putty.TypeKeys ("{ENTER}") 
