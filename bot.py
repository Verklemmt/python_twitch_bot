from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self, irc_token, client_id, nick, prefix, initial_channels):
        super().__init__(irc_token=irc_token, client_id=client_id, nick=nick, prefix=prefix,
                         initial_channels=initial_channels)

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    async def event_pubsub(self, data):
        pass

    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')
