import requests
import json


def get_content(password,user):
    r = requests.post(
        "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    print(content)
    content = json.loads(content)
    return content

def zhuzhen():
    token = get_content("yjz2012123", "yjz2012123")['token']
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=assist_copy&&m=sweep&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158856330204296&times=5&mission_id=60".format(token)
    for i in range(3):
        requests.post(url)
def jifen():
    content = get_content("yjz2012123", "yjz2012123")
    arena_jifen_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=arena&&m=get_reward&&token_uid=31973&token=" + \
                      content['token'] + "&channel=9&lang=zh-cn&rand=156255546745079"
    requests.post(arena_jifen_url)
    # fuck_kenglila_check = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=country&&m=get_audit_list&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265322894261"
    # fuck_kenglila_confirm = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=country&&m=ignore_all&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=156265323552191"
    # requests.post(fuck_kenglila_check)
    # requests.post(fuck_kenglila_confirm)]
    world_boss_jifen = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=worldboss&&m=reward&&token_uid=31973&token=" + \
                       content['token'] + "&channel=9&lang=zh-cn&rand=156257044398440"
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=sign&&m=sign_index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099296558640"
    r = requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=logined&m=get_reward&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132492285595&id=15"
    requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=logined&&m=get_reward&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155659269533816"
    requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=vipwage&&m=get_vip_wage&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155659274740646"
    requests.post(url)
    requests.post(world_boss_jifen)
def xiaohao_donation():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]  # 86
    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        if "token" not in content:
            print("###########################3" + str(user_info[i]))
            continue
        token = content['token']
        DONATE_URL = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=country&&m=donate&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157735055776467&type=1"
        get_salary_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=country&&m=get_salary&&token_uid=6792227&token=" + token + "&channel=1&lang=zh-cn&rand=157743508062665"
        sacrifice_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=countrysacrifice&&m=action&&token_uid=6792227&token=" + token + "&channel=1&lang=zh-cn&rand=157743498216098&id=1"
        requests.post(sacrifice_url)
        requests.post(get_salary_url)
        lottery_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=lottery&&m=action&&token_uid=6792227&token=" + token + "&channel=1&lang=zh-cn&rand=157743516577048"
        for i in range(7):
            requests.post(lottery_url)
        for i in range(60):
            requests.post(DONATE_URL)
def xiaohao_levelup():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]  # 86
    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        if "token" not in content:
            print("###########################3" + str(user_info[i]))
            continue
        token = content['token']
        index_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239787352490".format(token)
        resp1 = json.loads(requests.post(index_url).content.decode())
        print(resp1)
        check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=map&&m=mission&&token_uid=6792235&token="+token+"&channel=1&lang=zh-cn&rand=1602918004&signature=191fcf794abdad04ba822059cdda6449&l={l}&s={l}&id={id}"
        attack_url = 'http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=action&&token_uid=31973&token={token}&channel=9&lang=zh-cn&rand=1602913036&signature=95f2d71a5d01d0954ff7e58204b540c&fl={l}&s={s}&id={id}'
        map_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token={token}&channel=9&lang=zh-cn&rand=1602915124&signature=a151bdaef48176601d47f28ff2c839df&l={l}&s={s}"
        for l in range(3, 4):
            for s in range(1, 4):
                resp2 = json.loads(requests.post(map_url.format(token=token,l=l,s=s)).content.decode())
                print(resp2)
                for id in range(1, 11):
                    resp1 = json.loads(requests.post(check_url.format(l=l, s=s, id=id)).content.decode())

                    member_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=member&&m=index&&token_uid=6792235&token="+token+"&channel=1&lang=zh-cn&rand=1602918359&signature=cdb5908efccfe9474abd06bbca40fd5f"
                    message_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=message&&m=index&&token_uid=6792235&token="+token+"&channel=1&lang=zh-cn&rand=1602918359&signature=cdb5908efccfe9474abd06bbca40fd5f"
                    print(json.loads(requests.post(member_url).content.decode()))
                    print(json.loads(requests.post(message_url).content.decode()))
                    resp2 = json.loads(requests.post(attack_url.format(token=token, l=l, s=s, id=id)).content.decode())
                    print(resp1)
                    print(resp2)
def print_response(resq):
    print(json.loads(requests.post(resq).content.decode()))
def xiaohao_trade():
    userprefix = "buwzzxh"
    password = "123456"

    def silver_hole(token):
        url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=island&m=pk&token_uid=31973&token="+token + "&channel=9&lang=zh-cn&rand=155099000816495&id="
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
        print_response(check_gouhuo)
        print_response(buy_url)
        requests.post(check_url)
        print(join_team.format(site=cur_site,id=cur_id))

        resp = json.loads(requests.post(join_team.format(site=cur_site,id=cur_id)).content.decode())
        tradebyforce = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=overseastrade&&m=trade&&token_uid=6792235&token="+token+"&channel=1&lang=zh-cn&rand=1602921874&signature=21cf1c3d1bf90a33c0a04e5c98d42fba"
        requests.post(tradebyforce)

