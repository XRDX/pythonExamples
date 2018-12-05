# usr/bin/python3
# pip3 install wxpy

from time import sleep
from wxpy import *

def welcome():
    print("\n-----------------------------------------------\n")
    print("欢迎使用微信群群发工具(by Vic)")
    print("注意：该工具和电脑端微信无法同时登陆")
    input("按Enter键开始登陆，如需切换账号，请删除wxpy.pkl文件")


def menu(bot):
    print("\n-----------------------------------------------\n")
    print("1. 创建群发列表(第一次使用必选)")
    print("2. 群发消息\n")
    print("0. 输出好友状况")
    print("q. 退出程序")

    choice = input("\n请输入你需要的操作: ")

    if choice == "0":
        print("\n-----------------------------------------------\n")
        print(bot.friends().stats_text())
    elif choice == "1":
        create_send_list(bot)
    elif choice == "2":
        send_msg_to_list(bot)
    else:
        exit()

def create_send_list(bot):
    print("\n-----------------------------------------------\n")

    file_name = input("你要保存的微信群列表文件(list.txt)：") or "list.txt"
    key_word = input("请输入微信群名称关键字，空则为所有会话：")


    chats = []
    print("一些不活跃的群可能无法被获取到，将群加入到通讯录中来激活")
    print("搜索到的微信群列表：\n")
    chats += bot.groups().search(key_word)

    with open(file_name, 'w', encoding='utf8') as f:
        for chat in chats:
            try:
                f.write(chat.name + '\n')
                print("\t" + chat.name)
            except:
                pass

    print("\n一共搜索到{}个符合条件的会话，请在{}中查看或者修改".format(len(chats), file_name))


def send_msg_to_list(bot):
    print("\n-----------------------------------------------\n")


    print("请输入你要发送的内容")
    print("由 前缀 和 内容 两个部分组成，若省略前缀，将作为纯文本消息发送")
    print("前缀 部分可为: ‘@fil@’, ‘@img@’, ‘@msg@’, ‘@vid@’ (不含引号)")
    print("分别表示: 文件，图片，纯文本，视频")
    print("内容 部分可为: 文件、图片、视频的路径，或纯文本的内容\n")
    content = input()

    print("你要发送的消息是：\n\n")
    print(content)
    print("\n-----------------------------------------------\n")

    if input("请确认 (y)/n:") == 'n':
        return

    file_name = input("微信群列表文件(list.txt)：") or "list.txt"

    print("确认要发送的会话有：\n")
    chats = []
    groups = bot.groups()
    with open(file_name, 'r', encoding='utf8') as f:
        for line in f:
            chat = ensure_one(groups.search(line))
            chats.append(chat)
            print(chat.name)

    if input("\n一共将发送到{}个群聊 (y)/n:".format(len(chats))) == 'n':
        return


    print("")
    succ = 0
    fail = 0
    for chat in chats:
        # 微信限制不能发送太快
        sleep(1)
        try:
            chat.send(content)
            print("成功发送给：{}".format(chat.name))
            succ += 1
        except:
            print("发送给{}失败！！！！！！".format(chat.name))
            fail += 1
            pass

    print("\n发送成功：{}个，发送失败{}个".format(succ, fail))

if __name__ == "__main__":
    welcome()
    bot = Bot(cache_path=True)
    while True:
        menu(bot)

