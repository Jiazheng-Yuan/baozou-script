import requests
import json


def get_content(password,user):
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content

def zhuzhen():
    token = get_content("yjz2012123", "yjz2012123")['token']
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=assist_copy&&m=sweep&&token_uid=31973&token={token}&channel=9&lang=zh-cn&rand=158856330204296&times=5&mission_id=60".format(token=token)
    for i in range(3):
        requests.post(url)
def jifen():
    content = get_content("yjz2012123", "yjz2012123")
    arena_jifen_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=arena&&m=get_reward&&token_uid=31973&token=" + \
                      content['token'] + "&channel=9&lang=zh-cn&rand=156255546745079"
    requests.post(arena_jifen_url)
    # fuck_kenglila_check = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=get_audit_list&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265322894261"
    # fuck_kenglila_confirm = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=ignore_all&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265323552191"
    # requests.post(fuck_kenglila_check)
    # requests.post(fuck_kenglila_confirm)]
    world_boss_jifen = "http://s32.game.baozouwushuang.com/index.php?v=0&c=worldboss&&m=reward&&token_uid=31973&token=" + \
                       content['token'] + "&channel=9&lang=zh-cn&rand=156257044398440"
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=sign&&m=sign_index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099296558640"
    r = requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=logined&m=get_reward&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132492285595&id=15"
    requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=logined&&m=get_reward&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155659269533816"
    requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=vipwage&&m=get_vip_wage&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155659274740646"
    requests.post(url)
    requests.post(world_boss_jifen)
if __name__ == "__main__":
    zhuzhen()
    jifen()