def xiaohao_silver():
    userprefix = "buwzzxh"
    password = "123456"

    def silver_hole(token):
        url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=island&m=pk&token_uid=31973&token="+token + "&channel=9&lang=zh-cn&rand=155099000816495&id="
        for i in range(11, 15):
            requests.post(url + str(i))
        url += "15"
        for i in range(5):
            re = requests.post(url)  # silver hole
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]  # 86


    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']
        if "token" not in content:
            print("###########################3" + str(user_info[i]))
            continue
        zhengshou_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=city&&m=impose&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1602922218&signature=59681f19c96e77701c62d31d9672b54a"
        for i in range(12):
            requests.post(zhengshou_url)
        silver_hole(token)



# def buy_ninglingge():
#     token = get_content("123456", "buwzzxh1")["token"]
#     buy_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=tavern&&m=buy&&token_uid=6792173&token="+token+"&channel=1&lang=zh-cn&rand=1602915720&signature=41128be3fde2dc249cc27264a2c6e377&generalid=124"
#     shangzhen_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=muster&&m=go_battle&&token_uid=6792173&token="+token+"&channel=1&lang=zh-cn&rand=1602915720&signature=41128be3fde2dc249cc27264a2c6e377&gid=368203&confrim=0"
#     print_response(buy_url)
#     print_response(shangzhen_url)
#     start_xunlian = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=practice&&m=practice_start&&token_uid=6792173&token="+token+"&channel=1&lang=zh-cn&rand=1602916760&signature=b696157f5faf54a65ca18656b052bef0&pid=154895&gid=368203&type=1"
#     print_response(start_xunlian)
#     xunlian50_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=practice&&m=mop&&token_uid=6792173&token="+token+"&channel=1&lang=zh-cn&rand=1602916879&signature=0c857f331e803a40ed8783c9fb1e8265&gid=368203&times=50"
#     print_response(xunlian50_url)
#     xunlian1_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=practice&&m=go_leap&&token_uid=6792173&token="+token+"&channel=1&lang=zh-cn&rand=1602917049&signature=ad9e93299fc5821572932ce104b5cb06&gid=368203"
#     for i in range(50):
#         resp = json.loads(requests.post(xunlian1_url).content.decode())
#         if str(resp['status']) == "-4":
import random

def xiaohaoshengguan():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 1)] + [[password, userprefix + str(j)] for j in
                                                                          range(57, 86)]  # 86



    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']
        if "token" not in content:
            print("###########################3" + str(user_info[i]))
            continue
        for i in range(30):
            usurp_info_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=country&&m=get_usurp_info&&token_uid=6792226&token=" + token + "&channel=1&lang=zh-cn&rand=1603059468&signature=bacd2c82fb71c8047bb2224280273027"
            usurp_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=country&&m=usurp&&token_uid=6792226&token=" + token + "&channel=1&lang=zh-cn&rand=1603059468&signature=bacd2c82fb71c8047bb2224280273027"
        print_response(usurp_info_url)
        print_response(usurp_url)

def sweep():
    juexing_sweep_check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=awaken_copy&&m=sweep_index&&token_uid=31973&token=aHjfXDrSsS9NqOBritPmpQ&channel=9&lang=zh-cn&rand=1603186364&signature=9eeb9012ee7e31239750b8fdd560d8a6&check=57"
    juexing_sweep_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=awaken_copy&&m=sweep&&token_uid=31973&token=aHjfXDrSsS9NqOBritPmpQ&channel=9&lang=zh-cn&rand=1603186364&signature=9eeb9012ee7e31239750b8fdd560d8a6&check=57&times=5"
    requests.post(juexing_sweep_check_url)
    requests.post(juexing_sweep_url)

    juexing_sweep_check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=awaken_copy&&m=sweep_index&&token_uid=31973&token=aHjfXDrSsS9NqOBritPmpQ&channel=9&lang=zh-cn&rand=1603186364&signature=9eeb9012ee7e31239750b8fdd560d8a6&check=58"
    juexing_sweep_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=awaken_copy&&m=sweep&&token_uid=31973&token=aHjfXDrSsS9NqOBritPmpQ&channel=9&lang=zh-cn&rand=1603186364&signature=9eeb9012ee7e31239750b8fdd560d8a6&check=58&times=5"
    requests.post(juexing_sweep_check_url)
    requests.post(juexing_sweep_url)
def all_freebee():
    jinji_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=chicken&&m=get_vip_reward&&token_uid=31973&token=eSFMokLSPZQNf91r4FgAzA&channel=9&lang=zh-cn&rand=1603186709&signature=fc4c5c833d98b87aaa78897394cb29e7&id=40"
if __name__ == "__main__":
    #zhuzhen()
    jifen()

    xiaohao_donation()
    xiaohao_silver()
