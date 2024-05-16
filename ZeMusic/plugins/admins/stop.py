from pyrogram import Client, filters
from ZeMusic.utils.decorators.admins import admin_check

app = Client("my_bot")

# Assuming BANNED_USERS is a set or list of user IDs who are banned
BANNED_USERS = set()

def command(commands):
    return filters.command(commands, prefixes=["/", "!", "."])

async def stop_music(client, message):
    # Assuming you have a player instance or method to stop the music
    player = get_music_player_instance()  # استبدل هذا بالكود الفعلي للحصول على مشغل الموسيقى
    if player is not None:
        player.stop()  # استبدل هذا بالطريقة الفعلية لإيقاف الموسيقى
        await message.reply_text("تم إيقاف الموسيقى.")
    else:
        await message.reply_text("لم يتم العثور على مشغل الموسيقى.")

def get_music_player_instance():
    # Replace with actual code to get the music player instance
    # Example: return music_player_instance
    return None  # استبدل هذا بالكود الفعلي للحصول على مشغل الموسيقى

@app.on_message(command(["انهاء", "ايقاف"]) & filters.group & ~filters.user(BANNED_USERS) & filters.create(admin_check))
async def handle_stop_command(client, message):
    await stop_music(client, message)

if name == "main":
    app.run()
