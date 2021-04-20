import discord
import os
from api import getPrices
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

BOT_ID = os.getenv('BOT')

client = commands.Bot(command_prefix='>')


@client.command(name="btc" or "BTC" or "bitcoin")
async def bruh(ctx):
    price = str(getPrices.getPrice("BTC"))
    print(price)
    await ctx.send("Hey " + ctx.message.author.mention + ", the current price of Bitcoin(BTC) is ***US$ " + price + "***")


@client.command(name="eth" or "ETH" or "ether" or "Ethereum")
async def ether(ctx):
    price = str(getPrices.getPrice("ETH"))
    print(price)
    await ctx.send("Hey " + ctx.message.author.mention + ", the current price of Ethereum(ETH) is ***US$ " + price + "***")


@client.command(name="doge" or "DOGE")
async def doge(ctx):
    price = str(getPrices.getPrice("DOGE"))
    print(price)
    await ctx.send("Hey " + ctx.message.author.mention + ", the current price of DOGE is ***US$ " + price + "***")

client.run(BOT_ID)
