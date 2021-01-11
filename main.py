import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=".", intents = intents)
client.remove_command("help")

# VARIABLES

wordlist = ['hello', 'Hello', 'hewo', 'Hewo', 'hewwo', 'Hewwo', 'hey', 'Hey']

filtered_words = ['fuck','Fuck','shit','Shit','Nigga','nigga','retard','Retard','cunt','Cunt','bitch','Bitch']

welcome = ['welc', 'Welc']

# ON READY


@client.event
async def on_ready():
	
	await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = "the birds chirp. | !help"))
	
	print("Bot is ready! :)")


# HELP MENUS

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "⋅˚₊  ⸝⸝ ୨୧ ゛Goddess Commands ︵˚. ɞ", description = "prefix : **.** \n\
[] = optional args || <> = required args \n\
> \n\
 ⋮ **moderation commands!** \n\
♦︎ kick \n\
♦︎ ban/unban \n\
♦︎ clear \n\
♦︎ mute/unmute \n\
> \n\
 ⋮ **portal commands** \n\
♦︎ mass \n\
♦︎ finished \n\
> \n\
⋮ **misc commands** \n\
♦︎ whois \n\
> \n\
⋮ **information!** \n\
***main dev*** :: <@!744260291851845842> \n\
***goddess team*** :: <@!744260291851845842> <@!591893813920792586> \n\
***version*** :: v.1.0 \n\
***custom server bot for*** :: ₍✧₎ .. *. ⋆.  ꒰ enchanted portal ꒱", color = 0xf8f8f9)
	
    await ctx.send(embed = em)

