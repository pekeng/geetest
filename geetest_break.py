# -*- coding:utf-8 -*-
"""
geetest6.0.9
slide 7.4.3
"""
import random
import math
import rsa
import binascii
import execjs
import json
from geetest_request import parse_res
from geetest_performing import performanceing1



# 计算每次间隔   相当于c函数6531
def fun_c(a):
    g = []
    e = []
    f = 0
    for h in range(len(a) - 1):
        b = int(round(a[h + 1][0] - a[h][0]))
        c = int(round(a[h + 1][1] - a[h][1]))
        d = int(round(a[h + 1][2] - a[h][2]))
        g.append([b, c, d])

        if b == c == d == 0:
            pass
        else:
            if b == 0 and c == 0:
                f += d
            else:
                e.append([b, c, d + f])
                f = 0
    if f != 0:
        e.append([b, c, f])
    return e


# 6498 join函数用到
def q9e(item):
    b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]]
    c = 'stuvwxyz~'
    for i, t in enumerate(b):
        if t == item[:2]:
            return c[i]
    return 0


# 6572  join函数用到
def j9E(a):
    b = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
    c = len(b)
    d = ''
    e = abs(a)
    f = int(e / c)
    if f >= c:
        f = c - 1
    if f > 0:
        d = b[f]
    e %= c
    g = ''
    if a < 0:
        g += '!'
    if d:
        g += '$'
    return g + d + b[e]


def join(track_list):
    skip_list = fun_c(track_list)
    g, h, i = [], [], []
    for j in range(len(skip_list)):
        b = q9e(skip_list[j])
        if b:
            h.append(b)
        else:
            g.append(j9E(skip_list[j][0]))
            h.append(j9E(skip_list[j][1]))
        i.append(j9E(skip_list[j][2]))
    return ''.join(g) + '!!' + ''.join(h) + '!!' + ''.join(i)


# 9224
def h8(ll, change):
    Y3 = []
    n4 = 0
    G3 = change[32:]
    for i in range(len(G3)):
        O3 = ord(str(G3[n4]))
        if O3 > 57:
            Y3.append(O3 - 87)
        else:
            Y3.append(O3 - 48)
        n4 += 1

    G3 = 36 * Y3[0] + Y3[1]
    L3 = math.ceil(ll) + G3
    R4 = [[], [], [], [], []]
    Z3 = {}
    u4 = 0
    n4 = 0  # 重置n4
    for y in range(len(change[:32])):
        W3 = change[:32][n4]
        if W3 in Z3:
            pass
        else:
            Z3[W3] = 1
            R4[u4].append(W3)
            u4 += 1
            if u4 == 5:
                u4 = 0
            else:
                u4 = u4
        n4 += 1

    k3 = L3
    N4 = 4
    c3 = ''
    z3 = [1, 2, 5, 10, 50]
    while k3 > 0:
        if k3 - z3[N4] >= 0:
            f3 = int(random.random() * len(R4[N4]))
            c3 += R4[N4][f3]
            k3 -= z3[N4]
        else:
            del (R4[N4])
            del (z3[N4])
            N4 -= 1
    return c3


# 6772 6786
def Vd_my():
    b = int((65536 * (1 + random.random())))
    a = hex(b).replace('0x', '')[1:]
    message = a + a + a + a
    message = message.encode()
    return message


# 6135
def rsa_my():
    param_1 = "10001"
    # 公钥
    param_2 = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
    message = Vd_my()
    modulus = int(param_2, 16)
    exponent = int(param_1, 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message, rsa_pubkey)
    data = binascii.b2a_hex(crypto).decode()
    return data, message


# 4421  i8加密函数的js
def get_js():
    f = open("i8.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# data=gt+change(顺序不能反)MD5加密
def Ii8(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('I8', data))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# e1P
def get_js2():
    f = open("my_e2.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# rsa
def get_js3():
    f = open("rsa.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# e1P
def parse2(I1P, Vd):
    jsstr = get_js2()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('eee', I1P, Vd))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# h8
def parse3_h8(ll, change):
    jsstr = get_js2()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('xxx', ll, change))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def breaken():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host': 'api.geetest.com',
        'Referer': 'https://www.vipkid.com.cn/login',
    }
    track_list1, gt, new_challenge, distance, session = parse_res()
    if track_list1:
        print(gt, new_challenge, distance)
        aa = join(track_list=track_list1)
        ep = {
            "v": "7.4.3",
            "f": Ii8(data=gt + new_challenge),  # data=gt+change 用I8函数MD5加密
            "te": "false",  # 不能加引号
            "me": "true",  # 不能加引号
            "tm": performanceing1,  # 浏览器表现池得出
        }
        I1P = {
            "lang": "zh-cn",
            "userresponse": parse3_h8(ll=distance, change=new_challenge),  # 距离l,change 用h8函数加密
            "passtime": track_list1[-1][-1],  # 轨迹的最后参数
            "imgload": random.randint(300, 400),  # 图片加载时间
            "aa": aa,  # (join函数)轨迹池来模拟得出 正确！
            "ep": ep,  # 上面给出是字典形式
            "rp": Ii8(data=gt + new_challenge[:32] + str(track_list1[-1][-1]))  # 用Ii8函数MD5加密
        }  # I1P的形式一定是'{"lang":"zh-cn",}' 不然加密不同
        I1P1 = json.dumps(I1P).replace('"false"', 'false').replace('"true"', 'true')
        print("I1P1已经生成:{}".format(I1P1))
        K1P, message = rsa_my()                     # RSA加密   # message是都一样的
        message = message.decode()
        e1P = parse2(I1P=I1P1, Vd=message)             # AES加密
        print('e1P已经生成:{}'.format(e1P))
        print('K1P已经生成:{}'.format(K1P))

        w = e1P + K1P
        print('w已经生成:{}'.format(w))
        success_url = "https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&pt=0&w={}".format(
            gt, new_challenge, w)
        print("success_url成功生成:{}".format(success_url))
        success_res = session.get(url=success_url, headers=headers, verify=False)
        print(success_res.text)
    else:
        print("轨迹没匹配到")


if __name__ == '__main__':
    breaken()
    # parse3_rsa(message="fdc36534f4215f2f")
