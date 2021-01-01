# bot.py
import os
import random

import twitchio
from twitchio.ext import commands

from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


@bot.command(name='rolldice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='roastme')
async def roast_initiated(ctx):

    name = ctx.author.name

    roasts = [
        f'It’s nice to see such a diverse crowd here today. We’ve got Indians, Jews, Whites, and whatever the fuck {name} is.',
        f'{name} you\'re looking pretty rough this evening. You look like if sweatpants were a person.',
        f'{name} you\'re my favorite person besides every other person I\'ve ever met.',
        f'{name} I envy people who have never met you.',
        f'{name} if you were an inanimate object, you’d be a participation trophy.',
        f'{name} you are a pizza burn on the roof of the world\'s mouth.',
        f'{name} if genius skips a generation, your children will be brilliant.',
        f'{name} you have the charm and charisma of a burning orphanage.',
        f'{name} if there was a single intelligent thought in your head it would have died from loneliness.',
        f'{name} I want you to be the pallbearer at my funeral so you can let me down one last time.',
        f'{name} you are the human embodiment of an eight-dollar haircut.',
        f'{name} you\'re so inbred you\'re a sandwich.',
        f'{name} if I had a gun, with two bullets, and I was in a room with Hitler, Bin Laden and you, I would shoot you twice.'
    ]

    response = random.choice(roasts)
    await ctx.channel.send(response)


if __name__ == "__main__":
    bot.run()
