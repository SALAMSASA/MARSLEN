import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message, InlineKeyboardButton
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AlexaMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from AlexaMusic.core.call import Alexa
from AlexaMusic.utils import seconds_to_min, time_to_seconds
from AlexaMusic.utils.channelplay import get_channeplayCB
from AlexaMusic.utils.database import is_video_allowed
from AlexaMusic.utils.decorators.language import languageCB
from AlexaMusic.utils.decorators.play import PlayWrapper
from AlexaMusic.utils.formatters import formats
from AlexaMusic.utils.inline.play import (
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from AlexaMusic.utils.inline.playlist import botplaylist_markup
from AlexaMusic.utils.logger import play_logs
from AlexaMusic.utils.stream.stream import stream
from config import BANNED_USERS, lyrical, CHANNEL_SUDO, YAFA_NAME, YAFA_CHANNEL
from strings import get_command
from AlexaMusic.utils.database import is_served_user

# تعيين المنطقة الزمنية إلى بغداد
tz = pytz.timezone('Asia/Baghdad')

chat = []

@app.on_message(filters.text & ~filters.private, group = 20)
async def azaan(c, msg):
    if msg.text == "تفعيل الاذان":
        if msg.chat.id in chat:
            return await msg.reply_text("- الاذان مفعل من قبل")
        else:
            chat.append(msg.chat.id)
            return await msg.reply_text("تم تفعيل الاذان ♥️🌿")
    elif msg.text == "تعطيل الاذان":
        if msg.chat.id in chat:
            chat.remove(msg.chat.id)
            return await msg.reply_text("تم تعطيل الاذان ♥️🌿")
        else:
            return await msg.reply_text("- الاذان معطل من قبل")
      
async def kill():
    for i in chat:
        await Alexa.force_stop_stream(i)

async def play(i):
    assistant = await group_assistant(Alexa, i)
    file_path = "./assets/azan.m4a"
    stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
    try:
        await assistant.join_group_call(
            i,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        try:
            await Alexa.join_assistant(i, i)
        except Exception as e:
            await app.send_message(i, f"{e}")
    except TelegramServerError:
        await app.send_message(i, "في خطأ في سيرفرات التليجرام")
    except AlreadyJoinedError:
        await kill()
        try:
            await assistant.join_group_call(
                i,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except Exception as e:
            await app.send_message(i, f"{e}")

def prayer_time():
    try:
        prayer = requests.get(f"http://api.aladhan.com/timingsByAddress?address=Baghdad&method=4&school=0")
        prayer = prayer.json()
        fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
        dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
        asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
        maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
        isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')

        if datetime.now(tz).strftime('%I:%M %p') == fajr:
            return "الفجر"
        elif datetime.now(tz).strftime('%I:%M %p') == dhuhr:
            return "الظهر"
        elif datetime.now(tz).strftime('%I:%M %p') == asr:
            return "العصر"
        elif datetime.now(tz).strftime('%I:%M %p') == maghrib:
            return "المغرب"
        elif datetime.now(tz).strftime('%I:%M %p') == isha:
            return "العشاء"
    except Exception as e:
        asyncio.sleep(5)
        print(e)

async def azkar():
    while not await asyncio.sleep(2):
        prayer = prayer_time()
        if prayer:
            await kill()
            for i in chat:
                await app.send_message(i, f"حان الآن وقت أذان {prayer} بتوقيت بغداد 🥰♥️")
                await play(i)
            await asyncio.sleep(174)
            await kill()
