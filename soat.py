from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 18832737 #my.telegram.org dan olgan apiidni qoying
api_hash = "219b2fe43765100b8373e8e7958c697b" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="O'zbekistonda soat: " +str(x)
    ))
    time.sleep(30)
