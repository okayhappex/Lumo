import os
import dotenv
import time

import discord
lumo = discord.Bot()

import _commands.events as events
import _commands.moderation as mod
import _commands.economy as money


import _embeds.basic as _basic

bot = lumo.create_group("bot", "Infos à propos du bot")
report = lumo.create_group("signaler", "Signaler du contenu innapproprié")
item = lumo.create_group("article", "Interactions commerciales")

global boot

@lumo.event
async def on_ready():
    global boot
    print(f"Connecté en tant que {lumo.user.name}")
    boot = round(time.time())

@lumo.event
async def on_message(message):
    await events.on_message(message, lumo, boot)




@bot.command(description = "Informations sur Lumo")
async def info(ctx):
    await ctx.respond(embed = _basic.infos(boot))

@bot.command(description = "Connexion du bot")
async def ping(ctx):
    await ctx.respond(embed = _basic.ping(lumo, boot))

@bot.command(description = "Dire quelque chose à la place du bot")
@discord.default_permissions(mention_everyone=True)
async def dire(ctx, contenu: str):
    await ctx.respond(contenu)




@lumo.command(description="Bannit quelqu'un du serveur")
@discord.default_permissions(ban_members=True)
async def ban(ctx, membre: discord.Member, raison: str | None = None):
    await mod.ban(ctx, membre, raison, lumo)

@lumo.command(description = "Autorise un membre banni à rejoindre le serveur")
@discord.default_permissions(ban_members=True)
async def déban(ctx, membre: discord.User, raison: str | None = None):
    await mod.déban(ctx, membre, raison, lumo)

@lumo.command(description = "Expulse un membre du serveur")
@discord.default_permissions(kick_members=True)
async def kick(ctx, membre: discord.User, raison: str | None = None):
    await mod.kick(ctx, membre, raison, lumo)

@lumo.command(description = "Réduit un membre au silence")
@discord.default_permissions(moderate_members=True)
async def mute(ctx, membre: discord.Member, raison: str | None = None, minutes: int | None = None, heures: int | None = None, jours: int | None = None):
    await mod.mute(ctx, membre, raison, minutes, heures, jours, lumo)

@lumo.command(description = "Autorise un membre à parler")
@discord.default_permissions(moderate_members=True)
async def unmute(ctx, membre: discord.Member, raison: str | None = None):
    await mod.unmute(ctx, membre, raison, lumo)

@lumo.command(description = "Avertit un membre")
@discord.default_permissions(moderate_members=True, ban_members=True, kick_members=True)
async def warn(ctx, membre: discord.Member, contenu: str):
    await mod.warn(ctx, membre, contenu)

@report.command(name="membre", description="Signale un utilisateur")
async def report_member(ctx, membre: discord.Member, raison: str):
    await mod.report_member(ctx, membre, raison, lumo)

@report.command(name="message", description = "Signale un message")
async def report_message(ctx, message: discord.Message):
    await mod.report_message(ctx, message, lumo)

@lumo.user_command(name="Signaler")
async def report_member_ctx_menu(ctx, member: discord.Member):
    await report_member(ctx, member, "Signalé via le menu contextuel")

@lumo.message_command(name="Signaler")
async def report_message_ctx_menu(ctx, message: discord.Message):
    await report_message(ctx, message)



@lumo.command(description = "Paye un membre")
async def payer(ctx, membre: discord.User, somme: int, raison: str | None = None):
    await money.pay(ctx, membre, somme, raison)

@lumo.command(description = "Affiche votre argent ou celui d'un autre")
async def argent(ctx, membre: discord.User | None = None, montrer: bool | None = False):
    await money.money(ctx, membre, montrer)

@item.command(name="vendre", description = "Vendre un de vos objets")
async def vendre(ctx, article: str, prix: int, nombre: int):
    await money.sell(ctx, article, nombre, prix)

dotenv.load_dotenv()
lumo.run(str(os.getenv("BOT_TOKEN")))