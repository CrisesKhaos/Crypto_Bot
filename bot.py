from api import getPrices
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='>')


@client.command(name="btc" or "BTC" or "bitcoin")
async def bruh(ctx):
    price = str(getPrices.getPrice("BTC"))
    print(price)
    await ctx.send("Hey " + ctx.message.author.mention + ", the current price of Bitcoin(BTC) is ***US$" + price + "***")


@client.command(name="eth" or "ETH" or "ether" or "Ethereum")
async def ether(ctx):
    price = str(getPrices.getPrice("ETH"))
    print(price)
    await ctx.send("Hey " + ctx.message.author.mention + ", the current price of Ethereum(ETH) is ***US$" + price + "***")

client.run('ODIwNjk1NDM0NzkxMjIzMzA2.YE46Lw.PE37uyMqkccw0VEYtXq5pcjQ-Ec')
