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

    content = get_content("yjz2012123", "yjz2012123")
    arena_jifen_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=arena&&m=get_reward&&token_uid=31973&token=" + \
                      content['token'] + "&channel=9&lang=zh-cn&rand=156255546745079"
    requests.post(arena_jifen_url)
    # fuck_kenglila_check = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=get_audit_list&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265322894261"
    # fuck_kenglila_confirm = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=ignore_all&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265323552191"
    # requests.post(fuck_kenglila_check)
    # requests.post(fuck_kenglila_confirm)

    world_boss_jifen = "http://s32.game.baozouwushuang.com/index.php?v=0&c=worldboss&&m=reward&&token_uid=31973&token=" + \
                       content['token'] + "&channel=9&lang=zh-cn&rand=156257044398440"
    requests.post(world_boss_jifen)

    consecutive_login_check = "http://s32.game.baozouwushuang.com/index.php?v=0&c=logined&&m=index&&token_uid=31973&token=" + \
                              content['token'] + "&channel=9&lang=zh-cn&rand=156255851095191"
    consecutive_login_get = "http://s32.game.baozouwushuang.com/index.php?v=0&c=logined&&m=get_reward&&token_uid=31973&token=" + \
                            content['token'] + "&channel=9&lang=zh-cn&rand=156255851419186&id=15"
    requests.post(consecutive_login_check)
    requests.post(consecutive_login_get)
    free_yuanbao = "http://s32.game.baozouwushuang.com/index.php?v=0&c=christmasgift&&m=get_reward&&token_uid=31973&token=" + \
                   content['token'] + "&channel=9&lang=zh-cn&rand=156255551968282&id=2"
    requests.post(free_yuanbao)

    for i in range(14):
        qixielueduo()
    user_info = [["123456","buwzzxh" + str(i)] for i in range(148,151)] + [["yjz2012123","yjz2012123"]]
    for password,username in user_info:
        content = get_content(password,username)
        token = content['token']
        yuanbao_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=actjubao&&m=action&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157732067703616&type=1"
        requests.post(yuanbao_url)