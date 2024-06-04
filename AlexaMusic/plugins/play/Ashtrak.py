from pyrogram import Client, filters
from pyrogram.types import Message, ChatType, InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
import config

CHANNEL_LINK في config
if not hasattr(config, 'CHANNEL_LINK'):
    raise AttributeError("config module does not have 'CHANNEL_LINK' attribute")

channel = config.CHANNEL_LINK
Nem = config.BOT_NAME + " شغل"

async def subscription(_, __: Client, message: Message):
    if message.from_user is not None:
        user_id = message.from_user.id
        try:
            await app.get_chat_member(channel, user_id)
        except Exception as e:
            print(e)
            return False
    return True

subscribed = filters.create(subscription)

# تعريف دالة لمعالجة الأوامر
@app.on_message(filters.command(["تشغيل", "شغل", Nem], "") & ~subscribed)
async def command_handler(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        user_id = message.from_user.id
        user = message.from_user.first_name
        markup = Markup([
            [Button(config.CHANNEL_NAME, url=f"https://t.me/{channel}")]
        ])
        await message.reply(
            f"◇ عذرًا عزيزي {user} ، عليك الاشتراك في قناة البوت أولاً.",
            reply_markup=markup
        )
