from .get_response import nyaa_id, sukebei_id
from NyaaTorrrentBot import NYAA, botname
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

INVALID_TEXT = """ 
No ID found! Any Eroor Report At @CapitalLondonRadio
"""

@NYAA.on_message(filters.command(["magnet", f"magnet@{botname}"], prefixes = "/") & ~filters.edited)
async def get_magnet(client, message):
    query = message.text.split(maxsplit = 2)
    if len(query) < 2 or len(query) > 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return

    buttons = [
                    InlineKeyboardButton("Nyaa", f"nyaa {query[-1]}"),
                ]
    await NYAA.send_message(chat_id = message.chat.id, text = "Where do you wanna search?", reply_markup = InlineKeyboardMarkup(buttons))
