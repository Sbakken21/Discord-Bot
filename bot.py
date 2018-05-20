import discord
from discord.ext import commands
import asyncio
import re
import random
from imgurpython import ImgurClient
import config
import pgDB

# Imgur API
client = ImgurClient(config.client_id, config.client_secret)

bot = commands.Bot(command_prefix='/', description='JojoBot')

# Cogs/extensions
startup_extensions = ["trivia"]

status_updates = ['/help', 'with the Joestars', 'anything but PoE']
# React with Dio emoji
emoji_react = ['339924033443332096']

@bot.event
async def on_ready():
    print("Connected: JojoBot Online")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("=============================")
    for status in status_updates:
        status_updates.append(status) # makes the list continue
        await bot.change_presence(game=discord.Game(name=status, type=0))
        await asyncio.sleep(60)

@bot.event
async def on_message(message):
    # stop bot from replying to itself
    if message.author == bot.user:
        return

    # Create list of banned words
    blacklist_word = config.blacklist_word.split(',')

    # Parse message content for match to blacklist word
    for word in blacklist_word:
        if re.search(word, message.content.replace(" ", ""), re.IGNORECASE):
            await bot.delete_message(message)
            await bot.send_message(message.channel, '⚠ ' + message.author.mention + ' ' + config.response)

    # Check for words that bot will react with using emoji
    react_words = config.react_words.split(',')

    for word in react_words:
        if re.search(word.strip(), message.content, re.IGNORECASE):
            await bot.add_reaction(message, 'Dio:339924155921203201')

    # Check for bannable words
    ban_words = config.ban_list.split(',')

    for word in ban_words:
        if word.strip().lower() in message.content.lower():
            await bot.delete_message(message)
            if message.author == 162432523366957057:
                await bot.send_message(message.channel, '⚠ ' + message.author.mention + ' ' + config.response_ban)
            else:
                await bot.send_message(message.channel, '⚠ ' + message.author.mention + " you're not Dante, don't try to be")

    # Allow bot commands to function
    await bot.process_commands(message)

@bot.command()
async def dio_pasta():
    """Dio CopyPasta"""
    await bot.say(config.dio_pasta)


@bot.command(description=config.dio_desc)
async def dio():
    """Dio Picture"""
    await bot.say(config.dio_desc)

@bot.command()
async def pizza():
    """Pizza Picture"""
    await bot.say(config.dio_pizza)

@bot.command()
async def meme():
    """Random JoJo(usually) meme"""
    albums = config.albums.split(',')

    # Compile list of all albums
    items = sum([client.get_album_images(album.strip()) for album in albums], [])

    # Get list of individual image links from list of albums
    links = [item.link for item in items]

    # Return random image link from list
    await bot.say(random.choice(links))

#Commands for adding a name to Dodge List

@bot.command()
async def add(int_name : str):
    """Add name to dodge list"""
    pgDB.add_name(int_name)
    await bot.say('Added "%s" to the LoL dodge list' % (int_name))


@bot.command()
async def list():
    """Show the LoL dodge list"""
    await bot.say("Current Dodge List (AVOID THESE PEOPLE): ")
    summoners = pgDB.view_list()
    for row in range(len(summoners)):
        formatted = ''.join(map(str, (summoners[row])))
        await bot.say(formatted)

@bot.command()
async def remove(int_name : str):
    """Remove a name from the LoL dodge list"""
    await bot.say('Removing "%s" from the LoL dodge list' % (int_name))
    pgDB.remove_name(int_name)

# start the bot
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(config.token)
