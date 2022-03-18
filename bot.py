from telethon import TelegramClient, events
api_id = 15563529
api_hash = "c8e8a927f89fd5d00322c00760035030"
token = "5106990765:AAGVD4xpGDiJQlZxbsQozi1XTvxf98bHxGU"
client = TelegramClient("rishabh",api_id,api_hash).start(bot_token=token)
@client.on(events.NewMessage(incoming=True))
async def start(event):
   rishabh = event.text
   await event.reply(rishabh)


   client.run_utils_disconnected()