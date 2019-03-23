"""
    WeChat Auto Admire V0.0.1
"""

# -*- coding:utf-8 -*- 

import itchat, re
from itchat.content import *
import random
from super_admire import admire_sentence

@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    # group_name的值修改成你要夸的weixin群名
    group_name = '修改成你的群名';
    if msg['User']['NickName'] == group_name:
        print('Message from: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)

        match = re.search('夸我', msg['Text']) or re.search('求夸', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('夸我 is: %s' % (match is not None))
            random_idx = random.randint(0, len(admire_sentence.sentences['夸我']) - 1)
            itchat.send('@' + '%s\n%s' % (username, admire_sentence.sentences['夸我'][random_idx]), msg['FromUserName'])

        # print('isAt is:%s' % msg['isAt'])

        elif msg['isAt']:
            random_idx = random.randint(0, len(admire_sentence.sentences['default']) - 1)
            itchat.send('@' + '%s\n%s' % (username, admire_sentence.sentences['default'][random_idx]), msg['FromUserName'])
            print('-+-+'*5)
        else:
            random_idx = random.randint(0, len(admire_sentence.sentences['default']) - 1)
            itchat.send('@' + '%s\n%s' % (username, admire_sentence.sentences['default'][random_idx]), msg['FromUserName'])
            print('-+-+'*5)

# Windows系统，enableCmdQR=True
# itchat.auto_login(enableCmdQR=True, hotReload=True)
# Mac、Linux，enableCmdQR=2
itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()

