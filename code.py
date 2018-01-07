import discord
import random
import logging
from discord.ext import commands

bot = commands.Bot(description="The bot for Coder's Paradise whom you can play with!", command_prefix="play.")

logging.basicConfig(
        level = logging.INFO,
        style = '{',
        datefmt = "%d.%m.%Y %H:%M:%S",
        format = "\n{asctime} [{levelname:<8}] {name}:\n{message}"
)

@bot.event
async def on_ready():
    print("------------")
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------------")
    await bot.send_message(discord.User(id="311367735777165314"), content="PlayBot was booted up!", tts=False, embed=None)
    status_code = int(random.randint(1, 3))
    if status_code == 1:
        await bot.change_presence(game=discord.Game(name=str("in Coder's Paradise!")))
    if status_code == 2:
        await bot.change_presence(game=discord.Game(name=str("play. for prefix!")))
    if status_code == 3:
        await bot.change_presence(game=discord.Game(name=str("play.help for commands!")))
    bot.load_extension("ExampleRepl")

class MainCommands:
    async def on_message(self, msg):
        pass

    @commands.command()
    async def hello(self):
        self.bot.say("Hello")

    @commands.command()
    async def ping(self):
        await bot.say("Pong!")

    @commands.command(pass_context=True)
    async def say(self, ctx, *, something=None):
        if something is None:
            await bot.say("Tell me what to say")
        else:
            await bot.say("**{} said:** {}".format(str(ctx.message.author), something))
            await bot.delete_message(ctx.message)

    @commands.command()
    async def kick(self, member: discord.Member):
        await bot.kick(member)
        await bot.say("{} kicked!".format(member))

    @commands.command()
    async def ban(self, member: discord.Member):
        await bot.ban(member)
        await bot.say("{} banned!".format(member))

    @commands.command()
    async def botlogo(self):
        em = discord.Embed(title="CP PlayBot Logo", description="This bot's logo!", color=discord.Colour.magenta())
        em.set_footer()
        em.set_image(url="https://cdn.discordapp.com/avatars/390436469816164352/24709980e4d974cbba52b5e4e91979e4.png")
        await bot.say(embed=em)


bot.add_cog(MainCommands())


bot.run("MzkwNDM2NDY5ODE2MTY0MzUy.DSuJLg.jHizw6p1SOD-PXQtQ9A4ywNua9o")