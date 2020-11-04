import requests
import json
def get_content(password,user):
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    print(content)
    content = json.loads(content)
    return content

def xiaohao_trade():
    userprefix = "buwzzxh"
    password = "123456"

    def silver_hole(token):
        url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=island&m=pk&token_uid=31973&token="+token + "&channel=9&lang=zh-cn&rand=155099000816495&id="
        for i in range(11, 15):
            requests.post(url + str(i))
        url += "15"
        for i in range(5):
            re = requests.post(url)  # silver hole
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]  # 86

    cur_site = "1"
    cur_id = "0"
    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        if "token" not in content:
            print("###########################3" + str(user_info[i]))
            continue
        token = content['token']
        check_gouhuo = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=overseastrade&&m=item_list&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1602918819&signature=bdac98fd1bb56dc620ffb0263d962536"
        buy_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=overseastrade&&m=buy_item&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1602918819&signature=bdac98fd1bb56dc620ffb0263d962536&id=1"
        check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=overseastrade&&m=get_list_by_country&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1602918819&signature=bdac98fd1bb56dc620ffb0263d962536"
        join_team = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=overseastrade&&m=join_team&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1602918819&signature=bdac98fd1bb56dc620ffb0263d962536&id={id}&site={site}&page=2&place=1"
        requests.post(check_gouhuo)
        requests.post(buy_url)
        requests.post(check_url)
        print(join_team.format(site=cur_site,id=cur_id))

        resp = requests.post(join_team.format(site=cur_site,id=cur_id)).content.decode()
        tradebyforce = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=overseastrade&&m=trade&&token_uid=6792235&token="+token+"&channel=1&lang=zh-cn&rand=1602921874&signature=21cf1c3d1bf90a33c0a04e5c98d42fba"
        requests.post(tradebyforce)
if __name__ == "__main__":
     xiaohao_trade()