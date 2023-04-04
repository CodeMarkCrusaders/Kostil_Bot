from discord import Message
from discord.ext import commands
import asyncio
from discord import Interaction, InputTextStyle ,Embed
from discord.ui import Modal, InputText
import discord
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)




@bot.event
async def on_message(message: Message):
  kostil_channel = bot.get_channel(1092873574253080636)
  c = ''
  if message.channel.id == 1092884193165455451:
    with open('server_out.txt') as op:
      while True:
        a = op.readline()
        op.seek(0)
        if a != c:
          await kostil_channel.send(f'{a}')
        c = a
        await asyncio.sleep(0.1)
  elif message.author.name == 'Fallout equestria':
    with open('server_in.txt', 'w') as op:
      op.write(message.content)



loop = asyncio.get_event_loop()
loop.create_task(bot.run('TOKEN'))
loop.run_forever()