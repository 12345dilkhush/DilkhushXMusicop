import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv(","14408588"))
API_HASH = getenv(","e4e340ca8f1c6a1c2c302d5d34cbfe72)

BOT_TOKEN = getenv("5416582457:AAG_3d4u0XZakf_f-0z9Goukd9j-QiDw8Gs")

MONGO_DB_URI = getenv(","mongodb+srv://Dilwar:<password>@cluster0.ugj3r.mongodb.net/?retryWrites=true&w=majority",)

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "90")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001682834821"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐃𝐢𝐥𝐤𝐡𝐮𝐬𝐡 𝐗 𝐌𝐮𝐬𝐢𝐜")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5350202392").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DilwarBot/ZaraXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv(","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")

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/The_Friendship_Haveli")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/The_Friendship_Haveli")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f690021836689035f37ed.jpg")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID","617d8e2d79b64ad3ad88546538f56ee7)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET","5b82b666eb4c3351b23339b82700d89a)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "7")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", BQBTAu_9fpTrhdAXUX4u_MwVpIMgtSKJGCta3YSdjljbq155y3S0kQgNFEFscjXzZs7YWEcPxTW_q2z0Zx8FigwzY_vONIWObwcy-L90hF6mR-fWYo2aBTLUokCvMGBTr-pNZUjXH9hfE3_f0WEfo8oG6ShzIh2t9xRK8y8nc1PPRdqR4bf7baJ0hf0evUChTMmq30YF9nCkH1bgyeugnK6x1D9zrgwhLi4wQB2Mn01whWg1OLRjF8EixnE3OwVfZ5t1OIo-x_I4oUE5acWmyBgEVmPQbyBoLgKyHiRPCYi0jYrkO2K-ct7m2Z_6NjZWlusVBtVAnehFOvNJDRhkBfRVAAAAAS47opkA)
STRING2 = getenv("STRING_SESSION2",BQBTAu_9fpTrhdAXUX4u_MwVpIMgtSKJGCta3YSdjljbq155y3S0kQgNFEFscjXzZs7YWEcPxTW_q2z0Zx8FigwzY_vONIWObwcy-L90hF6mR-fWYo2aBTLUokCvMGBTr-pNZUjXH9hfE3_f0WEfo8oG6ShzIh2t9xRK8y8nc1PPRdqR4bf7baJ0hf0evUChTMmq30YF9nCkH1bgyeugnK6x1D9zrgwhLi4wQB2Mn01whWg1OLRjF8EixnE3OwVfZ5t1OIo-x_I4oUE5acWmyBgEVmPQbyBoLgKyHiRPCYi0jYrkO2K-ct7m2Z_6NjZWlusVBtVAnehFOvNJDRhkBfRVAAAAAS47opkA)
STRING3 = getenv("STRING_SESSION3",BQBTAu_9fpTrhdAXUX4u_MwVpIMgtSKJGCta3YSdjljbq155y3S0kQgNFEFscjXzZs7YWEcPxTW_q2z0Zx8FigwzY_vONIWObwcy-L90hF6mR-fWYo2aBTLUokCvMGBTr-pNZUjXH9hfE3_f0WEfo8oG6ShzIh2t9xRK8y8nc1PPRdqR4bf7baJ0hf0evUChTMmq30YF9nCkH1bgyeugnK6x1D9zrgwhLi4wQB2Mn01whWg1OLRjF8EixnE3OwVfZ5t1OIo-x_I4oUE5acWmyBgEVmPQbyBoLgKyHiRPCYi0jYrkO2K-ct7m2Z_6NjZWlusVBtVAnehFOvNJDRhkBfRVAAAAAS47opkA)
STRING4 = getenv("STRING_SESSION4",BQBTAu_9fpTrhdAXUX4u_MwVpIMgtSKJGCta3YSdjljbq155y3S0kQgNFEFscjXzZs7YWEcPxTW_q2z0Zx8FigwzY_vONIWObwcy-L90hF6mR-fWYo2aBTLUokCvMGBTr-pNZUjXH9hfE3_f0WEfo8oG6ShzIh2t9xRK8y8nc1PPRdqR4bf7baJ0hf0evUChTMmq30YF9nCkH1bgyeugnK6x1D9zrgwhLi4wQB2Mn01whWg1OLRjF8EixnE3OwVfZ5t1OIo-x_I4oUE5acWmyBgEVmPQbyBoLgKyHiRPCYi0jYrkO2K-ct7m2Z_6NjZWlusVBtVAnehFOvNJDRhkBfRVAAAAAS47opkA)
STRING5 = getenv("STRING_SESSION5",BQBTAu_9fpTrhdAXUX4u_MwVpIMgtSKJGCta3YSdjljbq155y3S0kQgNFEFscjXzZs7YWEcPxTW_q2z0Zx8FigwzY_vONIWObwcy-L90hF6mR-fWYo2aBTLUokCvMGBTr-pNZUjXH9hfE3_f0WEfo8oG6ShzIh2t9xRK8y8nc1PPRdqR4bf7baJ0hf0evUChTMmq30YF9nCkH1bgyeugnK6x1D9zrgwhLi4wQB2Mn01whWg1OLRjF8EixnE3OwVfZ5t1OIo-x_I4oUE5acWmyBgEVmPQbyBoLgKyHiRPCYi0jYrkO2K-ct7m2Z_6NjZWlusVBtVAnehFOvNJDRhkBfRVAAAAAS47opkA)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "aaruxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph//file/d122a125988c66faa1393.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph//file/d122a125988c66faa1393.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[KYA RE LAVDE] - BOHOT FONT LAGANE KA SHAUKH HAI. JAA PHIR BANNA KO APNI CHUMT DEKE AA"
    )
