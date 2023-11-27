import discord
import bot

def ban(reason, guild):
    title = ":lock: Vous avez été banni"
    description = f"""
    **Vous avez été banni du serveur {guild.name} pour la raison suivante:**
    > _{reason}_
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)

def kick(reason, guild):
    title = ":x: Vous avez été expulsé"
    description = f"""
    **Vous avez été expulsé du serveur {guild.name} pour la raison suivante:**
    > _{reason}_

    Vous pouvez toujours revenir grâce à une invitation.
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)

def warn(reason, guild):
    title = ":warning: Vous avez reçu un avertissement"
    description = f"""
    **Vous avez reçu un avertissement sur le serveur {guild.name} pour la raison suivante:**
    > _{reason}_
    """
    color = bot.colors["sanction"]

    return discord.Embed(title=title, description=description, colour=color)


def paid(author: discord.User, amount: int, reason: str | None = None):
    if reason is None: reason = "Aucune"

    title = "Vous avez reçu de l'argent"
    description = f"""
    Vous venez de recevoir de l'argent de la part de <@{author.id}>:

    > **Montant:** {amount}
    > **Raison:** {reason}
    """
    color = bot.colors["economy"]

    return discord.Embed(title=title, description=description, colour=color)