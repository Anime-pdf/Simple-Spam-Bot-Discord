import discord
from discord.ext import commands
from discord.utils import get

msg = "hi"

client = commands.Bot(command_prefix='!')

client.remove_command("help")

@client.event
async def on_ready():
    print ("bot is now online")

@client.command(pass_context=True)
async def setmsg(ctx, *, smg):
	if ctx.author.id==389343709986160642:
		global msg
		msg = smg
		print(f"SET msg TO '{smg}'")
	else:
		pass

@client.command(pass_context=True)
async def spam(ctx, member, ammount):
	if ctx.author.id==389343709986160642:
		global msg
		memberid = int(member[3:21])
		dmusr = client.get_user(memberid)
		dm_channel = await dmusr.create_dm()
		for i in range(int(ammount)):
			await dm_channel.send(msg)
		print(f"SENT {ammount} MESSAGES TO '{dmusr.name}'")
	else:
		pass

@client.command(aliases = ['clear'])
async def __clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount+1)
client.run('NzQwNTc1MjQ2NTA3MTgwMDYy.XyrAcQ.CMV5kR2ykeE148dAKrGEpmdGXrc')