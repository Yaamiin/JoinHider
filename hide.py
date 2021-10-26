import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 5891777))
API_HASH = os.environ.get("API_HASH", "")

bot = Client(
        "hide",
        bot_token=BOT_TOKEN,
	api_hash=API_HASH,
        api_id=API_ID
    )

@bot.on_message(filters.command('start'))
async def start(bot, message):
	text = 'Hey, Im a Join Hider Bot\n\n I Can Delete A Member joined Message.\n\n Add Me To Your Group And Give permission Of delete message.'
	await message.reply(text, quote=True)

@bot.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()	

@bot.on_message(filters.member_invited)
async def welcome(bot, message):
        await message.delete()
	
bot.run()
