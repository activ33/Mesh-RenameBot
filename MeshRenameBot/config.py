from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://ankit29:ankit29@cluster0.7gdbq.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "ff8451462d91861a13ffd8a6bb72aa8b"]
        API_ID = [int, 1464463]
        BOT_TOKEN = [str, "6561330005:AAE2Cw0mXmdc_RJtMEyVkF5akWBuRfDbJR0"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 30]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[689061386]]
        OWNER_ID = [int,689061386]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"animefiles"]
        FORCEJOIN_ID = [int,-1202033572]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
