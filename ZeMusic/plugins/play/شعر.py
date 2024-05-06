import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
import random
    

@app.on_message(command([f"شعر", "شعر🎸", "ش", "{BOT_USERNAME} شعر"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/saresnx/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الشعر لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )


@app.on_message(command([f"قصيده", "قصيده🎸", "ق", "{BOT_USERNAME} قصيده"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,96)
    url = f"https://t.me/QasedFaeder/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار قصيده اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )
