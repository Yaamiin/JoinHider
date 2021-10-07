import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bot = Client(
    "BotNameHere",
     api_id = int(os.environ.get("APP_ID"))
     api_hash = os.environ.get("API_HASH")
     bot_token = os.environ.get("BOT_TOKEN")
)

@bot.on_message(filters.new_chat_members)
async def welcome(bot,message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	await message.delete()	


	
bot.run()
