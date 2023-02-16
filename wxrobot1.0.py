from PyOfficeRobot.core.WeChatType import*
import time
import random

wx=WeChat()
wx.GetSessionList()
#a=input("请输入接收人")#can be delete
who='民大附中初一学生群（总群）'
#who=a#can be delete
msg='testmsg'
wx.ChatWith(who)
for i in range(2):
    wx.SendMsg(msg)
msg1='此人工智能为Halpha-wxrobot-1.0ser,请输入 /help 来进行下一步操作'
wx.SendMsg(msg1)
while True:
    glm=wx.GetLastMessage[1]
    print(glm)
    if glm=='/help':
        msg2='请输入命令[系统主动询问时请在5秒内回答][/call:向Halpha主机里的某个人发送消息,/rand:随机一个0-1024的数,/repeat:重复某条消息[禁止输入/repeat,否则会停机]]'
        wx.SendMsg(msg2)
    glm1=wx.GetLastMessage[1]
    if glm1=='/call':
        msg3='请输入对象'
        wx.SendMsg(msg3)
        time.sleep(20)
        glm2=wx.GetLastMessage[1]
        if glm2=='请输入对象':
            break
        who1=glm2
        msg4='请输入内容'
        wx.SendMsg(msg4)
        time.sleep(20)
        glm3=wx.GetLastMessage[1]
        if glm3=='请输入内容':
            break
        wx.ChatWith(who1)
        msg5=glm3
        wx.SendMsg(msg5)
        wx.ChatWith(who)
        wx.SendMsg(msg='over')
    if glm1=='/rand':
        msg6=chr(random.randint(0,1024))
        wx.SendMsg(msg6)
    if glm1=='/repeat':
        msg7='请输入内容'
        wx.SendMsg(msg7)
        time.sleep(20)
        glm4=wx.GetLastMessage[1]
        if glm4=='repeat':
            break
        msg8=glm4
        wx.SendMsg(msg8)
