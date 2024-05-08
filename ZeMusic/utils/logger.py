from pyrogram.enums import ParseMode

from ZeMusic import app
from ZeMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**💞 {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**🌹️ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐌𝐞 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 𝐍𝐚𝐌𝐞 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 𝐔𝐬𝐞𝐑𝐧𝐚𝐌𝐞 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝐈𝐃  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 𝐂𝐡𝐚𝐭 𝐥𝐢𝐧𝐤: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🌻 𝐒𝐞𝐀𝐫𝐜𝐇𝐞𝐝 𝐅𝐨𝐫:** {message.text}
**━━━━━━━━━━━━━━━**
**💐 𝐒𝐭𝐫𝐄𝐚𝐦 𝐓𝐲𝐏𝐞:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
