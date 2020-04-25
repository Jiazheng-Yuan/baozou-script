import requests
import json
def get_content(password, user):
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=" + user + "&p=" + password + "&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content
if __name__ == "__main__":
    print("123456","buwzzxh51")