import time

import discord

import data

import _embeds.errors as _err
import _embeds.ephemeral as _eph
import _embeds.dm as _dm
import _embeds.economy as _eco

async def money(ctx, user: discord.User | discord.Member | None = None, shown: bool | None = False):
    if user is None: user = ctx.author
    customer = data.User(user.id)
    if customer.name == "Unknown User": customer.name = user.name
    customer.save()

    await ctx.send_response(embed = _eco.money(user, customer.money), ephemeral=not shown)

async def pay(ctx, user: discord.User | discord.Member, amount: int, reason: str | None = None):
    customer = data.User(ctx.author.id)
    seller = data.User(user.id)

    amount = int(amount)

    if customer.money >= amount & amount > 0:
        customer.money -= amount
        seller.money += amount

        customer.save()
        seller.save()
        await ctx.send_response(embed = _eph.paid(user, amount))
        await user.send(embed = _dm.paid(ctx.author, amount, reason))
    else:
        await ctx.send_response(embed = _err.notEnoughMoney(), ephemeral = True)

async def sell(ctx, item: str, amount: int, price: int):
    inventory = data.searchItem(owner=ctx.author.id, name=item, forsale=False)
    hasObj = False
    current: dict = {}
    print(inventory)
    for obj in range(len(inventory)):
        current = inventory[obj]
        if current["_name"] == item and int(current["amount"]) >= amount:
            hasObj = True
            break
    
    if hasObj:
        old = data.Item(current["key"], current["_name"], current["value"], current["owner"], current["amount"])
        a = int(old.amount)
        a -= amount
        old.amount = a
        old.save()

        obj = data.Item(round(time.time()), item, price, ctx.author.id, amount)
        obj.sell(price)
        obj.save()
        await ctx.respond("Yes")
    else:
        await ctx.respond("No")