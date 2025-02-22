from pyrogram.types import Message
from utils import is_admin
from pySmartDL import SmartDL
import os
from pyrogram import (
    Client, 
    filters
    )
from bot import bot


admin_filter=filters.create(is_admin) 

@bot.on_message(filters.command(["download"]) & chat_filter)
async def Upload(bot, message):
     
     if len(message.command) == 1:
        await message.reply("No link!")
        return
     link = message.command[1]     
     download = SmartDL(link, progress_bar=False)
     m = message.reply("Downloading")
     download.start(blocking=False)
     while not download.isFinished():
      Eta = download.get_eta(human=True)
      Progress = download.get_progress()*100)
      Bar = download.get_progress_bar())
      m.edit(f"Downloading...\nEta: {Eta}\n\n{Bar}Progress: {Progress}")       
      time.sleep(5)
     if download.isSuccessful():
      m.edit("DOWNLOAD SUCCESSFUL")
     else:
      for e in download.get_errors():
            m.edit(f"Errors\n\n\n{e}")
     video = download.get_dest()
     await m.edit("Uploading to you")
     await client.send_video(chat_id=chat_id, video=video)
     os.remove(video)
