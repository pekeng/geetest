import random
import execjs
import rsa
import binascii
import requests
import re
import time
from geetest_image import get_distance
from geetest_source_track import source_track


# fullpage
def get_js3():
    f = open("fullpage.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# fullpage
def fullpages():
    jsstr = get_js3()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('ddd'))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# 6772 6786
def Vd_my():
    b = int((65536 * (1 + random.random())))
    a = hex(b).replace('0x', '')[1:]
    message = a + a + a + a
    message = message.encode()
    return message


# 6135
def rsa_my(message):
    param_1 = "10001"
    # 公钥
    param_2 = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
    modulus = int(param_2, 16)
    exponent = int(param_1, 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message, rsa_pubkey)
    data = binascii.b2a_hex(crypto).decode()
    return data


# Q0o
def get_js():
    f = open("my_e2.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# Q0o
def parse(I1P, Vd):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('eee', I1P, Vd))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def parse_res():
    session = requests.session()
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host': 'www.vipkid.com.cn',
        'Referer': 'https://www.vipkid.com.cn/login',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
    res = session.post(
        url='https://www.vipkid.com.cn/rest/ucaccount/account/verifycode/login/sms'
        , data={'mobile': '15934117585',
                'type': '1',
                'appId': '10001',
                'domain': 'www.vipkid.com.cn'
                }, headers=headers, verify=False)
    gt = res.headers.get('vk-gt')
    challenge = res.headers.get('vk-gt-challenge')
    i = fullpages()
    print(gt)
    print(challenge)
    print(res.text)
    print(res.headers)
    headers.update({'Host': 'api.geetest.com'})
    res2 = session.get(
        url='https://api.geetest.com/gettype.php?gt={}'.format(gt),
        headers=headers, verify=False)
    print("第二个请求：{}".format(res2.text))
    print("第二个请求headers：{}".format(res2.headers))

    param1 = '''{"gt":"%s", "challenge": "%s", "offline": false, "new_captcha": false, "product": "bind", "width": "280px","protocol": "https://", "static_servers": ["static.geetest.com/", "dn-staticdown.qbox.me/"],"fullpage": "/static/js/fullpage.8.6.1.js", "pencil": "/static/js/pencil.1.0.1.js","aspect_radio": {"voice": 128, "pencil": 128, "click": 128, "beeline": 50, "slide": 103},"geetest": "/static/js/geetest.6.0.9.js", "type": "fullpage", "click": "/static/js/click.2.6.3.js","voice": "/static/js/voice.1.1.4.js", "slide": "/static/js/slide.7.4.1.js","beeline": "/static/js/beeline.1.0.1.js", "cc": 4, "ww": true, "i": "%s"}''' % (
        gt, challenge, i)
    print(param1)
    message = Vd_my()
    print(message)
    t0o = rsa_my(message)
    message = message.decode()
    Q0o = parse(I1P=param1, Vd=message)
    print(t0o)
    print(Q0o)
    w = Q0o + t0o
    print("生成的w值为{}".format(w))
    res3 = session.get(
        url='https://api.geetest.com/get.php?gt={}&challenge={}&lang=zh-cn&pt=0'.format(
            gt, challenge),
        headers=headers, verify=False)
    print("第三个请求url为:::{}".format(res3.url))
    print("第三个请求{}".format(res3.text))
    print("第三个请求headers为:::{}".format(res3.headers))
    print("第三个请求cookies为:::{}".format(session.cookies))
    res4 = session.get(
        url='https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&pt=0'.format(
            gt, challenge),
        headers=headers, verify=False)

    print("第4个请求url为:::{}".format(res4.url))
    print("第4个请求{}".format(res4.text))
    print("第4个请求headers为:::{}".format(res4.headers))
    print("第4个请求cookies为:::{}".format(session.cookies))
    res5 = session.get(
        url='https://api.geetest.com/get.php?is_next=true&type=slide3&gt={}&challenge={}&lang=zh-cn&https=false&protocol=https%3A%2F%2F&offline=false&product=embed&api_server=api.geetest.com&width=100%25&callback=geetest_{}'.format(
            gt, challenge, int(time.time() * 1000)),
        headers=headers, verify=False)

    print("第5个请求url为:::{}".format(res5.url))
    print("第5个请求text:{}".format(res5.text))
    print("第5个请求headers为:::{}".format(res5.headers))
    print("第5个请求cookies为:::{}".format(session.cookies))
    full1 = re.findall(re.compile(r'"fullbg": "(.*?)",'), str(res5.text))
    slice1 = re.findall(re.compile(r'"bg": "(.*?)",'), str(res5.text))
    new_challenge = re.findall(re.compile(r'"challenge": "(.*?)",'), str(res5.text))

    if full1 and slice1 and new_challenge:
        full1 = full1[0]
        slice1 = slice1[0]
        new_challenge = new_challenge[0]
        print("得到新的new_challenge:{}".format(new_challenge))
        print("得到新的new_gt:{}".format(gt))
        full_picture_url = "https://static.geetest.com/" + full1
        slice_picture_url = "https://static.geetest.com/" + slice1
        print("full_picture_url图片地址{}".format(full_picture_url))
        print("slice_picture_url图片地址{}".format(slice_picture_url))
        headers.update({'Host': 'static.geetest.com'})
        response_image1 = session.get(url=full_picture_url, headers=headers, verify=False)
        response_image2 = session.get(url=slice_picture_url, headers=headers, verify=False)
        with open('full.webp', 'wb') as f:
            f.write(response_image1.content)
            print('full.webp生成成功')
        with open('slice.webp', 'wb') as f:
            f.write(response_image2.content)
            print('slice.webp生成成功')
        distance = get_distance()
        print('距离成功生成：{}'.format(distance))
        # 从轨迹池挑选轨迹
        track_list1 = ''
        print(source_track)
        for track_list in source_track:
            if distance in track_list[-1] or distance + 1 in track_list[-1] or distance - 1 in track_list[-1]:
                print("成功取到轨迹{}".format(track_list))
                track_list1 = track_list
        if track_list1:
            # 从破解文件得到w
            return track_list1, gt, new_challenge, distance, session
        else:
            track_list1 = ''
            gt = ''
            new_challenge = ''
            distance = ''
            session = ''
        return track_list1, gt, new_challenge, distance, session
