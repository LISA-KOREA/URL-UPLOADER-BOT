from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """Hello {},

I Am Telegram URL Uploader Bot.

<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b>

<b>/help for more details...</b>"""

    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b> 👉 Create own Clone Bot Check Source /about</b>"
    FORMAT_SELECTION = "Set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\n\nYou can use /deletethumbnail to delete the auto-generated thumbnail\n"
    SET_CUSTOM_USERNAME_PASSWORD = """<b>👮‍♂ Powered By :</b> @LISA_FAN_LK"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    #DOWNLOAD_FILE = "📥 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶"
    DOWNLOAD_START = "📥 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶"
    UPLOAD_START = "📤 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDe tected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = " OWNER : Lisa 💕\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = """𝘛𝘏𝘈𝘕𝘒𝘚 𝘍𝘖𝘙 𝘜𝘚𝘐𝘕𝘎 𝘔𝘌 🥰\n\n@NT_BOT_CHANNEL"""
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✅"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Delete Thumbnail ✅"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Delete Thumbnail ✅"
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTube</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_ABOUT_DETAILS = """<b>🔘 My Name :</b> URL Uploader Bot

<b>🔘 Source :</b> <a href="https://github.com/LISA-KOREA/URL-UPLOADER-BOT">Click</a>

<b>🔘 Language :</b> <a href="https://www.python.org/">Python 3.10.5</a>

<b>🔘 Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 1.4.16</a>

<b>🔘 Creater :</b> @LISA_FAN_LK"""

    HELP_USER = """𒊹︎︎︎ HOW TO UPLOAD FILE OR MEDIA
    
➪ SEND YOUR LINK FOR UPLOAD FILE OR MEDIA.

𒊹︎︎︎ HOW TO SET THUMBNAIL

➪ SEND YOUR THUMBNAIL PHOTO AND <b>ADDED ONCE TIME ONLY.</b>

𒊹︎︎︎ HOW TO DELETING THUMBNAIL

➪ SEND /deletethumbnail TO DELETE YOUR THUMBNAIL.

𒊹︎︎︎ COMMENTS

/help - how to use this bot 

/upgrade - view offers

/info - check your info 

/about - something about me 

/deletethumbnail - delete your thumbnail"""

    INFO_TEXT = """
🌸 First Name : <b>{}</b>

🌸 Second Name : <b>{}</b>

🌸 Username : <b>@{}</b>

🌸 Id : <code>{}</code>

🌸 Profile : <b>{}</b>

🌸 Dc : <b>{}</b>

🌸 Language : <b>{}</b>

🌸 Status : <b>{}</b>
"""
     #START_BUTTONS = InlineKeyboardMarkup(
       #  [[
       #  InlineKeyboardButton('HELP', callback_data='help')
       #  InlineKeyboardButton('ABOUT', callback_data='about')
       #  ],[
      #   InlineKeyboardButton('CLOSE', callback_data='close')
        # ]]
  #  )
  # BUTTONS = InlineKeyboardMarkup( soon

    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @NT_BOT_ADMIN"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    MSG_TO_DOC_OR_LINK_FOR_RARX_SRT = "Msg to a Telegram media (MKV), to extract embedded streams"
    MSG_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Msg /set_thumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /plan to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Free users only 1 request per 2 minutes."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    
