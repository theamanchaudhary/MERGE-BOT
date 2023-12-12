import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", '84d8b635a127218158581c0fd8225770')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '6937730640:AAGj_euD3MUED6tH6C4qv5Auyx-ja67pVCE')
    TELEGRAM_API = os.environ["TELEGRAM_API", '28271319']
    OWNER = os.environ.get("OWNER", '5674333293')
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", 'theamanchaudhary')
    PASSWORD = os.environ.get("PASSWORD", 'AmanBotz')
    DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://theamanchaudhary:updatesbyaman@cluster0.dnol3vs.mongodb.net/?retryWrites=true&w=majority')
    LOGCHANNEL = os.environ.get("LOGCHANNEL", '-1001910513374')  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
