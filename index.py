import asyncio
from telethon import TelegramClient
from telethon.tl.types import PeerUser
from telethon.tl.functions.channels import GetLeftChannelsRequest, InviteToChannelRequest
from telethon import errors


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'


async def main():
  client = TelegramClient('session_name', api_id, api_hash)
  await client.start()

  try:
    async with client.takeout() as takeout:
      # Number of channels to skip
      offset = 0
      channels = await takeout(GetLeftChannelsRequest(offset))
      f = open('channels.txt', 'a')
      f.write(channels.stringify())
      f.close()

      #After channels.txt is populated. Paste needed channels ids into the array. And run script again
      ids = []
      if len(ids) == 0:
        print('Open channels.txt and look for the needed channels. Copy their ids to the ids = []. Run this script for the third time')
      else:
        selected_channels =  [x for x in channels.chats if x.id in ids]
        I = await client.get_entity('me')
        for channel in selected_channels:
          try:
            await client(InviteToChannelRequest(channel, [I]))
            print('Rejoined ' + channel.title)
          except:
            print('You are not allowed to rejoin ' + channel.title + '. skipped')
        print('Check your Telegram App for the lost channels. If they are not in the chats list, try search')

  except errors.TakeoutInitDelayError as e:
    print('Open your Telegram App. Telegram will send you private message with Data export request. Allow it and run this script for the second time')


asyncio.run(main())
