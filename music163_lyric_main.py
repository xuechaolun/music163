# 2024/1/23 13:20
import hashlib
import random
import time

import redis

import music163_get_id_name
import music163_lyric


# 判断是否被采集过
def is_no_crawl(value):
    redis_client = redis.Redis()
    return redis_client.sadd('music163_lyric:filter', hashlib.md5(value.encode()).hexdigest())


def run():
    for index, id_name in enumerate(music163_get_id_name.get_id_name()):
        if is_no_crawl(str(id_name)):
            print(f'正在采集第{index+1}个 {id_name[1]} 的歌词,id:{id_name[0]}')
            music163_lyric.get_lyric(*id_name)
            time.sleep(random.uniform(0.5, 1.0))
        else:
            print(f'{id_name} 已经采集过了...')


if __name__ == '__main__':
    start = time.time()
    run()
    print(f'耗时:{time.time()-start:.2f}s')
