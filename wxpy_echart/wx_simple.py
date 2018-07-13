#-*- coding: utf-8 -*-
import os
from wxpy import *


def remove_txt_file(path):
    ''' 写入txt文本 '''
    if os.path.exists(path):
        os.remove(path)
        
def write_txt_file(path, txt):
    ''' 写入txt文本 '''
    with open(path, 'a', encoding='utf8') as f:
        f.write(txt)

def read_txt_file(path):
    ''' 读取txt文本 '''
    with open(path, 'r', encoding='utf8') as f:
        return f.read()

def login():
    # 初始化机器人，扫码登陆
    bot = Bot()

    # 获取所有好友
    my_friends = bot.friends()

    write_txt_file('data.js', 'var name = "')
    write_txt_file('data.js', str(bot.self.name))
    write_txt_file('data.js', '";\n') 

    return my_friends

def show_sex_ratio(friends):
    # 使用一个字典统计好友男性和女性的数量
    sex_dict = {'male': 0, 'female': 0, 'other':0}

    for friend in friends:
        # 统计性别
        if friend.sex == 1:
            sex_dict['male'] += 1
        elif friend.sex == 2:
            sex_dict['female'] += 1
        else:
            sex_dict['other'] += 1

    # 为了方便数据的呈现，生成JSON Array格式数据
    data = []
    for key, value in sex_dict.items():
        data.append({'name': key, 'value': value})
        
    write_txt_file('data.js', 'var sex_data = ')
    write_txt_file('data.js', str(data))
    write_txt_file('data.js', ';\n')
    print(sex_dict)

def show_area_distribution(friends):
    # 使用一个字典统计各省好友数量
    province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
        '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
        '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
        '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
        '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
        '四川': 0, '贵州': 0, '云南': 0,
        '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
        '香港': 0, '澳门': 0, '其他': 0}

    # 统计省份
    for friend in friends:
        if friend.province in province_dict.keys():
            province_dict[friend.province] += 1
        else:
            province_dict['其他'] += 1

    # 为了方便数据的呈现，生成JSON Array格式数据
    data = []
    for key, value in province_dict.items():
        data.append({'name': key, 'value': value})

    write_txt_file('data.js', "var provice_data = ")
    write_txt_file('data.js', str(data))
    write_txt_file('data.js', ';') 
    print(data)


if __name__ == '__main__':
    remove_txt_file('data.js')
    friends = login()
    show_sex_ratio(friends)
    show_area_distribution(friends)
