import os
import time
from cmd_cllaback import *
import logging
from pyrogram import *
import requests
from progress import progress
from conf import Config
from pyrogram import Client, filters, idle
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

   
OC_GoFiles_Files = Client(
    "GofileUploader",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@OC_GoFiles_Files.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@OC_GoFiles_Files.on_message(filters.private & filters.media & ~filters.sticker)
async def main(client, message):
    status = await message.reply("𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒊𝒏𝒈 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 𝑻𝒐 𝑴𝒚 𝑺𝒆𝒓𝒗𝒆𝒓...")
    now = time.time()
    file =await OC_GoFiles_Files.download_media(message,progress=progress,progress_args=("**𝚄𝚙𝚕𝚘𝚊𝚍 𝙿𝚛𝚘𝚐𝚛𝚎𝚜𝚜 𝚂𝚝𝚊𝚛𝚝𝚎𝚍, 𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝 !**\n**𝕀ᴛ𝕤 𝕋ᴀᴋᴇ ᴛɪᴍᴇ 𝔸ᴄᴄᴏʀᴅɪɴɢ 𝕐ᴏᴜʀ 𝔽ɪʟᴇ𝕤 𝕊ɪᴢᴇ** \n\n**ᴇᴛᴀ:** ", status,now))
    server = requests.get(url="https://api.gofile.io/getServer").json()["data"]["server"]
    upload = requests.post(url=f"https://{server}.gofile.io/uploadFile",files={"upload_file": open(file, "rb")}).json()
    link = upload["data"]["downloadPage"]
    name = upload["data"]["fileName"]
    directlink = upload["data"]["directLink"]

    await status.delete()
    os.remove(file)
    File_Button = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📥 Direct Download Link',url=directlink),
            InlineKeyboardButton('📜 Download Page', url=link),
            InlineKeyboardButton('🎁 Share Link', url="https://t.me/share/url?url="+directlink)
            ]]
        )

    output = f"""
<u>**🔅🎁🎁 ƑƖԼЄ ƲƤԼƠƛƊЄƊ ƬƠ ƓƠƑƖԼЄ 🎁🎁**</u>

**📂 Fɪʟᴇ Nᴀᴍᴇ:**

◇───────────────◇

 `{name}`

◇───────────────◇

**📦 Download Page:**

◇───────────────◇

 {link}

◇───────────────◇

**📥Direct Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ:** 

◇───────────────◇

{directlink}

◇───────────────◇


🌷 𝒟𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝓇 : ✍️✍️𝓞𝓹𝓮𝓷 𝓒𝓸𝓭𝓮 𝓓𝓮𝓿𝓼 ✍️✍️"""

    await message.reply(output,reply_markup=File_Button, disable_web_page_preview=True)



@OC_GoFiles_Files.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()


OC_GoFiles_Files.start()
print("""GoFileBot Is Started!
🌷 𝒟𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝓇 : ✍️✍️𝓞𝓹𝓮𝓷 𝓒𝓸𝓭𝓮 𝓓𝓮𝓿𝓼 ✍️✍️
Send me any media file, I will upload it to Gofile.io and give the download link
""")
idle()