import discord
import bot

def banned(user: discord.User, reason: str):
    title = "Bannissement réussi"
    description = f"""
    > **Mention:** <@{user.id}>
    > **ID du compte:** {user.id}
    > **Raison du ban** {reason}
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def unbanned(user: discord.User, raison: str):
    title = "Bannissement révoqué"
    description = f"""
    > **ID du compte:** {user.id}
    > **Raison:** {raison}
    """
    color = bot.colors["warning"]

    return discord.Embed(title=title, description=description, colour=color)

def kicked(user: discord.User, reason: str):
    title = "Expulsion réussie !"
    description = f"""
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    > **Commentaire:** {user.display_name} peut revenir à n'importe quel moment
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def muted(user: discord.User, reason: str, duration, problem: str | None = None):
    if problem == "noDurationProvided": problem = "Le mute durera 30 minutes (aucune durée spécifiée)"
    else: problem = "N/A"

    title = "Réduction au silence"
    description = f"""
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    > **Durée: ** {duration}
    > **Commentaire: ** {problem}
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def unmuted(user: discord.User, raison: str):
    title = "Parole retrouvée"
    description = f"""
    > **ID du compte:** {user.id}
    > **Raison:** {raison}
    """
    color = bot.colors["warning"]

    return discord.Embed(title=title, description=description, colour=color)

def warn(user, reason):
    title = "Avertissement reçu"
    description = f"""
    > **ID du compte:** {user.id}
    > **Raison:** {reason}
    """
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def reported(author: discord.Member):
    title = f"Merci pour votre signalement, {author.name} !"
    description = ":white_check_mark: Un membre du staff devrait se charger du signalement."
    color = bot.colors["success"]

    return discord.Embed(title=title, description=description, colour=color)

def paid(user: discord.User, amount: int):
    title = "Payement effectué"
    description = f"""
    > **Somme:** {amount}
    > **Receveur:** {user.id} (<@{user.id}>)
    """
    color = bot.colors["economy"]

    return discord.Embed(title=title, description=description, colour=color)
