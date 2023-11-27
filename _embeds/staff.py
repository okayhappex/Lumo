import discord
import bot

def report_user(author, member, reason, channel: discord.TextChannel):
    title = ":rotating_light: Nouveau signalement !"
    description = f"""
    <@{author.id}> vient de signaler <@{member.id}> pour la raison suivante:
    > {reason}

    Salon du signalement: <#{channel.id}>
    """
    color = bot.colors["warning"]

    return discord.Embed(title=title, description=description, colour=color)

def report_message(author, message: discord.Message, channel: discord.TextChannel):
    title = ":rotating_light: Nouveau signalement !"
    description = f"""
    <@{author.id}> vient de signaler un message de <@{message.author.id}>. Contenu du message:
    
    > {message.content}

    Salon du signalement: <#{channel.id}>
    """
    color = bot.colors["warning"]

    return discord.Embed(title=title, description=description, colour=color)

def banned(user: discord.User, reason: str, author: discord.User):
    title = "Nouveau bannissement"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Auteur:** <@{author.id}>
    > **Raison du ban:** {reason}
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)

def unbanned(user: discord.User, reason: str, author: discord.User):
    title = "Bannissement révoqué"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Auteur:** <@{author.id}>
    > **Raison du déban:** {reason}
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def kicked(user: discord.User, reason: str):
    title = "Nouvelle expulsion"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    > **Commentaire:** Il ou elle peut revenir à n'importe quel moment
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)

def muted(user: discord.User, reason: str, duration):
    title = "Réduction au silence"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    > **Durée:** {duration}
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)

def unmuted(user: discord.User, reason: str):
    title = "Annulation d'une sanction"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)