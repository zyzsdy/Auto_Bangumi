VERSION_PREFIX = "2.6.0"
VERSION_SUFFIX = "KoaMod.1"

DEFAULT_SETTINGS = {
    "program": {
        "sleep_time": 7200,
        "times": 20,
        "webui_port": 37144,
        "data_version": 4.0
    },
    "downloader": {
        "type": "qbittorrent",
        "host": "127.0.0.1:37145",
        "username": "admin",
        "password": "adminadmin",
        "path": "D:\\tmp\\tmpdownload",
        "ssl": False
    },
    "rss_parser": {
        "enable": True,
        "type": "mikan",
        "link": "",
        "enable_tmdb": True,
        "filter": ["720", "\\d+-\\d+"],
        "language": "zh"
    },
    "bangumi_manage": {
        "enable": True,
        "eps_complete": False,
        "rename_method": "pn",
        "group_tag": False,
        "remove_bad_torrent": False
    },
    "debug": {
        "enable": False,
        "level": "info",
        "file": "bangumi.log",
        "dev_debug": False
    },
    "proxy": {
        "enable": False,
        "type": "http",
        "host": "127.0.0.1",
        "port": 7890,
        "username": "",
        "password": ""
    },
    "notification": {
        "enable": False,
        "type": "telegram",
        "token": "",
        "chat_id": ""
    }
}