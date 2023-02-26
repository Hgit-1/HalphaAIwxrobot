'''
tips:WARNING, THIS IS A CHINESE PROGRAM! It may not friendly for peoples from countries expect China.
tips:this code is an open source code.
--------------------------------EULA--------------------------------

ENG:
----------------DOCUMENTS BEGIN----------------
this is a python program for chat in wechat.
if you use this, we will think that you had agreed the EULA.
1:install:
    if you see this, you must be installed this program.
    input "pip install pyofficerobot" and "pip install openai" in 'cmd'[you must have a python enviroment under 3.10]
    and you can try it!
2:must/should change something:
    if you see this, you must be seen this program.
    change the line which has been noticed 'can be change' by your self
    MUST CHANGE THE LINE WHICH HAS BEEN NOTICED 'must be change'!
    you can delete the line which has been noticed 'can be delete'
    [you must know my school and my grade :)]
3:use:
    maybe you want to use this. now I want to introduce that.
    1:/call:
        /call is a special command. you can use it with your good friends.[DO NOT USE IT WHEN YOU FACED TO SOME STRANGER!!!]
        you can just use it follow the instruction.
    2:/rand:
        /rand can rand something between 0 to 32768, and we char it.
    3:/repeat:
        /repeat can repeat something, just follow the instruction.
    4:/record:
        /record can record something, just follow the instruction.
    5:/chatgpt:
        /chatgpt can connect you to chatgpt[MUST CHANGE API!]
    6:something has been put in the trashbin but saved here:
        like /chat1,/chat2. You shall not to touch them.
use it!
----------------DOCUMENTS END----------------
CHN:
----------------开始文档----------------
这是一个用于在微信中聊天的Python程序。
如果您使用此程序，我们将认为您已同意下面的协议。
1：安装：
    如果您看到这个，您想必已经安装了这个程序。
    在'cmd'中输入“pip install pyofficerobot”和“pip install openai”[您必须有一个Python环境在3.10以下]，然后您可以尝试使用它！
2：必须/应该更改的内容：
    如果您看到这个，您想必已经看到了这个程序。
    您必须自己更改已经被标记为“can be change”的行
    必须更改已经被标记为“must be change”的行！
    您可以删除已被标记为“can be delete”的行
    [您想必知道我的学校和年级 :)]
3：使用：
    也许您想使用这个程序。现在我想介绍一下。
1：/call：
    /call是一个特殊的命令。您可以与您的好朋友一起使用。[当您面对一些陌生人时，不要使用它！]
    您只需按照指示使用即可。
2：/rand：
    /rand可以随机生成0到32768之间的char化的数字，并将其发送到微信中。
3：/repeat：
    /repeat可以重复某些内容，只需按照指示使用即可。
4：/record：
    /record可以记录某些内容，只需按照指示使用即可。
5：/chatgpt：
    /chatgpt可以将您连接到chatgpt[必须更改API！]
6：有些东西已经被放入垃圾桶但在这里保存：
    如/chat1，/chat2。您不应该触碰它们。
使用它吧！
----------------结束文档----------------
'''
from PyOfficeRobot.core.WeChatType import*
import time
import random
import openai
wx=WeChat()
wx.GetSessionList()
a=input("请输入接收人")#can be delete
who='民大附中初一学生群（总群）'#can be change
who=a#can be delete
msg='testmsg'
wx.ChatWith(who)
for i in range(2):
    wx.SendMsg(msg)
