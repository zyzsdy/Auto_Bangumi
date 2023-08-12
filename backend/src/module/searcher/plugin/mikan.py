import re


def mikan_url(keywords: list[str]):
    keyword = "+".join(keywords)
    search_str = re.sub(r"[\W_ ]", "+", keyword)
    url = f"https://mikanani.me/RSS/Search?searchstr={search_str}"
    return url
