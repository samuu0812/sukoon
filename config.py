import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22451487
API_HASH = "9e7ac680cfc997528edae9676dc4baec"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7994707404:AAFhZsAdV1z25QNEutEovVIAyyYqJ40bKiU"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Samu22:Samu22@samu.t8pvy.mongodb.net/?retryWrites=true&w=majority&appName=Samu"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002082859243

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7251325591

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/uff_yeh_saadgi"
SUPPORT_GROUP = "https://t.me/+OjnPm05ViugyZTQ1"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFWlR8AcL_hof2Q5gAUgPpBfTxEfeYBF9_dZiS-LZZx1FgiJDF4BFZhglyieQXWY9MGQgC6fJUhtJF2ac7aXv3CobGNqytSHnTHo1hB16nhzYscLt0Ny3b7j2Cu2Z7Lb4XmP00i_CLwxYQJn8CyR_7AT4LuxFgcK2GKPSHIuQp708CIwkPmMMV_G_VERFXfbQspsHOMywn0zz5UiOCpa8_F3mDVrXBmGWWCocMykhbmW2wzUpcnBZiAb7aVgLbFqDp3d9xd8QBI64JRQg20BahyuNYqT8ZhzzZdWgw_HaELoSni0t3he77vxvUTwyNL2-q9wfTyavF3FvAbAkRDRK1e5u0VygAAAAHPSoU5AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/ebe2b949f94efbf31d52a-3dbe5d3c4161af275c.jpg"

PING_IMG_URL = "https://graph.org/file/f614236b0fab1bc3d8bb4-72ae2d2c2874b54141.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/7d7524315db26ec0c7573-a5e721926f6c0fd968.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/7d7524315db26ec0c7573-a5e721926f6c0fd968.jpg"
STREAM_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9319823596978a90d09ff-c4c1688598d62e378a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
