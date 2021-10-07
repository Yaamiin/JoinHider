import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Button

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", 8451490))

API_HASH = os.environ.get("API_HASH", "")
bot = Client(
        "hide",
        bot_token=BOT_TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

@bot.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Im JoinHider**,\n\nAdd me as an admin your group. Made In India 🇮🇳",
                    buttons=(
                      [Button.url('Add Me', 'https://t.me/JOlNHlDERBOT?startgroup=true'),
                      Button.url('📜 Source', 'https://github.com/TechnicalHunter/JoinHider/tree/Tanaji')]
                    ),
                    link_preview=False
                   )

@bot.on_message(filters.new_chat_members)
async def welcome(bot,message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	await message.delete()	


	
bot.run()
