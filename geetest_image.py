from __future__ import division

try:
    import cPickle as pickle
except ImportError:
    import pickle
import PIL.Image as image

"""总结一下：最终的图片就是把拼图，
按照x=157、y=58、w=10、h=58截取出来，放在上半部分第一个位置
，x=145、y=58、w=10、h=58截取出来放在上半部分第二个位置，紧挨着第一个，以此类推，拼成一张整图。"""
a = [{'y': 80, 'x': 157}, {'y': 80, 'x': 145}, {'y': 80, 'x': 265}, {'y': 80, 'x': 277}, {'y': 80, 'x': 181},
     {'y': 80, 'x': 169}, {'y': 80, 'x': 241}, {'y': 80, 'x': 253}, {'y': 80, 'x': 109}, {'y': 80, 'x': 97},
     {'y': 80, 'x': 289}, {'y': 80, 'x': 301}, {'y': 80, 'x': 85}, {'y': 80, 'x': 73}, {'y': 80, 'x': 25},
     {'y': 80, 'x': 37}, {'y': 80, 'x': 13}, {'y': 80, 'x': 1}, {'y': 80, 'x': 121}, {'y': 80, 'x': 133},
     {'y': 80, 'x': 61}, {'y': 80, 'x': 49}, {'y': 80, 'x': 217}, {'y': 80, 'x': 229}, {'y': 80, 'x': 205},
     {'y': 80, 'x': 193},
     {'y': 0, 'x': 145}, {'y': 0, 'x': 157}, {'y': 0, 'x': 277}, {'y': 0, 'x': 265},
     {'y': 0, 'x': 169}, {'y': 0, 'x': 181}, {'y': 0, 'x': 253}, {'y': 0, 'x': 241}, {'y': 0, 'x': 97},
     {'y': 0, 'x': 109}, {'y': 0, 'x': 301}, {'y': 0, 'x': 289}, {'y': 0, 'x': 73}, {'y': 0, 'x': 85},
     {'y': 0, 'x': 37}, {'y': 0, 'x': 25}, {'y': 0, 'x': 1}, {'y': 0, 'x': 13}, {'y': 0, 'x': 133}, {'y': 0, 'x': 121},
     {'y': 0, 'x': 49}, {'y': 0, 'x': 61},
     {'y': 0, 'x': 229}, {'y': 0, 'x': 217}, {'y': 0, 'x': 193}, {'y': 0, 'x': 205}]


def get_merge_image(filename, location_list):
    im = image.open(filename)
    im_list_upper = []
    im_list_down = []

    for location in location_list:
        if location['y'] == 80:
            im_list_upper.append(im.crop((
                abs(location['x']), 80,
                abs(location['x']) + 10, 80 + 80)))
        if location['y'] == 0:
            im_list_down.append(im.crop((
                abs(location['x']), 0,
                abs(location['x']) + 10, 0 + 80)))

    # 画布
    new_im = image.new('RGB', (260, 160))

    # 上部分拼接
    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    # 下部分拼接
    x_offset = 0
    for im in im_list_down:
        new_im.paste(im, (x_offset, 80))  # 将im 粘贴到new_im 位置(x_offset,80)
        x_offset += im.size[0]

    return new_im


def is_similar(image1, image2, x, y):
    """
    image1 image2对比RGB 只要部分缺口处RGB值相差较大输出横坐标
    """
    pixel1 = image1.getpixel((x, y))
    pixel2 = image2.getpixel((x, y))
    # RGB 3个通道  只要有一个通道的值相差大于50就算是找到了缺口
    for i in range(3):
        if abs(pixel1[i] - pixel2[i]) >= 50:
            return True
    return False


def get_distance():
    # 合并图片使用
    new_image1 = get_merge_image(filename='full.webp', location_list=a)
    new_image2 = get_merge_image(filename='slice.webp', location_list=a)
    new_image1.save('image1.jpg')
    new_image2.save('image2.jpg')
    for i in range(260):
        for j in range(160):
            if is_similar(new_image1, new_image2, i, j):
                # 找到缺口  返回缺口的横坐标i
                return i - 5
