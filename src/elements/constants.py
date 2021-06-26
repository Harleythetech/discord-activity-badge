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

# Classifications of constants of any kind. (limiters, choices, etc.) | constants.py
# Version dev.0.06232021


from typing import final


if __name__ == "__main__":
    from .exceptions import IsolatedExecNotAllowed
    raise IsolatedExecNotAllowed

else:
    from datetime import timedelta as timeConstraint
    from typing import Final, List

    # This is an intentional implementation, I just prefer to keep long strings to another file.
    # And let short constants intact so that the context is not out of blue.

    # # Classified Arguments Information
    ARG_CONSTANTS : Final[dict[str, str]] = { # Cannot evaluate less.
        "ENTRY_PARSER_DESC": "An application that runs under workflow to evaluate User's Discord Activity Presence to Displayable Badge for their README.md.",
        "ENTRY_PARSER_EPILOG": "The use of arguments are intended for debugging purposes only. Please be careful.",
        "HELP_DESC_NO_LOGGING":  "Disables logging but does not surpress outputting logs to console, if enabled.",
        "HELP_DESC_DRY_RUN": "Runs the whole script without commiting changes to external involved factors (ie. README.md)",
        "HELP_DESC_NO_ALERT_USR": "Does not alert the user / developer from the possible crashes through Direct Messages (this also invokes the do-not-send logs.)",
        "HELP_DESC_LOG_TO_CONSOLE": "Prints the log output to the console, whenever the case."
        }

    # # Class Container Metadata
    ARG_PLAIN_CONTAINER_NAME : Final[str] = "ArgsContainer"
    ARG_PLAIN_DOC_INFO : Final[str] = "This is a plain class to where the args has been living after being evaluated."

    # # Discord Client Bot Message Context
    # To be done later.

    # # Logger Information

    LOGGER_LOG_LOCATION : Final[str] = "../../"
    LOGGER_FILENAME: Final[str] = "idk.log" # todo: lmao, do something about this. Let's try automation later.
    LOGGER_OUTPUT_FORMAT: Final[str] = "" # todo: this one as well.

    # VALID_ARGS_PROPERTIES : Final[List[str]] = ["disable_logs", "no_alert", "", ""] # # Classified Arguments to Container

    # # Pre-Condition Constraints
    ALLOWABLE_TIME_TO_COMMIT: Final = timeConstraint(minutes=30) # todo: Clarify this. This is connected from the workflow recommended refresh rate. Also rate-limits.