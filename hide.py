import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = 5891777
API_HASH = '64fa91f5fafd43a3b9dc504f0e2a4d70'

bot = Client(
        "hide",
        bot_token=BOT_TOKEN,
	api_hash=API_HASH,
        api_id=API_ID
    )

@bot.on_message(filters.command('start'))
async def start(bot, message):
	text = 'Hey, Im a Join Hider Bot\n\n I Can Delete A Member joined Message.\n\n Add Me To Your Group And Give permission Of delete message.\n\n ©️ @Somalibots'
	await message.reply(text, quote=True)

@bot.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()	


	
bot.run()
#just a simple . nothing special.
