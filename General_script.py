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
if __name__ == "__main__":
    zhuzhen()
