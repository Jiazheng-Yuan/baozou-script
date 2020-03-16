import requests
import json
def get_content(password,user):
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content
def qixielueduo():
    categories = ["tree","stone"]
    token = get_content("yjz2012123", "yjz2012123")['token']
    for category in categories:
        try:
            wood_check = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot_index&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239849642689".format(category,token)
            res = json.loads(requests.post(wood_check).content.decode())
            uid = res["loot_list"][0]['uid']
            wood_attack = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239862309448&touid={}".format(category,token,uid)
            requests.post(wood_attack)
            finish_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot_lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239894482311".format(category,token)
            res = json.loads(requests.post(finish_url).content.decode())
            count = 0
            for item in res["reward"]:
                print(item)
                if item['reward_param'] == 3:
                    count += item['reward_value']

            if count >= 3:
                print(res)
                lottery = "p://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239941428587".format(category,token)
                get_all_lottery = "p://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=get_all_lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239942078067".format(category,token)
                requests.post(lottery)
                requests.post(get_all_lottery)
        except:
            pass
if __name__ == "__main__":
    for i in range(14):
        qixielueduo()