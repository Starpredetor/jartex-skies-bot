import asyncio
import discord
from discord.ext import commands
from utils.helpers import parse_duration


class Moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        self.last_member = None

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.Member, *, reason=None):
        author = ctx.author
        try:
            await user.send(f"You have been kicked from jartex Skies for: {reason}")
        except Exception as excp:
            pass
        try: 
            await user.kick(reason=reason)
        except Exception as e:
            await ctx.reply(f"Couldn't kick the user due to: {e}")
        logs_embed = discord.Embed(title="Kicked user", description="A user was Kicked", color=0xff8000)
        logs_embed.add_field(name="**Kicked**", value=user)
        logs_embed.add_field(name="**Reason**", value=reason)
        logs_embed.add_field(name="Moderator", value=author.mention)
        logs_embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=logs_embed)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user:discord.Member, *, reason=None):
        author = ctx.author
        try:
            await user.send(f"You have been Banned from jartex Skies for: {reason}")
        except Exception as excp:
            pass
        try: 
            await user.ban(reason=reason)
        except Exception as e:
            await ctx.reply(f"Couldn't ban the user due to: {e}")
        logs_embed = discord.Embed(title="Banned user", description="A user was Banned", color=0xff0000)
        logs_embed.add_field(name="**Banned**", value=user)
        logs_embed.add_field(name="**Reason**", value=reason)
        logs_embed.add_field(name="Moderator", value=author.mention)
        await ctx.send(embed=logs_embed)

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        author = ctx.author
        member_name, member_discriminator = member.split('#')

       

        unbanned = discord.Embed(color=0x009933)
        unbanned.set_author(name="Unbanned")
        unbanned.set_thumbnail(url=ctx.author.avatar_url)
        unbanned.add_field(name="Unbanned", value=f'{member_name}#{member_discriminator}', inline=False)
        unbanned.add_field(name="Moderator", value=f'{author}', inline=False)

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=unbanned)
        try:
            await user.send(f"You have been unbanned on Jartex Skies.")
        except:
            pass

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user:discord.Member, duration: str, *, reason=None):
        author = ctx.author
        muted_role = ctx.guild.get_role(933372388840722492)
        time = parse_duration(duration)
        logs_embed = discord.Embed(title="Muted user", description="A user was Muted", color=0xff8000)
        logs_embed.add_field(name="**Muted**", value=user)
        logs_embed.add_field(name="**Reason**", value=reason)
        logs_embed.add_field(name="Moderator", value=author.mention)
        if duration[-1] == "w":
            logs_embed.add_field(name="**Duration**", value=f"{duration[0:-1]}week(s)")
        elif duration[-1] == "d":
            logs_embed.add_field(name="**Duration**", value=f"{duration[0:-1]}day(s)")
        elif duration[-1] == "h":
            logs_embed.add_field(name="**Duration**", value=f"{duration[0:-1]}hour(s)")
        elif duration[-1] == "m":
            logs_embed.add_field(name="**Duration**", value=f"{duration[0:-1]}minute(s)")
        elif duration[-1] == "s":
            logs_embed.add_field(name="**Duration**", value=f"{duration[0:-1]}second(s)")
        else:
            pass
        unmuted_embed = discord.Embed(title="Unmuted user", description="A user was Unmuted", color=0xff8000)
        unmuted_embed.add_field(name="**Unmuted**", value=user)
        unmuted_embed.add_field(name="**Reason**", value="Mute expire")
        unmuted_embed.add_field(name="Moderator", value=author.mention)

        if time != -1:
            try:
                await user.add_roles(muted_role)
                await ctx.send(embed=logs_embed)
                await asyncio.sleep(time)
                try:
                    await user.remove_roles(muted_role)
                except Exception as e:
                    print(e)
                else:
                    await ctx.send(embed=unmuted_embed)
            except Exception:
                pass
        else:
            await ctx.reply("Invalid Duration type please try from [w, d, h, m, s]")
            
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member,*,reason=None):
        author = ctx.author
        muted_role = ctx.guild.get_role(933372388840722492)
        unmuted_embed = discord.Embed(title="Unmuted user", description="A user was Unmuted", color=0xff8000)
        unmuted_embed.add_field(name="**Unmuted**", value=user)
        unmuted_embed.add_field(name="**Reason**", value=reason)
        unmuted_embed.add_field(name="Moderator", value=author.mention)
        try:
            await user.remove_roles(muted_role)
            await ctx.send(embed=unmuted_embed)
        except Exception:
            await ctx.send("Couldn't Unmute the given user")