msg1='此人工智能为Halpha-wxrobot-1.0ser,请输入 /help 来进行下一步操作'
while True:
    glm=wx.GetLastMessage[1]
    print(glm)
    if glm=='/help':
        msg2='请输入命令[系统主动询问时请在20秒内回答][/call:向Halpha主机里的某个人发送消息,/rand:随机一个未知的东西,/repeat:重复某条消息[禁止输入/repeat,否则会停机],/record:记录消息,/chat1:正在训练中的稳定聊天模型[已废弃],/chat2:不稳定人工智能模型[test][已废弃],/chatgpt:connect->chatgpt][如要@我，请先写"@Halpha",等到"请输入信息"被发送时再留言[20sec内回答]]'#can be change
        wx.SendMsg(msg2)
    glm1=wx.GetLastMessage[1]
    if glm1=='/call':
        msg3='请输入对象'
        wx.SendMsg(msg3)
        time.sleep(20)
        glm2=wx.GetLastMessage[1]
        if glm2=='请输入对象':
            wx.SendMsg(msg='timeout')
            break
        who1=glm2
        msg4='请输入内容'
        wx.SendMsg(msg4)
        time.sleep(20)
        glm3=wx.GetLastMessage[1]
        if glm3=='请输入内容':
            wx.SendMsg(msg='timeout')
            break
        wx.ChatWith(who1)
        msg5=glm3
        wx.SendMsg(msg5)
        wx.ChatWith(who)
        wx.SendMsg(msg='over')
    if glm1=='/rand':
        msg6=chr(random.randint(0,32767))
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
    if glm1=='/record':
        wx.SendMsg(msg='Start to record......[输入/stoprecord以停止收录]')
        x=wx.GetLastMessage[1]
        time.sleep(3)
        if x=='/stoprecord':
            wx.SendMsg(msg='record over')
            break
        with open('record-self.txt', 'a') as f:
            f.write(x)
            if x=='/stoprecord':
                f.close()
                wx.SendMsg(msg='record over')
    if glm1=='@Halpha' or glm1=='@Halpha扰民人工智障[v1.0]别改群名':#can be change
        wx.SendMsg(msg='请输入信息')
        time.sleep(20)
        y=wx.GetLastMessage[1]
        if y=='请输入信息':
            wx.SendMsg(msg='timeout')
        with open('record-spe-call.txt', 'a') as g:
            g.write(y)
            g.close()
            wx.SendMsg(msg='over')
    glm_ans='blank'#define
    if glm1=='/chat1':#can be change
        while 1:
            glm_ans=wx.GetLastMessage[1]
            wx.SendMsg('WARNING:此模块已废弃[5sec]')
            time.sleep(5)
            if glm_ans=='hi':
                wx.SendMsg(msg='hello')
            if glm_ans=='how are you?':
                wx.SendMsg(msg='I am fine.')
            if glm_ans=='what is this?':
                wx.SendMsg(msg='this is my database')
            if glm_ans=='how can I use this data base':
                wx.SendMsg(msg='you-can-use-the-data-base-in-a-special-way(such-like:a-b-c)')
            if glm_ans=='how-can-i-create-this-database':
                wx.SendMsg(msg='please-call-H(wxid=H18201697173)')
            if glm_ans=='is-that-an-ai':
                wx.SendMsg(msg='yes')
    if glm1=='/chat2':#can be change
        while 1:
            glm_ans=wx.GetLastMessage[1]
            time.sleep(1)
            wx.SendMsg('WARNING:此模块已废弃[5sec]')
            time.sleep(5)
            if glm_ans=='hi':
                wx.SendMsg(msg='hello')
            elif glm_ans=='how-are-you':
                wx.SendMsg(msg='I-am-fine')
            elif glm_ans=='what-is-this':
                wx.SendMsg(msg='this-is-my-database')
            elif glm_ans=='how-can-I-use-this-data-base':
                wx.SendMsg(msg='you-can-use-the-data-base-in-a-special-way(such-like:a-b-c)')
            elif glm_ans=='how-can-i-create-this-database':
                wx.SendMsg(msg='please-call-H(wxid=H18201697173)')
            elif glm_ans=='is-that-an-ai':
                wx.SendMsg(msg='yes')
            elif glm_ans=='你好':
                wx.SendMsg(msg='你好！')
            elif glm_ans=='你是谁':
                wx.SendMsg(msg='我是Halpha人工智能')
            elif glm_ans=='这是什么':
                wx.SendMsg(msg='这是我的数据库')
            elif glm_ans=='你在吗？':
                wx.SendMsg(msg='我在')
            elif glm_ans=='这台人工智能怎么用':
                wx.SendMsg(msg='[AI也不知道]')
            elif glm_ans=='这是什么类型的程序':
                wx.SendMsg(msg='Python(ver=3.8,use pyofficerobot)')
            elif glm_ans=='这个人工智能有对话能力吗？':
                wx.SendMsg(msg='也许有')
            elif glm_ans=='知道chatGPT吗?':
                wx.SendMsg(msg='知道')
            elif glm_ans=='这个人工智能是如何建立数据库的':
                wx.SendMsg(msg='请联系Halpha')
            else:
                wx.SendMsg("none files of your question")
                wx.SendMsg("请输入问题")
                while 1:
                    glm5=wx.GetLastMessage[1]
                    if glm5=="请输入问题":
                        print("waiting")
                    else:
                        continue
                wx.SendMsg("请回答问题")
                while 1:
                    glm6=wx.GetLastMessage[1]
                    if glm6=="请回答问题":
                        print("waiting")
                    else:
                        continue
                c="elif glm_ans=='"+glm6+"':\n"+"   wx.SendMsg(msg='"+glm6+"')\n"
                with open('return.txt', 'a') as txt:
                    txt.write(c)
                    txt.close()
    if glm1=='/chatgpt':
        #must be change
        openai.api_key = "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"

        # Document
        wx.SendMsg(msg='-------------------------------------------------- Documents Begin --------------------------------------------------')
        wx.SendMsg("Attention:")
        wx.SendMsg("This program is only for entertainment. NOT BUSINESS AVAILABLE.")
        wx.SendMsg("Model in this program is from OpenAI company. More information about this model, please access https://openai.com/blog/chatgpt/")
        wx.SendMsg("Please do not enter keyboard before AI gives an answer, maybe it take some time, please wait patiently.")
        wx.SendMsg("We suggest you input your question in English.")
        wx.SendMsg("--------------------------------------------------- Documents End ---------------------------------------------------")
        wx.SendMsg('Input your question below:')
        # Main program
        while True:
            Question = wx.GetLastMessage[1]
            if Question!='Input your question below:':
                completion = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=Question,
                    max_tokens=1024,
                    temperature=0.5
                )
                Answer = completion.choices[0].text
                wx.SendMsg(Answer)
                wx.SendMsg("------------------------------------------------------------------------------------------------------")
                wx.SendMsg('Input your question below:')
            else:
                print('none')
    #endline
