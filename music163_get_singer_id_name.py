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
        'Cookie': 'NMTID=00OSPTGVpmPyM1JkUU2t79ewj5IZIQAAAGNRL-yMg; JSESSIONID-WYYY=rFVcDvhuEU0jenRAYwk9%5CiVurChZ3lOxosR0YFDwFFpn1JMQwEFPtN8p0YtUsvDJ0%2FDU2pYKsEBh9f0%2FHPBK6%5CD5lCbHmk9AN2aJrdnq%2BW8Oi7u42mCyw254DwAu2D%5CUoA1%2BhKOvN6sIXl2WjdCM8dUcUMsjvIswvMJ3omN3BRxyq3BQ%3A1706257229927; _iuqxldmzr_=32; _ntes_nnid=0ab55e017bee31abaec22d64eeaa2eeb,1706255429997; _ntes_nuid=0ab55e017bee31abaec22d64eeaa2eeb; WEVNSM=1.0.0; WNMCID=vebnbt.1706255430322.01.0; WM_NI=xbqaF8qC60YDsPHUgNAFzCm3WeGKa%2FoXDSlzdmgP01hF1BDkB1mj4Fi1aqbX%2BDhKmvxeXOeMDLYE%2FKFnYJ7CgucQjmRAwD4Nn4HDSicV5IgUHLXj1MNwQUh3hRk%2FYsdwbFY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9bbb70a38bbfaeeb489bbc8ab6c15e929b8fb1d533ab8eff8af43d90ecbdade22af0fea7c3b92abcbebf82c534b39dfad1dc50b19088b6e646839ab6a4f03995bb89ace425ad888cb4ef72a8b3a9b1b33bac9affa3c76182efa38bb74eabefaf92e154e99ca8acf07ebcbb98b0e847889497a6ae4186b297abb649a5abadb2e967929fb9a5b746aeec88a5d263a18afbaae65f8c94988bb4478ea99fb6eb39ac8ea5d0dc79a8a9aea7dc37e2a3; WM_TID=RaHsDN2C2XNFEFUQRBOF5mUw2qratsLM; ntes_utid=tid._.ApyA9iBmZeZBVwUQFALVpyBh37vfr3%252Ba._.0; __snaker__id=rni6czfXJYdI1wUd; sDeviceId=YD-lXfofKRiOW5ERhBVVVfRsl9SRVukeoVu; gdxidpyhxdE=5kTgKDVN50%5CSBB1EnnV%2Fo08kMfC%2B7o1Vm%2B43%5CVdMk%2F%2FQ1fJDp4rajbAiLUx0jWNyheynwJnRCsoBEbqDqpf4PBqxbUaao9eJUzczmbUxSC8Dz28pa%2F7HG%2B9cul7aILwn1kePIU10Rd3vfEYzUPKsN%2BzmVWMUrL6uYcYDK9DCnqGOxCwj%3A1706256335074; __csrf=66af9bb7b1e8c04c7169d0db74d800bf; MUSIC_U=00404325CB071454F795A81529715D5B5E0A4DF82DA5157B3B8F7402A4338BEF6A76E666C26DC66BEA9ACC727C7B1AA912D49FDA73129D6DF2484AD01842077B0E9E709CE14C2AFDC5194CCEFBD4197307FBE0397666B3F18EAD9C494B7733F62A8C39C0222FCBD89156966BEBD380D341AD0A63F54984C715A39EC76CB70AC12AFB002D4E623915299C2847620E0E6126C613607AC16F0CA0AC633D5F90BBD88591B2367EFD0A7D962CAAF63025A1CBB3EE2C5FA1185A24E714BDA05EB14352C9BC61D812D984583C39F92AFBC6F12C1FBF32B3E9F3F55A3ED657331E943CB99A9930E6B4E9C1CC16E4FA7BA9262C9A9F6BE89F90EA157CD5584662EE4A5B198009DA82F595FAA5BC83066A3697CB6A1D1AA17B4909EA9499512DA1B2968BE9B871ECCA84700CD9A6B06B225067AE9EACCD226EDE26BAB6CBB6897921B1DDECC27C8745FE368375D22AB273B2741CCF683BC6B1CB49606C61D8946F19706B1E78; ntes_kaola_ad=1'
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
        info = [(item.get('id'), item.get('name')) for item in songs]
    except Exception as e:
        print(e)
        info = None
    response.close()
    return info


if __name__ == '__main__':
    sing = '就是南方凯'
    page = 20
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
