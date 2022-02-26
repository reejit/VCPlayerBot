from pyrogram.types import Message
from utils import is_admin
from pySmartDL import SmartDL
import os
from pyrogram import (
    Client, 
    filters
    )


admin_filter=filters.create(is_admin) 

@Client.on_message(filters.command(["download"]) & chat_filter)
async def Upload(client: Client, message: Message):
     chat_id = message.chat.id
     if len(message.command) == 1:
        await message.reply_text("No link!")
        return
     else:
       link = message.command[1]     
       download = SmartDL(link, progress_bar=False)
       m = message.reply_text("Downloading")
       download.start(blocking=False)
       while not download.isFinished():
        Eta = download.get_eta(human=True)
        Progress = download.get_progress()*100)
        Bar = download.get_progress_bar())
        m.edit_text(f"Downloading...\nEta: {Eta}\n\n{Bar}Progress: {Progress}")       
        time.sleep(5)
       if download.isSuccessful():
        m.edit_text("DOWNLOAD SUCCESSFUL")
       else:
        for e in download.get_errors():
              m.edit_text(f"Errors\n\n\n{e}")
       video = download.get_dest()
       await client.send_video(chat_id=chat_id, video=video)
       os.remove(video)
