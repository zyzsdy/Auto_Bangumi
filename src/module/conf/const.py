# -*- encoding: utf-8 -*-
import os
from ..config import DEFAULT_SETTINGS

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ENV_TO_ATTR = {
    "program": {
        "AB_INTERVAL_TIME": ("sleep_time", float),
        "AB_RENAME_FREQ": ("times", float),
        "AB_WEBUI_PORT": ("webui_port", int),
    },
    "downloader": {
        "AB_DOWNLOADER_HOST": "host",
        "AB_DOWNLOADER_USERNAME": "username",
        "AB_DOWNLOADER_PASSWORD": "password",
        "AB_DOWNLOAD_PATH": "path",
    },
    "rss_parser": {
        "AB_RSS_COLLECTOR": ("enable", lambda e: e.lower() in ("true", "1", "t")),
        "AB_RSS": "link",
        "AB_NOT_CONTAIN": ("filter", lambda e: e.split("|")),
        "AB_LANGUAGE": "language",
        "AB_ENABLE_TMDB": ("enable_tmdb", lambda e: e.lower() in ("true", "1", "t")),
    },
    "bangumi_manage": {
        "AB_RENAME": ("enable", lambda e: e.lower() in ("true", "1", "t")),
        "AB_METHOD": "method",
        "AB_GROUP_TAG": ("group_tag", lambda e: e.lower() in ("true", "1", "t")),
        "AB_EP_COMPLETE": ("eps_complete", lambda e: e.lower() in ("true", "1", "t")),
        "AB_REMOVE_BAD_BT": ("remove_bad_torrent", lambda e: e.lower() in ("true", "1", "t")),
    },
    "debug": {
        "AB_DEBUG_MODE": ("enable", lambda e: e.lower() in ("true", "1", "t")),
    },
    "proxy": {
        "AB_HTTP_PROXY": "http",
        "AB_SOCKS": "socks",
    },
}


class BCOLORS:
    @staticmethod
    def _(color: str, *args: str) -> str:
        strings = [str(s) for s in args]
        return f"{color}{', '.join(strings)}{BCOLORS.ENDC}"

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
