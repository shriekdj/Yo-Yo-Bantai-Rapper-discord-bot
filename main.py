import discord
import os
import requests
import json
import random
from discord.ext import commands
from replit import db
from variables_and_gifs import *
from keep_alive import keep_alive

client = discord.Client()

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_words(encouraging_message):
    if "words" in db.keys():
        words = db["words"]
        words.append(encouraging_message)
        db["words"] = words
    else:
        db["words"] = [encouraging_message]


def delete_encouragement(index):
    words = db["words"]
    if len(words) > index:
        del words[index]
        db["words"] = words


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Streaming(platform="YOUTUBE",name="Sasta Biig Bosss | Parody | Ashish Chanchlani", url="https://www.youtube.com/watch?v=hWPopqZJJww"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content.lower()

    async def meme_reply(list_of_words,list_of_gif):
      if any(word in message.content.lower() for word in list_of_words):
        await message.channel.send(random.choice(list_of_gif))
        return
    

    if msg.startswith('carry inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith("carry welcome"):
        welcome = random.choice(welcomes_gifs)
        await message.channel.send(random.choice(welcomes_gifs))
        return
    

    if msg.startswith("carry new"):
        encouraging_message = msg.split("carry new ", 1)[1]
        update_words(encouraging_message)
        await message.channel.send("New carryminati message added.")
        return

    if msg.startswith("carry del"):
        words = []
        if "words" in db.keys():
            index = int(msg.split("carry del ", 1)[1])
            delete_encouragement(index)
            words = db["words"]
        await message.channel.send(words)
        return

    if msg.startswith("carry list"):
        words = []
        if "words" in db.keys():
            words = db["words"]
        await message.channel.send(words)
        return

    if msg.startswith("carry responding"):
        value = msg.split("carry responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")
        return

    if any(word in msg for word in flirt_words):
        await message.channel.send(random.choice(flirt_gifs))
        return
    

    if msg.startswith("natsu" or "natsu dragneel"):
        await message.channel.send(random.choice(natsu_gifs))
        return
    
    await meme_reply(flirt_words,flirt_gifs)

    await meme_reply(yo_words,yo_gifs)

    await meme_reply(huh_words,huh_gifs)

    await meme_reply(kuchbhi_words,kuchbhi_gifs)

    await meme_reply(gm_words,gm_gifs)

    await meme_reply(gn_words,gn_gifs)

    await meme_reply(bruh_words,bruh_gifs)

    await meme_reply(control_words,control_gifs)

    await meme_reply(takleef_words,takleef_gifs)

    await meme_reply(nikal_words,nikal_gifs)

    await meme_reply(nahi_words,nahi_gifs)

    if db["responding"]:
        options = starter_words
        if "words" in db.keys():
            options = options + db["words"]

#       if any(word in msg for word in carryminati_words):
#           await message.channel.send(random.choice(options))

keep_alive()
client.run(os.getenv("TOKEN"))

