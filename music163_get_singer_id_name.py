# 2024/1/26 15:21
import json
import os.path
import random
import time

import execjs
import requests

import randomUA


def get_singer_id_name(singer='就是南方凯', offset=0):
    url = 'https://music.163.com/weapi/cloudsearch/get/web'
    params = {
        'csrf_token': ''
    }
    headers = {
        'Referer': 'https://music.163.com/search/',
        'User-Agent': randomUA.get_random_ua(),
        'Cookie': ''
    }
    # 构建动态值
    x1 = {
        "hlpretag": "<span class=\"s-fc7\">",
        "hlposttag": "</span>",
        "id": "5781",
        "s": singer,
        "type": "1",
        "offset": str(offset * 30),
        "total": "false",
        "limit": "30",
        "csrf_token": params.get('csrf_token')
    }
    x1 = json.dumps(x1)
    x2 = '010001'
    x3 = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    x4 = '0CoJUm6Qyw8W8jud'
    jsc = execjs.compile(open('music163.js', 'r').read())
    ret = jsc.call('d', x1, x2, x3, x4)
    # print(ret)

    from_data = {
        'params': ret.get("encText"),
        'encSecKey': ret.get("encSecKey")
    }
    response = requests.post(url, data=from_data, params=params, headers=headers)
    print(response)
    try:
        songs = response.json().get('result').get('songs')
        info = [(item.get('id'), item.get('name').strip()) for item in songs]
    except Exception as e:
        print(e)
        info = None
    response.close()
    return info


if __name__ == '__main__':
    sing = '许嵩'
    page = 10
    if not os.path.exists('./singer'):
        os.mkdir('./singer')

    id_name_list = list()
    for i in range(page):
        print(f'正在获取第{i + 1}页...')
        ret = get_singer_id_name(sing, i)
        if not ret:
            break
        id_name_list.extend(ret)
        time.sleep(random.uniform(0.5, 1.0))
    id_name_list = list(set(id_name_list))

    fw = open(f'./singer/{sing}.txt', 'w', encoding='utf-8')
    for id_name in id_name_list:
        # print(id_name)
        fw.write(f'{id_name}\n')
    fw.close()
