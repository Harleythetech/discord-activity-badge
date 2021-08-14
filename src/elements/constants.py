"""
Copyright 2021 Janrey "CodexLink" Licas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from datetime import datetime
from enum import Enum, IntEnum, auto, unique
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from time import strftime
from typing import Any, Final, Optional, TypedDict
from aiohttp import BasicAuth

from discord import Intents
from discord.enums import Enum as DiscordEnum

from .typing import (
    BadgeElements,
    BadgeStructure,
    ColorHEX,
    HttpsURL,
    READMEContent,
    READMEIntegritySHA,
    RegExp,
)

# # Badge Generator Constants
BADGE_BASE_URL: Final[HttpsURL] = HttpsURL("https://badgen.net/badge/")
BADGE_REDIRECT_BASE_DOMAIN: Final[HttpsURL] = HttpsURL("https://github.com/")
BADGE_NO_COLOR_DEFAULT: Final[ColorHEX] = ColorHEX("#434343")
BADGE_ICON: Final[BadgeElements] = BadgeElements("discord")
BADGE_BASE_SUBJECT: Final[BadgeElements] = BadgeElements("Discord User")

BADGE_BASE_MARKDOWN: BadgeStructure = BadgeStructure(
    "[![{0}]({1})]({2})"
)  # [0] Represents the Generated Badge, [1] Represents Generate Badge URL, [3] Represents Any Redirect Link

BADGE_REGEX_STRUCT_IDENTIFIER: Final[RegExp] = RegExp(
    r"(?P<Delimiter>\[\!\[)(?P<badge_identifier>([a-zA-Z0-9_()-]+(\s|\b)){1,6})\]\((?P<badge_url>https://[a-z]+.[a-z]{2,4})/(?P<entrypoint>\w+)/(?P<subject_badge>[^...]+\b)/(?P<status_badge>[^?]+)\?(?P<params>[^)]+)\)\]\((?P<redirect_url>https://[a-z]+.[a-z]{2,4}/[^)]+)\)"
)

# # Base64 Actions and Related Classiications
@unique
class Base64Actions(IntEnum):
    DECODE_B64_TO_BUFFER = auto()
    ENCODE_BUFFER_TO_B64 = auto()


# # Classified Arguments Information
ARG_CONSTANTS: Final[dict[str, str]] = {
    "ENTRY_PARSER_PROG": "Discord Activity Fetcher and Badge Constructor (entrypoint.py)",
    "ENTRY_PARSER_DESC": "An application that runs under workflow container to evaluate User's Discord Activities to a Displayable Badge for their Special Repository's README.",
    "ENTRY_PARSER_EPILOG": "The use of arguments are intended for debugging purposes and development only. Please be careful and be vigilant about the requirements to make certain arguments functioning.",
    "HELP_DESC_NO_ALERT_LOCAL_USR": "Disables the Client Bot to send messages through PM whenever there's an error occured inside of Discord Client API Handler Class and WebSocket.",
    "HELP_DESC_DONT_COMMIT": "Runs the whole script without commiting and pushing some changes to README.md.",
    "HELP_DESC_GENERATE_LOG_FILE": "Enables logging to file. (File is viewable when running-on-local).",
    "HELP_DESC_DONT_LOG_TO_CONSOLE": "Disables printing log output to the console. (This is effective when running-on-local)",
    "HELP_DESC_RUNNING_LOCALLY": "Allows the script from running locally by loading .env instead of automatic invokation of values in Github Runner. This can raise or terminate the script if '.env' cannot be found.",
    "HELP_DESC_LOGGER_LEVEL": "Sets the logger level coverage that the logger object can display.",
    "HELP_DESC_VERBOSITY": "Sets the module coverage that the logger object can output, the top module will cover most of the modules that requires logging.",
}

# # Discord Client Intents
DISCORD_CLIENT_INTENTS: Intents = Intents.none()
DISCORD_CLIENT_INTENTS.guilds = True
DISCORD_CLIENT_INTENTS.members = True
DISCORD_CLIENT_INTENTS.presences = True


# # Discord User Client Dictionary Structure
class DISCORD_USER_STRUCT(TypedDict):
    id: int
    name: str
    discriminator: str  # I don't know why it was declared as `str` when its a 4-digit which should be `int`.
    statuses: dict[str, DiscordEnum]
    activities: dict[str, Any]  # To many elements to cover, let it be Any.


BLUEPRINT_INIT_VALUES: DISCORD_USER_STRUCT = {
    "id": 0,
    "name": "",
    "discriminator": "",
    "statuses": {},
    "activities": {},
}


# # Enumerations
@unique
class ContextOnSubject(IntEnum):
    CONTEXT_DISABLED: int = auto()
    DETAILS: int = auto()
    STATE: int = auto()


class ExitReturnCodes(IntEnum):
    EXIT_HELP: Final[int] = 0
    ENV_KEY_DOES_NOT_EXISTS_ON_DICT: Final[int] = 1
    ENV_KEY_DOES_NOT_EXISTS_ON_MACHINE: Final[int] = 1
    EXCEPTION_EXIT: Final[int] = 1
    ILLEGAL_CONDITION_EXIT: Final[int] = 1
    ILLEGAL_IMPORT_EXIT: Final[int] = 1
    NO_CONDITION_IMPLEMENTED_EXIT: Final[int] = 1
    RATE_LIMITED_EXIT: Final[int] = 1


@unique
class GithubRunnerActions(IntEnum):
    FETCH_README: int = auto()
    COMMIT_CHANGES: int = auto()


@unique
class GithubRunnerLevelMessages(Enum):
    WARNING: Final[str] = "warning"
    ERROR: Final[str] = "error"


@unique
class LoggerLevelCoverage(IntEnum):
    DEBUG: Final[int] = DEBUG
    INFO: Final[int] = INFO
    WARNING: Final[int] = WARNING
    ERROR: Final[int] = ERROR
    CRITICAL: Final[int] = CRITICAL


@unique
class LoggerRootLevel(Enum):
    SCRIPT_LEVEL: Final[str] = "__main__"
    SCRIPT_PLUS_DISCORD: Final[str] = "discord"
    LOOP_LEVEL: Final[str] = "asyncio"


@unique
class PreferredActivityDisplay(IntEnum):
    CUSTOM_ACTIVITY: int = auto()
    GAME_ACTIVITY: int = auto()
    RICH_PRESENCE: int = auto()
    STREAM_ACTIVITY: int = auto()
    SPOTIFY_ACTIVITY: int = auto()


@unique
class PreferredTimeDisplay(IntEnum):
    TIME_DISABLED: int = auto()
    HOURS: int = auto()
    HOURS_MINUTES: int = auto()
    MINUTES: int = auto()
    SECONDS: int = auto()


# # HTTPS Request Header Dictionary Structure
class REQUEST_HEADER(TypedDict):
    headers: dict[str, str]
    auth: BasicAuth


class COMMIT_REQUEST_PAYLOAD(TypedDict):
    content: Optional[READMEContent]
    message: Optional[str]
    sha: Optional[READMEIntegritySHA]
    committer: Optional[dict[str, str]]


# # Logger Constants
ROOT_LOCATION: Final[str] = "../"
ENV_FILENAME: Final[str] = ".env"
LOGGER_FILENAME: Final[str] = strftime("%m%d%Y-%H%M-") + "discord-activity-badge.log"
LOGGER_OUTPUT_FORMAT: Final[
    str
] = "[%(relativeCreated)dms, %(levelname)s] at %(module)s.py:%(lineno)d -> %(message)s"


# # Map Structure
# * This replicates actions.yml but with better handling for invalid values and replacing them (if invalid) with fallback_value to avoid pedantic errors.
ENV_STRUCT_CONSTRAINTS: Final[  # * If you have been referred to action.yml, this is the right place.
    dict[str, Any]
] = {
    # # Github Actions Environmental Variables
    "GITHUB_API_URL": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": True,
    },
    "GITHUB_ACTOR": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": True,
    },
    # # Required Parameters
    "INPUT_BADGE_IDENTIFIER_NAME": {
        "expected_type": str,
        "fallback_value": "(Script) Discord Activity Badge",
        "is_required": False,
    },
    "INPUT_COMMIT_MESSAGE": {
        "expected_type": str,
        "fallback_value": "Discord Activity Badge has been Updated!",
        "is_required": False,
    },
    "INPUT_DISCORD_BOT_TOKEN": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": True,
    },
    "INPUT_DISCORD_USER_ID": {
        "expected_type": int,
        "fallback_value": None,
        "is_required": True,
    },
    "INPUT_PROFILE_REPOSITORY": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": False,
    },
    "INPUT_URL_TO_REDIRECT_ON_CLICK": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": False,
    },
    "INPUT_WORKFLOW_TOKEN": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": True,
    },
    # # Optional Parameters — Colors and Intentions.
    "INPUT_CUSTOM_ACTIVITY_STRING": {
        "expected_type": str,
        "fallback_value": "",
        "is_required": False,
    },
    "INPUT_GAME_ACTIVITY_STRING": {
        "expected_type": str,
        "fallback_value": "Playing Game",
        "is_required": False,
    },
    "INPUT_RICH_PRESENCE_STRING": {
        "expected_type": str,
        "fallback_value": "Currently Playing",
        "is_required": False,
    },
    "INPUT_STREAM_ACTIVITY_STRING": {
        "expected_type": str,
        "fallback_value": "Currently Streaming",
        "is_required": False,
    },
    "INPUT_SPOTIFY_ACTIVITY_STRING": {
        "expected_type": str,
        "fallback_value": "Listening to",
        "is_required": False,
    },
    "INPUT_ONLINE_STATUS_STRING": {
        "expected_type": str,
        "fallback_value": "Online",
        "is_required": False,
    },
    "INPUT_IDLE_STATUS_STRING": {
        "expected_type": str,
        "fallback_value": "Idle",
        "is_required": False,
    },
    "INPUT_DND_STATUS_STRING": {
        "expected_type": str,
        "fallback_value": "Do-Not-Disturb",
        "is_required": False,
    },
    "INPUT_OFFLINE_STATUS_STRING": {
        "expected_type": str,
        "fallback_value": "Offline",
        "is_required": False,
    },
    "INPUT_CUSTOM_ACTIVITY_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#c70094",
        "is_required": False,
    },
    "INPUT_GAME_ACTIVITY_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#00cd90",
        "is_required": False,
    },
    "INPUT_RICH_PRESENCE_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#df1473",
        "is_required": False,
    },
    "INPUT_STREAM_ACTIVITY_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#4d14df",
        "is_required": False,
    },
    "INPUT_SPOTIFY_ACTIVITY_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#1db954",
        "is_required": False,
    },
    "INPUT_ONLINE_STATUS_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#61d800",
        "is_required": False,
    },
    "INPUT_IDLE_STATUS_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#edca00",
        "is_required": False,
    },
    "INPUT_DND_STATUS_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#fc4409",
        "is_required": False,
    },
    "INPUT_OFFLINE_STATUS_COLOR": {
        "expected_type": ColorHEX,
        "fallback_value": "#545454",
        "is_required": False,
    },
    "INPUT_STATIC_SUBJECT_STRING": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": False,
    },
    # # Optional Parameters — Context
    "INPUT_TIME_DISPLAY_SHORTHAND": {
        "expected_type": bool,
        "fallback_value": False,
        "is_required": False,
    },
    "INPUT_PREFERRED_PRESENCE_CONTEXT": {
        "expected_type": ContextOnSubject,
        "fallback_value": ContextOnSubject.DETAILS,
        "is_required": False,
    },
    "INPUT_TIME_DISPLAY_OUTPUT": {
        "expected_type": PreferredTimeDisplay,
        "fallback_value": PreferredTimeDisplay.HOURS_MINUTES,
        "is_required": False,
    },
    "INPUT_TIME_DISPLAY_ELAPSED_OVERRIDE_STRING": {
        "expected_type": str,
        "fallback_value": "elapsed.",
        "is_required": False,
    },
    "INPUT_TIME_DISPLAY_REMAINING_OVERRIDE_STRING": {
        "expected_type": str,
        "fallback_value": "remaining.",
        "is_required": False,
    },
    # # Optional Parameters — Preferences
    "INPUT_PREFERRED_ACTIVITY_TO_DISPLAY": {
        "expected_type": PreferredActivityDisplay,
        "fallback_value": PreferredActivityDisplay.RICH_PRESENCE,
        "is_required": False,
    },
    "INPUT_SHIFT_STATUS_ACTIVITY_COLORS": {
        "expected_type": bool,
        "fallback_value": False,
        "is_required": False,
    },
    "INPUT_SPOTIFY_INCLUDE_ALBUM_PLAYLIST_NAME": {
        "expected_type": bool,
        "fallback_value": False,
        "is_required": False,
    },
    "INPUT_STATUS_CONTEXT_SEPERATOR": {
        "expected_type": str,
        "fallback_value": None,
        "is_required": False,
    },
    # # Development Parameters
    "INPUT_IS_DRY_RUN": {
        "expected_type": bool,
        "fallback_value": False,
        "is_required": False,
    },
}

# # Time Constants
TIME_STRINGS: list[str] = ["hours", "minutes", "seconds"]
