from telethon import TelegramClient, events, Button
api_id = 15563529
api_hash = 'c8e8a927f89fd5d00322c00760035030'
token = '5106990765:AAGVD4xpGDiJQlZxbsQozi1XTvxf98bHxGU'
client = TelegramClient("legendx", api_id, api_hash).start(bot_token=token)
'''
ophghf
'''
rishabh = [Button.url('JOIN THANOS', 'https://t.me/rishuxp')]
@client.on(events.NewMessage(incoming=True))
async def start(event):
#echo = event.text
# await event.reply(echo)
  msg = f'SENDER USERNAME: {event.sender.username} AND SENDER user id: {event.sender.id} message: {event.text}'
  await client.send_message("Ultron_owner", msg, link_preview=False, buttons=rishabh)
# event.sender.first_name = sender ka first name
# event.sender.last_name = sender ka last name

# complete exercize please
	
	
client.run_until_disconnected()
