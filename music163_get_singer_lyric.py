# 2024/1/26 17:18
# 判断是否被采集过
import hashlib
import concurrent.futures

import redis

import music163_get_singer_id_name
import music163_lyric


def is_no_crawl(value):
    redis_client = redis.Redis()
    return redis_client.sadd('music163_lyric:filter', hashlib.md5(value.encode()).hexdigest())


def get_singer_lyric(singer, page):
    id_name_list = music163_get_singer_id_name.get_singer_id_name(singer, page)
    if not id_name_list:
        return None
    for id_name in id_name_list:
        # print(id_name)
        if is_no_crawl(str(id_name)):
            music163_lyric.get_lyric(*id_name)
        else:
            print(f'{id_name} 已经采集过了...')


if __name__ == '__main__':
    # 多线程
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as exe:
    #     for p in range(10):
    #         exe.submit(get_singer_lyric, '就是南方凯', p)

    # 单线程
    for p in range(10):
        get_singer_lyric('张杰', p)
