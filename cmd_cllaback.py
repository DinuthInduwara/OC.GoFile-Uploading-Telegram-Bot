from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

START_TEXT = """
<b>Hey There,
I can upload any media files to __gofile.io__


🌷 𝒟𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝓇 : ✍️✍️𝓞𝓹𝓮𝓷 𝓒𝓸𝓭𝓮 𝓓𝓮𝓿𝓼 ✍️✍️


Hit 'How To Use' button to find out more about how to use me</b>
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('How To Use', callback_data='help'),
        InlineKeyboardButton('Repo', url='https://github.com/DinuthInduwara/OC.GoFile-Uploading-Telegram-Bot'),
        InlineKeyboardButton('Github', url='https://github.com/DinuthInduwara/')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Repo', url='https://github.com/DinuthInduwara/OC.GoFile-Uploading-Telegram-Bot'),
        InlineKeyboardButton('Github', url='https://github.com/DinuthInduwara/')
        ]]
    )
HELP_TEXT = """
GoFile Help!

🌷 𝒟𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝓇 : ✍️✍️𝓞𝓹𝓮𝓷 𝓒𝓸𝓭𝓮 𝓓𝓮𝓿𝓼 ✍️✍️

Send me any file, I will upload it to gofile.io and give the download link
"""


