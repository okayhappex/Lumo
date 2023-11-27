from random import *

import discord
import data

import _embeds.basic as _basic

async def on_message(message: discord.Message, lumo: discord.Bot, boot: int):
    user = data.User(message.author.id)
    user.save()
    
    if user.name == "Unknown User": user.name = message.author.name
    user.money += randint(5, 10)
    if user.premium: user.money += randint(5, 10)
    if user.blocked: user.money = 0
    user.save()

    if message.content == "<@1153244564820340736>":
        await message.reply(embed = _basic.ping(lumo, boot))