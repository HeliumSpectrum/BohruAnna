#BohruAnna new code
import sys
print(sys.executable)
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()
client.run('NzMwMDA5ODg1NDE2MzU3OTY4.XwXvdg.t0k_YQXdKLRfmkgSFFLvxQTqhTw')
