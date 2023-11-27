import discord
import bot

def money(user: discord.User | discord.Member, money: int):
    title = f"Monnaie de {user.display_name}"
    description = f"""
    Vous avez: **{money}€**
    Tapez </inventaire:1234> pour voir les objets que vous possédez
    """
    color = bot.colors["economy"]

    return discord.Embed(title=title, description=description, colour=color)
