from pyrogram import Client, filters

# Assuming BANNED_USERS is a set or list of user IDs who are banned
BANNED_USERS = set()

def command(commands):
    return filters.command(commands, prefixes=["/", "!", "."])

async def stop_music(client, message):
    # Assuming you have a player instance or method to stop the music
    player = get_music_player_instance()  
    if player is not None:
        player.stop()  
        await message.reply_text("تم إيقاف الموسيقى.")
    else:
        await message.reply_text("لم يتم العثور على مشغل الموسيقى.")

def get_music_player_instance():
    # Replace with actual code to get the music player instance
    return None  

app = Client("my_bot")

@app.on_message(
    command(["انهاء", "ايقاف"]) &
    filters.group &
    ~filters.user(BANNED_USERS)
)
async def handle_stop_command(client, message):
    # Assuming admin_check is defined somewhere else
    if admin_check(message):
        await stop_music(client, message)
    else:
        await message.reply_text("ليس لديك صلاحيات لإيقاف الموسيقى.")

def admin_check(message):
    # Define your admin check logic here
    return True  # or False based on your logic

def main():
    app.run()

if name == "main":
    main()
