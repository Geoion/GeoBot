# -*- coding: utf-8 -*-
import random
from datetime import date

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me! @{}".format(update.message.from_user["username"]))

def roll(bot, update):
    if int(update.message.from_user["id"]) == 354713607:
        result = "@{0} 的点数为：{1} (1-100)".format(update.message.from_user["username"], random.choice(range(80,101)))
    else:
        result = "@{0} 的点数为：{1} (1-100)".format(update.message.from_user["username"], random.choice(range(1,101)))
    bot.sendMessage(chat_id=update.message.chat_id, text=result)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
    InlineQueryResultArticle(
        id=query.upper(),
        title='Caps',
        input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answerInlineQuery(update.inline_query.id, results)

def userinfo(bot, update):
    user_info = update.message.from_user
    bot.sendMessage(chat_id=update.message.chat_id, 
                    text=", ".join(["{}: {}".format(k,v) for k,v in user_info.items()]))

def huanqian(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="今天@SunskyXH 还am钱了么？")

def today_guidance(bot, update):
    today = date.today()
    uid = int(update.message.from_user["id"])
    activities = [
        {
            "name": "写单元测试",
            "good": "写单元测试将减少出错",
            "bad": "写单元测试会降低你的开发效率"
        },{
            "name": "洗澡",
            "good": "你几天没洗澡了？",
            "bad": "会把写代码的灵感洗掉"
        },{
            "name": "锻炼一下身体",
            "good": "写代码会非常精神",
            "bad": "能量没消耗多少，吃得却更多"
        },{
            "name": "抽烟",
            "good": "抽烟有利于提神，增加思维敏捷",
            "bad": "除非你活够了，死得早点没关系"
        },{
            "name": "白天上线",
            "good": "今天白天上线是安全的",
            "bad": "可能导致灾难性后果"
        },{
            "name": "重构",
            "good": "代码质量得到提高",
            "bad": "你很有可能会陷入泥潭"
        },{
            "name": "使用%t",
            "good": "你看起来更有品位",
            "bad": "别人会觉得你在装逼"
        },{
            "name": "跳槽",
            "good": "该放手时就放手",
            "bad":"鉴于当前的经济形势，你的下一份工作未必比现在强"
        },{
            "name": "招人",
            "good": "你面前这位有成为牛人的潜质",
            "bad": "这人会写程序吗？"
        },{
            "name": "面试",
            "good": "面试官今天心情很好",
            "bad": "面试官不爽，会拿你出气"
        },{
            "name": "申请加薪",
            "good": "老板今天心情很好",
            "bad": "公司正在考虑裁员"
        },{
            "name": "晚上加班",
            "good": "晚上是程序员精神最好的时候",
            "bad": "喝太多咖啡可能会腹泻"
        },{
            "name": "在妹子面前吹牛",
            "good": "改善你矮穷挫的形象",
            "bad": "会被识破"
        },{
            "name": "浏览成人网站",
            "good": "重拾对生活的信心",
            "bad": "你会心神不宁"
        },{
            "name": "写超过1000行的方法",
            "good": "你的代码组织的很好，长一点没关系",
            "bad": "你的代码将混乱不堪，你自己都看不懂"
        },{
            "name": "提交代码",
            "good": "遇到冲突的几率是最低的",
            "bad": "你遇到的一大堆冲突会让你觉得自己是不是时间穿越了",
        },{
            "name": "代码review",
            "good": "发现重要问题的几率大大增加",
            "bad": "你会发现你的代码像一坨屎",
        },{
            "name": "开会",
            "good": "写代码之余放松一下打个盹，有益健康",
            "bad": "小心被扣屎盆子背黑锅",
        },{
            "name": "打DOTA",
            "good": "你将有如神助",
            "bad": "你会被虐的很惨",
        },{
            "name": "晚上上线",
            "good": "晚上是程序员精神最好的时候",
            "bad": "你白天已经筋疲力尽了",
        },{
            "name": "修复BUG",
            "good": "你今天对BUG的嗅觉大大提高",
            "bad": "新产生的BUG将比修复的更多",
        },{
            "name": "上微博",
            "good": "今天发生的事不能错过",
            "bad": "今天的微博充满负能量",
        },{
            "name": "上AB站",
            "good": "还需要理由吗？",
            "bad": "满屏兄贵亮瞎你的眼",
        },{
            "name": "玩FlappyBird",
            "good": "今天破纪录的几率很高",
            "bad": "除非你想玩到把手机砸了",
        }
    ]
    weeks =  ["日", "一", "二", "三", "四", "五", "六"]
    directions = ["北方", "东北方", "东方", "东南方", "南方", "西南方", "西方", "西北方"]
    drinks = ["水", "茶", "红茶", "绿茶", "咖啡", "奶茶", "可乐", "鲜奶", "豆奶", "果汁", "果味汽水", "苏打水", "运动饮料", "酸奶", "酒"]
    result = "今天是{0}年{1}月{2}日 星期{3}\n".format(today.year, today.month, today.day, weeks[today.isoweekday()])
    result += "@{0}\n>>> 今日 宜：\n".format(update.message.from_user["username"])
    choice = today.day*today.isoweekday()*uid%len(activities) 
    result += "{0} ({1})\n".format(activities[choice]["name"], activities[choice]["good"])
    del activities[choice]
    choice = today.day*today.isoweekday()*11*uid%(len(activities)-1)
    result += "{0} ({1})\n".format(activities[choice]["name"], activities[choice]["good"])
    del activities[choice]
    result += ">>> 今日 不宜：\n"
    choice = today.day*today.isoweekday()*3*uid%(len(activities)-2)
    result += "{0} ({1})\n".format(activities[choice]["name"], activities[choice]["bad"])
    del activities[choice]
    choice = today.day*today.isoweekday()*7*uid%(len(activities)-2)
    result += "{0} ({1})\n".format(activities[choice]["name"], activities[choice]["bad"])
    del activities[choice]
    result += ">>> 座位朝向：面向{0}写代码，BUG最少。\n".format(directions[today.day*uid%len(directions)])
    result += ">>> 状态加成：喝{0}".format(drinks[today.day*today.isoweekday()*uid%len(drinks)])

    bot.sendMessage(chat_id=update.message.chat_id, text=result)

def dream(bot, update):
    count = 0
    redno_list = []
    blueno = []
    while count < 6:
        temp = choice(range(1, 34))
        if temp in redno_list:
            continue
        else:
            redno_list.append(temp)
            count = count + 1

    blueno = choice(range(1, 17))
    redno_list.sort()
    redno = ",".join([str(i) for i in redno_list])
    bot.sendMessage(chat_id=update.message.chat_id, text="{} 的梦想号码(双色球)是：\n红球 {}，蓝球 {}".format(update.message.from_user["username"], redno, blueno))

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="{1}:\nSorry, I didn't understand that command.".format(update.message.from_user["username"]))

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, 
                    text="""Use /start to test this bot.\nuse /roll feeling lucky""")
    