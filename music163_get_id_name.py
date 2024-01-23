# 2024/1/23 13:12
import re

import requests
import randomUA


# 默认为热歌榜的id
def get_id_name(params_id="3778678"):
    headers = {
        "referer": "https://music.163.com/",
        "user-agent": randomUA.get_random_ua()
    }
    url = "https://music.163.com/discover/toplist"
    params = {
        "id": params_id
    }
    response = requests.get(url, headers=headers, params=params)
    ret = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a></li>', response.text, re.S)
    response.close()

    return ret


if __name__ == '__main__':
    get_id_name()
