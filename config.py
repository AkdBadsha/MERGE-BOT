import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6546362014:AAEx6SI0veYCMKHjH5HrgXCcb2X8VTNgiyM")
    TELEGRAM_API = os.environ["TELEGRAM_API", "21748181"]
    OWNER = os.environ.get("OWNER", "1980321098")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "kingBadsha3232")
    PASSWORD = os.environ.get("PASSWORD", "OK")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://moviepro:pass@cluster0.jw98t9a.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001718789952")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