@help.command()
async def kick(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛kick command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> kicks a user from the guild/server! \n\
♦︎ ⋮ **command!** \n\
> !kick <member> [reason] \n\
♦︎ **please provide a reason as it keeps everything neat!** \n\
> aliases :: k \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛ban command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> bans a user from the guild/server! \n\
♦︎ ⋮ **command!** \n\
> !ban <member> [reason] \n\
♦︎ **please provide a reason as it keeps everything neat!** \n\
> aliases :: b \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛unban command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> unbans a user from the guild/server! \n\
♦︎ ⋮ **command!** \n\
> !unban <member> \n\
♦︎ **to use this command, we use the user's username along with ID (ex :: bee (´･ᴗ･`) \n\
#0001)** \n\
> aliases :: ub \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛mute command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> mute a user in the guild/server! \n\
♦︎ ⋮ **command!** \n\
> !mute <member> \n\
♦︎ **to use this command, we use the user's @ping (ex :: <@!744260291851845842>** \n\
> aliases :: m \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛unmute command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> unmutes a user in the guild/server! \n\
♦︎ ⋮ **command!** \n\
> !unmute <member> \n\
♦︎ **to use this command, we use the user's @ping (ex :: <@!744260291851845842>** \n\
> aliases :: um \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛clear command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> clears the set number of messages! \n\
♦︎ ⋮ **command!** \n\
> !purge <amount> \n\
♦︎ **the ran command counts as __one__ message, so if we needed to clear 10 messages we would say `!purge 11`** \n\
> aliases :: p,, purge,, c \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)

    await ctx.send(embed = em)

@help.command()
async def whois(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛whois command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> shows the listed stats for a user! \n\
♦︎ ⋮ **command!** \n\
> !whois <member> \n\
♦︎ **to use this command, we use the user's @ping (ex :: <@!744260291851845842>** \n\
> aliases :: info,, user,, userinfo \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def mass(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛mass command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> provides information on the steps to mass with us along with giving you a pm-portal access role! \n\
♦︎ ⋮ **command!** \n\
> !mass \n\
♦︎ **this is the command that allows you to mass with us!** \n\
> aliases :: \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

@help.command()
async def finished(ctx):
    em = discord.Embed(title ="♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", description = "⋅˚₊ ♦︎ ⸝⸝ ୨୧ ゛finished command! ︵˚. ɞ \n\
♦︎ ⋮ **description!** \n\
> provides information on the steps to close the ticker and/or finish along with giving you a massed role and removes your pm-access role! \n\
♦︎ ⋮ **command!** \n\
> !finished \n\
♦︎ **this is the command that allows you to complete your mass with us!** \n\
> aliases :: \n\
♦︎ ⋮ **︶︶︶︶︶︶︶︶︶!**", color = 0xf8f8f9)
    
    await ctx.send(embed = em)

# COMMANDS


@client.command()
async def mass(ctx):
	role = ctx.guild.get_role(788213344393887744)
	await ctx.author.add_roles(role)

	embed = discord.Embed(title="**looking to mass?**", color=0xf8f8f9)
	embed.add_field(
		name="⠂꒦．thank you for opening a ticket! please **follow** the steps below to mass !!" , 
		value="∿ ✧ ⠂**send** your advertisement (limit of 5 ads) in **codeblock**. \n\
⠂꒦．then start **posting** from **bottom** to **top** all of the channels below with an ad. \n\
∿ ✧ ⠂once **finished** send a few pictures **here** of “proof” that you posted. \n\
╰ <:w_heart:787789783724064788> ：then **we** will post your advertisements into the listed servers, once we’ve sent the “done” go ahead and say `!finished` to remove your pm-access role.٫ ⠂" , 
		inline = True)
	await ctx.send(embed=embed)


@client.command()
async def finished(ctx):
	massed = ctx.guild.get_role(788567632596303933)
	await ctx.author.add_roles(massed)

	removerole = ctx.guild.get_role(788213344393887744)
	await ctx.author.remove_roles(removerole)

	embed = discord.Embed(title="**wowza, finished already?**", color=0xf8f8f9)
	embed.add_field(
	    name=
	    "let me just remove your pm-channel access so it isn’t as crowded..",
	    value=
	    "⠂꒦．you have now been rewarded with the <@&788567632596303933> role! \n\
∿ ✧ ⠂if you have any questions send them before you close the ticket. this means do not close the ticket if you still have questions. \n\
╰ <:w_heart:787789783724064788> ：thank you so much for massing with us (make sure to leave a review for us in <#788557574223298622>).٫ ⠂"
	)
	await ctx.send(embed=embed)


@client.command(aliases=['info', 'user', 'userinfo'])
async def whois(ctx, member: discord.Member):
	embed = discord.Embed(
	    title="**꒱꒱ loading . .**" , description=member.mention + "**'s profile has loaded succesfully.**" , color=0xf8f8f9)
	embed.add_field(name="ID!", value=member.id, inline=True)
	embed.add_field(name="Join Date!", value=member.joined_at.strftime("%a, %#d %b %Y, %I:%M %p CST"), inline=True)
	embed.add_field(
	    name="Account Creation!", value=member.created_at.strftime("%a, %#d %b %Y, %I:%M %p CST"), inline=True)
	embed.add_field(
	    name="Top Role!", value=member.top_role.mention, inline=True)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(
	    icon_url=ctx.author.avatar_url, text=f"requested by {ctx.author.name}")
	await ctx.send(embed=embed)
        

# MODERATION


@client.command(aliases=['purge','c'])
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx,
               member: discord.Member,
               *,
               reason="No reason has been provided!"):
	try:
		await member.send(
		    "You have been kicked from Enchanted Portal. The reason is: " +
		    reason)
	except:
		await ctx.send(
		    "The member has their DMs closed but we'll kick them anyways.")

	await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx,
              member: discord.Member,
              *,
              reason="No reason has been provided."):
	try:
		await member.send(member.name +
		                  " has been banned from the server. Reason: " +
		                  reason)
	except:
		await ctx.send(
		    "The member has their DMs off but we will ban them anyways.")
	await member.ban(reason=reason)


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc, = member.split('#')

	for banned_entry in banned_users:
		user = banned_entry.user

		if (user.name, user.discriminator) == (member_name, member_disc):

			await ctx.guild.unban(user)
			await ctx.send(member_name + " has been unbanned!")
			return

@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member : discord.Member):
    removerole = ctx.guild.get_role(788173190512771082)
    await ctx.author.remove_roles(removerole)

    await ctx.send(member.mention + "has been unmuted.")

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(788173190512771082)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + "has been muted.")
		
@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send("Sorry but you can't do that in our forest, " + ctx.author.mention + ".")
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(ctx.author.mention + " is trying to call a command but forgot to add something to the command! Ack.")


# EVENTS


# @client.event
# async def on_message(msg):
# 	if msg.author == client.user:
# 		return None
# 
# 	for word in wordlist:
# 		if word in msg.content:
# 			await msg.channel.send("Oh! Hello there!")
# 
# 	for word in filtered_words:
# 		if word in msg.content:
# 			await msg.delete()
# 
# 	for word in welcome:
# 		if word in msg.content:
# 			await msg.add_reaction("<:w_heart:787789783724064788>")
# 
# 	for word in welcome:
# 		if word in msg.content:
# 			await msg.add_reaction# ("<:p_cherryblossoms:787504360686092299>")
# 	await client.process_commands(msg)


client.run('')

