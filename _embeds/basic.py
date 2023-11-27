import discord
import bot

# Basic

def infos(boot):
    title = f":information_source: Informations sur Lumo"
    description = f"""
    Salut à toi, Moi c'est Lumo: un bot de modération. Tu trouveras peut-être meilleur que moi, mais tu ne trouveras pas plus charismatique. Pour t'épargner la lecture, j'ai raccourci ma description :arrow_down:

    **Version:** {bot.infos["version"]}

    **:robot: Application**
    **Création:** <t:{bot.infos["created"]}:R>, le <t:{bot.infos["created"]}:D>
    **Développeur:** <@{bot.infos["dev"]}>
    **ID:** {bot.infos["ID"]}

    **:computer: Pour les hackers (ou les stalkers)**
    **Dernier démarrage:** <t:{boot}:R>
    **Version de Python:** 3.11.4
    **Version de Pycord:** 2.4.1
    """
    color = bot.colors["main"]

    return discord.Embed(title=title, description=description, colour=color)

def ping(lumo: discord.Bot, boot: int):
    title = "Lumo fonctionne :)"
    description = f"""
    **Dernier démarrage:** <t:{boot}:R>
    **Version de Python:** 3.11.4
    **Version de Pycord:** 2.4.1
    **Latence:** {round(lumo.latency * 1000)}ms
    """
    color = bot.colors["main"]
    
    return discord.Embed(title=title, description=description, colour=color)
