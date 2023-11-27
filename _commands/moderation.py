from datetime import timedelta

import discord

import _embeds.dm as _dm
import _embeds.ephemeral as _eph
import _embeds.errors as _error
import _embeds.staff as _staff
import data

async def ban(ctx, membre, raison, lumo):
    me = ctx.guild.me
    guildcfg = data.config[str(ctx.guild.id)]
    logs = guildcfg["logs"]
    channel = lumo.get_channel(logs["channel"])

    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif ctx.guild.me.guild_permissions.ban_members and not membre.guild_permissions.administrator:
        if raison is None: raison = "Aucune"

        await channel.send(embed = _staff.banned(membre, raison, ctx.author))
        await membre.send(embed = _dm.ban(raison, ctx.guild))
        await membre.ban(reason = raison)
        await ctx.send_response(embed = _eph.banned(membre, raison), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.missing_perms("Bannir des membres"), ephemeral=True)

async def déban(ctx, membre, raison, lumo):
    me = ctx.guild.me
    guildcfg = data.config[str(ctx.guild.id)]
    logs = guildcfg["logs"]
    channel = lumo.get_channel(logs["channel"])

    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif ctx.guild.me.guild_permissions.ban_members:
        if raison is None: raison = "Aucune"

        await channel.send(embed = _staff.unbanned(membre, raison, ctx.author))
        await ctx.guild.unban(membre, reason = raison)
        await ctx.send_response(embed = _eph.unbanned(membre, raison), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.missing_perms("Bannir des membres"), ephemeral=True)

async def kick(ctx, membre, raison, lumo):
    me = ctx.guild.me
    guildcfg = data.config[str(ctx.guild.id)]
    logs = guildcfg["logs"]
    channel = lumo.get_channel(logs["channel"])

    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif ctx.guild.me.guild_permissions.kick_members and not membre.guild_permissions.administrator:
        if raison is None: raison = "Aucune"

        await channel.send(embed = _staff.kicked(membre, raison))
        await ctx.guild.kick(membre)
        await membre.send(embed = _dm.kick(raison, ctx.guild))
        await ctx.send_response(embed = _eph.kicked(membre, raison), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.missing_perms("Expulser des membres"), ephemeral=True)

async def mute(ctx, membre, raison, minutes, heures, jours, lumo):
    me = ctx.guild.me
    guildcfg = data.config[str(ctx.guild.id)]
    logs = guildcfg["logs"]
    channel = lumo.get_channel(logs["channel"])

    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif ctx.guild.me.guild_permissions.moderate_members and not membre.guild_permissions.administrator:
        if raison is None: raison = "Aucune"

        if heures is None: heures = 0
        if minutes is None: minutes = 0
        if jours is None: jours = 0

        if heures + jours + minutes > 0 and jours < 28:
            await channel.send(embed = _staff.muted(membre, raison, timedelta(days=jours, minutes=minutes, hours=heures)))
            await membre.timeout_for(timedelta(days=jours, minutes=minutes, hours=heures))
            await ctx.send_response(embed = _eph.muted(membre, raison, timedelta(days=jours, minutes=minutes, hours=heures)), ephemeral=True)
        else:
            await channel.send(embed = _staff.muted(membre, raison, timedelta(minutes=30)))
            await membre.timeout_for(timedelta(minutes=30))
            await ctx.send_response(embed = _eph.muted(membre, raison, timedelta(minutes=30), "noDurationProvided"), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.missing_perms("Réduire au silence (modérer les membres)"), ephemeral=True)
    
async def unmute(ctx, membre, raison, lumo):
    me = ctx.guild.me
    guildcfg = data.config[str(ctx.guild.id)]
    logs = guildcfg["logs"]
    channel = lumo.get_channel(logs["channel"])

    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif ctx.guild.me.guild_permissions.moderate_members and not membre.guild_permissions.administrator:
        if raison is None: raison = f"{ctx.author.name} n'a donné aucune raison"
        else: raison = f"{ctx.author.name}: {raison}"

        await channel.send(embed = _staff.unmuted(membre, raison))
        await membre.remove_timeout(reason = raison)
        await ctx.send_response(embed = _eph.unmuted(membre, raison), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.missing_perms("Réduire au silence (modérer les membres)"), ephemeral=True)
    
async def warn(ctx, membre, contenu):
    me = ctx.guild.me
    if membre.id == me.id:
        await ctx.send_response(embed = _error.action_on_myself(), ephemeral=True)
    elif (not membre.guild_permissions.administrator) or ctx.author.guild_permissions.administrator:
        await membre.send(embed = _dm.warn(contenu, ctx.guild))
        await ctx.send_response(embed = _eph.warn(membre, contenu), ephemeral=True)
    else:
        await ctx.send_response(embed = _error.target_is_admin(), ephemeral=True)

async def report_member(ctx, membre, raison, lumo):
    guildcfg = data.config[str(ctx.guild.id)]
    reports = guildcfg["reports"]
    print(reports["channel"])
    channel = lumo.get_channel(int(reports["channel"]))

    await channel.send(content=f"<@&{reports['mention']}>", embed=_staff.report_user(ctx.author, membre, raison, ctx.channel))
    await ctx.send_response(embed = _eph.reported(ctx.author), ephemeral=True)

async def report_message(ctx, message, lumo):
    guildcfg = data.config[str(ctx.guild.id)]
    reports = guildcfg["reports"]
    channel = lumo.get_channel(int(reports["channel"]))

    await channel.send(content=f"<@&{int(reports['mention'])}>", embed=_staff.report_message(ctx.author, message, ctx.channel))
    await ctx.send_response(embed = _eph.reported(ctx.author), ephemeral=True)