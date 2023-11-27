import discord
import bot

def missing_perms(perm: str):
    title = "Impossible d'effectuer l'action !"
    description = f"""
    Pour celà, il faut que j'aie accès à la permission `{perm}`, vous pouvez l'activer en modifiant l'un de mes rôles.
    **Rappel: Seul le propriétaire du serveur peut modérer un membre avec la permission `administrator`.**
    """
    color = bot.colors["failure"]

    return discord.Embed(title=title, description=description, colour=color)

def action_on_myself():
    title = "Impossible d'effectuer une action sur moi-même"
    description = f"""
    Je suis désolé, mais il va falloir le faire avec un autre bot pour me modérer. Juste par curiosité... avez-vous un problème avec moi ?
    """
    color = bot.colors["failure"]
    return discord.Embed(title=title, description=description, colour=color)

def target_is_admin():
    title = "Impossible d'effectuer l'action"
    description = """Vous n'avez pas le droit d'effectuer des actions sur les administrateurs. Seul le propriétaire du serveur peut le faire, par ses propres moyens."""
    color = bot.colors["failure"]

    return discord.Embed(title=title, description=description, colour=color)


def notEnoughMoney():
    title = "Payement refusé"
    description = "Essayer de parler un peu plus dans vos serveurs ou de vous faire de l'argent d'un autre moyen."
    color = bot.colors["failure"]

    return discord.Embed(title=title, description=description, colour=color)