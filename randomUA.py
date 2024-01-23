# 2024/1/10 19:36
import random


def get_random_ua():
    platform = ['(Windows NT 10.0; Win64; x64)', '(Windows NT 6.1; WOW64)', '(Windows NT 6.0; Win64; x64)',
                '(Windows NT 6.1; WOW64; rv:54.0)', '(Windows NT 6.1; Win64; x64)',
                '(Macintosh; Intel Mac OS X 10_12_5)', '(Linux; Android 13; SM-G981B)']
    webkit = ['AppleWebKit/537.36 (KHTML, like Gecko)', 'Gecko/20100101']
    browser = ['Chrome/58.0.3029.110 Safari/537.36', 'Firefox/54.0', 'Version/10.1.1 Safari/603.2.4',
               'Version/9.1.2 Safari/601.7.7']

    return f'Mozilla/5.0 {random.choice(platform)} {random.choice(webkit)} {random.choice(browser)}'


if __name__ == '__main__':
    print(get_random_ua())
    