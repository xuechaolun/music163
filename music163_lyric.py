# 2024/1/22 21:59
import os.path

import requests
import execjs

import randomUA


def get_lyric(my_id, name):
    url = "https://music.163.com/weapi/song/lyric"

    # 字典转json字符串
    # x1 = {
    #     "id": my_id,
    #     "lv": -1,
    #     "tv": -1,
    #     "csrf_token": ""
    # }
    # x1 = json.dumps(x1)

    # 构建动态值
    x1 = '{"id":%s,"lv":-1,"tv":-1,"csrf_token":""}' % my_id
    x2 = '010001'
    x3 = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    x4 = '0CoJUm6Qyw8W8jud'
    jsc = execjs.compile(open('music163.js', 'r').read())
    ret = jsc.call('d', x1, x2, x3, x4)

    headers = {
        'User-Agent': randomUA.get_random_ua()
    }

    data = {
        "params": ret.get('encText'),
        "encSecKey": ret.get('encSecKey'),
    }
    response = requests.post(url, data=data, headers=headers)

    lyric = response.json().get('lrc').get('lyric')
    response.close()

    if lyric:
        print(f'{name} 的歌词采集到了...')
        if not os.path.exists('./lyric'):
            os.mkdir('lyric')
        # 防止歌名里有“/”，例如：张杰/张碧晨-只要平凡（钢琴曲）
        if '/' in name:
            name = name.replace('/', '-')
        name = name.strip()
        with open(f'./lyric/{name}.txt', 'w') as fw:
            fw.write(lyric)
    else:
        print(f'{name} 的歌词没有采集到...')


def save_lyric(lyric, filename, filepath):
    pass


if __name__ == '__main__':
    get_lyric('2061978961', '就是南方凯-离别开出花')
