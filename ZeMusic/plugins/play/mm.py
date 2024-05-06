from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZeMusic import app
import config

Muntazer =config.CHANNEL_LINK
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not Muntazer:
        return
    try:
        try:
            await app.get_chat_member(Muntazer, msg.from_user.id)
        except UserNotParticipant:
            if Muntazer.isalpha():
                link = "https://t.me/" + Muntazer
            else:
                chat_info = await app.get_chat(Muntazer)
                link = chat_info.invite_link
            try:
                await msg.reply
                  await message.reply_text(
    f'❤️‍🩹┇عزيزي: {message.from_user.mention}\n🫀┇أشتࢪك في قناة البوت أولاً.\n🚧┇قناة البوت: @L_Q7I 🫂',
    reply_markup=force_btn,
    disable_web_page_preview=False
)
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup
                        [InlineKeyboardButton(config.CHANNEL_NAME, url=f"https://t.me/L_Q7I")]
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {Muntazer}!")
