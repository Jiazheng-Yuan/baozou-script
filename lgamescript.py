import requests
import json

import time


def lottery_rank(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=springlottery&&m=index&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099070112696"
    while True:
        r = requests.post(url)
        content = json.loads(r.content)
        userlist = content['userlist']
        if len(userlist) == 3:
            break
    # print(len(userlist))

    url_lottery = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=springlottery&&m=action&&token_uid=31973&token=" + \
                  content['token'] + "&channel=9&lang=zh-cn&rand=155099234854935"
    # print(r.content[])
    requests.post(url_lottery)


def silver_hole(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=island&m=pk&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099000816495&id="
    for i in range(84, 86):
        requests.post(url + str(i))
    url += "85"
    for i in range(17):
        re = requests.post(url)  # silver hole
        # print(re.content)


def sign_in(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=sign&&m=sign_index&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099296558640"
    r = requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=logined&m=get_reward&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155132492285595&id=15"
    requests.post(url)


def donate(content, times):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=country&&m=donate&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099312403245&type=1"
    for i in range(times):
        # pool.apply_async(requests.post, [url])
        requests.post(url)


def sacfirice_for_nation(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=countrysacrifice&m=action&token_uid=31973&token=" + \
          content['token'] + "&channel=9&lang=zh-cn&rand=155099341822220&id=1"
    r = requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=country&&m=get_salary&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155102761189739"
    requests.post(url)


def business(content):
    token = content['token']
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=business&&m=index&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099586487582"
    re = requests.post(url)
    content = json.loads(re.content.decode())
    traders = content['trader']

    # url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=business&m=go_business&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099356533783&id=6"
    # for i in range(80):
    # re = requests.post(url)
    # content = json.loads(re.content.decode())

    while True:
        trader_id = str(traders[0]['id'])
        # print(trader_id)
        url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=business&m=go_business&token_uid=31973&token=" + \
              token + "&channel=9&lang=zh-cn&rand=155099356533783&id=" + trader_id
        re = requests.post(url)
        content = json.loads(re.content.decode())
        print(content)
        try:
            traders = content['trader']
            if content['times'] == 0:
                break
        except:
            break


def jade_mine(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=countrymine&&m=index&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099446630583"
    re = requests.post(url)
    response_content = json.loads(re.content.decode())
    user_list = response_content['list']
    time = response_content['log']['times']
    if time > 1:
        pass
    return response_content


def shenjiangzhimen(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=generaltask&m=action&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099655983030&id=399&type=0&gid=362120"
    for i in range(10):
        requests.post(url)


def hero_throne(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=herothrone&&m=index&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155176609795753"
    requests.post(url)
    for i in range(4):
        try:
            url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=herothrone&&m=start&&token_uid=31973&token=" + \
                  content['token'] + "&channel=9&lang=zh-cn&rand=155102736139239"
            requests.post(url)
        except:
            return
        url_391 = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=herothrone&&m=action&&token_uid=31973&token=" + \
                  content['token'] + "&channel=9&lang=zh-cn&rand=155099683928379"
        # url_392 = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=herothrone&&m=action&&token_uid=31973&token=FJ8ZTtOt96no73HhibG9mQ&channel=9&lang=zh-cn&rand=155099693188373"
        for i in range(10):
            re = requests.post(url_391)
            print(json.loads(re.content.decode()))
        # print(json.loads(re.content.decode()))


def dice(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=dice&&m=shake_dice&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155102770131520"
    for i in range(7):
        requests.post(url)


def jianghunxinglu(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=tower&m=get_mopup_price&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155102830162193&id=118"
    re = requests.post(url)
    condition = json.loads(re.content.decode())
    if int(condition['info']['ten_sub']) == 0:
        url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=tower&m=mop_up&token_uid=31973&token=" + content[
            'token'] + "&channel=9&lang=zh-cn&rand=155102790179643&id=118&times=10"
        re = requests.post(url)
        # print(re.content)


def atk_roll(content):
    check_status_url_pre = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=mission&token_uid=31973&token=" + \
                           content['token'] + "&channel=9&lang=zh-cn&rand=155102870704658&"

    necessary_pre_check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token=" + \
                              content['token'] + "&channel=9&lang=zh-cn&rand=155103095467635"
    battle_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=action&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155103095467635&"  # l=18&s=1&id=8&times=5"
    map_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token=" + \
              content['token'] + "&channel=9&lang=zh-cn&rand=15510326043749"
    for l in range(17, 19):
        for s in range(1, 8):
            map_param = "&l=" + str(l) + "&s=" + str(s)
            requests.post(map_url + map_param)
            for id in range(6, 7, 2):
                params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id)
                check_status_url = check_status_url_pre + params
                condition = json.loads(requests.post(check_status_url).content.decode())
                nowmaxtimes = int(condition['info']['nowmaxtimes'])
                if nowmaxtimes > 0:
                    # re = requests.post(necessary_pre_check_url)
                    # print(json.loads(re.content.decode()))
                    battle_params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id) + "&times=" + str(nowmaxtimes)
                    true_battle_url = battle_url + battle_params
                    # print(true_battle_url)
                    requests.post(true_battle_url)
                    # print(json.loads(re.content.decode()))

    param = []


def jewel(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=sanctum&m=action&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155132506502966&id=250&times=1"
    for i in range(10):
        requests.post(url)


def tongtianta(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=heaven&m=mop_up&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155132527649516&id=177&times=10"
    requests.post(url)


def shenzhu(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token=" + \
          content['token'] + "&channel=9&lang=zh-cn&rand=15513239203246&times=5&monster_id=6&diff_id=3&id=3"
    requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token=" + \
          content['token'] + "&channel=9&lang=zh-cn&rand=15513239203246&times=5&monster_id=10&diff_id=3&id=3"
    requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token=" + \
          content['token'] + "&channel=9&lang=zh-cn&rand=155132427716932&id=1&diff_id=3&monster_id=10&times=5"
    requests.post(url)
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token=" + \
          content['token'] + "&channel=9&lang=zh-cn&rand=155132427716932&id=1&diff_id=3&monster_id=6&times=5"
    requests.post(url)


def daily_lottery(content):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=lottery&&m=action&&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155132452941485"
    for i in range(7):
        requests.post(url)


def xiaohao():
    password = "zzz2012123"
    usr = "zzz2012123"
    r = requests.post(
        "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)

    check_status_url_pre = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=mission&token_uid=31973&token=" + \
                           content['token'] + "&channel=9&lang=zh-cn&rand=155102870704658&"

    necessary_pre_check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token=" + \
                              content['token'] + "&channel=9&lang=zh-cn&rand=155103095467635"
    battle_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=action&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155103095467635&"  # l=18&s=1&id=8&times=5"
    map_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token=" + \
              content['token'] + "&channel=9&lang=zh-cn&rand=15510326043749"
    for l in range(19, 20):
        for s in range(1, 2):
            map_param = "&l=" + str(l) + "&s=" + str(s)
            requests.post(map_url + map_param)
            for id in range(1, 2):
                params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id)
                check_status_url = check_status_url_pre + params
                condition = json.loads(requests.post(check_status_url).content.decode())
                print(condition)
                # nowmaxtimes = int(condition['info']['nowmaxtimes'])
                # if nowmaxtimes > 0:
                # re = requests.post(necessary_pre_check_url)
                # print(json.loads(re.content.decode()))
                battle_params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id) + "&times=" + str(1)
                true_battle_url = battle_url + battle_params
                # print(true_battle_url)
                for i in range(300):
                    requests.post(true_battle_url)


def chaogong(content):
    check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=flop&&m=index&&token_uid=31973&token=3Bx_0YOTbrWYQ9dPC4_jOg&channel=9&lang=zh-cn&rand=155655985061498"
    flop_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=flop&&m=turnover&&token_uid=31973&token=3Bx_0YOTbrWYQ9dPC4_jOg&channel=9&lang=zh-cn&rand=155655979346793&id=5"
    response = json.loads(requests.post(check_url).content.decode())
    response = json.loads(requests.post(check_url).content.decode())
    for key, item in response.items():
        if key == "box_reward":
            for i in item:
                print(i)
        print(key, item)

    response = json.loads(requests.post(flop_url).content.decode())
    print(response)


def fukuang_harvest(content):
    for i in range(1, 10):
        spot_num = i
        collect_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=harvest_mine&&token_uid=31973&token=" + \
                      content['token'] + "&channel=9&lang=zh-cn&rand=15565919538656&s=" + str(spot_num)
        response = json.loads(requests.post(collect_url).content.decode())
        print(response)


def fukuang_available_spots(content):
    check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token=" + \
                content['token'] + "&channel=9&lang=zh-cn&rand=155680885761671&p="
    available_spots = []
    for p in range(1, 6):
        response = json.loads(requests.post(check_url + str(p)).content.decode())
        for spot in response['list']:
            if str(spot['status']) == '0':
                available_spots.append([str(spot['page']), str(spot['id']), str(spot['type'])])
    return available_spots

    p = 1
    id = 1
    t = 1
    formdata = "&p=" + str(p) + "&id=" + str(id) + "&t=" + str(t)
    take_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=action_mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=155659196548989" + formdata


# response = requests.post("http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=15565922387968&p=3")
# content = json.loads(response.content.decode())
# for key,item in content.items():
#     if key == "list":
#         for i in item:
#             print(i)
#     else:
#         print(key,item)
def lianxiaohao():
    for i in range(2, 3):
        click = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=map&&m=mission&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659926245678&l=1&s=1&id=" + str(
            3)
        requests.post(click)

    battle = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    get_mission_list = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    index = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=member&&m=index&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=15565993617769"
    hit = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=map&&m=action&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659897286217"

    update_guide = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    mission_list = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=map&&m=get_mission_list&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659942527825"
    pool = [click, get_mission_list, index, hit, update_guide, index, mission_list]
    for url in pool:
        response = requests.post(url)
        content = json.loads(response.content.decode())
        for key, item in content.items():
            print(key, item)
    # r = requests.post(
    #     "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    #
    # check_status_url_pre = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=mission&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155102870704658&"
    #
    # necessary_pre_check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155103095467635"
    # battle_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&m=action&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155103095467635&"  # l=18&s=1&id=8&times=5"
    # map_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=15510326043749"
    # for l in range(1, 2):
    #     for s in range(1, 2):
    #         map_param = "&l=" + str(l) + "&s=" + str(s)
    #         requests.post(map_url + map_param)
    #         for id in range(1, 10):
    #             params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id)
    #             check_status_url = check_status_url_pre + params
    #             condition = json.loads(requests.post(check_status_url).content.decode())
    #             print(condition)
    #             # nowmaxtimes = int(condition['info']['nowmaxtimes'])
    #             # if nowmaxtimes > 0:
    #             # re = requests.post(necessary_pre_check_url)
    #             # print(json.loads(re.content.decode()))
    #             battle_params = "l=" + str(l) + "&s=" + str(s) + "&id=" + str(id) + "&times=" + str(1)
    #             true_battle_url = battle_url + battle_params


def get_content(password, user):
    r = requests.post(
        "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=" + user + "&p=" + password + "&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content


def get_available():
    content = get_content('123456', "buwzzxh52")
    return fukuang_available_spots(content)


def occupy_fukuang():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]
    spots = get_available()
    for i in range(len(user_info)):
        # if i >= len(spots):
        #    break

        p = spots[i][0]
        id = spots[i][1]
        t = spots[i][2]
        formdata = "&p=" + str(p) + "&id=" + str(id) + "&t=" + str(t)
        content = get_content(user_info[i][0], user_info[i][1])
        take_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=action_mine&&token_uid=31973&token=" + \
                   content['token'] + "&channel=9&lang=zh-cn&rand=155659196548989" + formdata

        response = json.loads(requests.post(take_url).content.decode())

        print(response)
        print(user_info[i])


def harvest():
    userprefix = "buwzzxh"
    password = "123456"
    for i in range(51, 86):
        fukuang_harvest(get_content(password, userprefix + str(i)))
    for i in range(1, 6):
        fukuang_harvest(get_content(password, userprefix + str(i)))


def check_lottery_list():
    checkurl = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=springlottery&&m=index&&token_uid=31973&token=5Fwn1RVD45EzUNU2efCSuw&channel=1&lang=zh-cn&rand=155716722639280"
    response = json.loads(requests.post(checkurl).content.decode())
    while 'userlist' in response and len(response['userlist']) != 3:
        response = json.loads(requests.post(checkurl).content.decode())
    draw_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=springlottery&&m=index&&token_uid=31973&token=5Fwn1RVD45EzUNU2efCSuw&channel=1&lang=zh-cn&rand=155716722639280"
    if 'userlist' in response and len(response['userlist']) == 3:
        requests.post(draw_url)


def longzhou(token):
    start = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=go_boat&&token_uid=6826319&token=" + token + "&channel=1&lang=zh-cn&rand=156988429136212"
    response = json.loads(requests.post(start).content.decode())
    print(response)
    direction = response['direction']
    for i in range(9):
        print("ere")
        direction_answer = "%2C".join([str(dir) for dir in direction])
        rowing_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=rowing_boat&&token_uid=6826319&token=" + token + "&channel=1&lang=zh-cn&rand=156988432015486&list=" + direction_answer
        resp = json.loads(requests.post(rowing_url).content.decode())
        print(resp)
        refresh_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=boat_index&&token_uid=6826319&token=" + token + "&channel=1&lang=zh-cn&rand=156988432072668"
        new_resp = json.loads(requests.post(refresh_url).content.decode())
        print(new_resp)
        try:
            old_direction = direction
            direction = resp['direction']
        except:
            direction = old_direction
        time.sleep(1)
        print(direction)


def all_longzhou(buy="notbuy"):
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(51, 86)]  # 86
    user_info.append(["yjz2012123", "yjz2012123"])
    print("loop start")
    for i in range(len(user_info)):

        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']
        print("debug start,user {}".format(user_info[i]))
        #yuanbao_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=actjubao&&m=action&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157732067703616&type=1"
        #requests.post(yuanbao_url)
        print(user_info[i])
        if buy == "buy" and user_info[0] != "yjz2012123":
            buytimes = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=buy_time&&token_uid=31973&token=" + token + "&channel=1&lang=zh-cn&rand=15698660881518"
            requests.post(buytimes)
        try:
            longzhou(token)
        except:
            continue


def xiaohao_donation():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(1, 3)] + [[password, userprefix + str(j)] for j in
                                                                          range(75, 86)]  # 86
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
        for i in range(20):
            requests.post(DONATE_URL)


def xinnianzhanling():
    content = get_content("yjz2012123", "yjz2012123")
    token = content['token']
    harvest_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=harvest&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988700903840&id=1"
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(148, 150)]  # 86
    rob_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=rob&&token_uid=31973&token=xiTPWLIFSPIz-uyZ5AJHTg&channel=9&lang=zh-cn&rand=157988813627385&id"
    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']


def xinnian_rob():
    content = get_content("yjz2012123", "yjz2012123")
    token = content['token']
    check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=occupy_list&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988860002249&id=1"
    res = json.loads(requests.post(check_url).content.decode())
    harvest_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=harvest&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988700903840&id=1"
    requests.post(harvest_url)
    for val in res["list"]:
        if val["country"] == "jiaz":
            rob_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=rob&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988813627385&cid=1&id=" + str(
                val["id"])
            requests.post(rob_url)
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password, userprefix + str(j)] for j in range(148, 150)]  # 86

    for i in range(len(user_info)):
        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']

        check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=occupy_list&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988860002249&id=1"
        res = json.loads(requests.post(check_url).content.decode())
        if not res["own_reward"]:
            occupy_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=occupy_city&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157988940407740&id=1"
            requests.post(occupy_url)
            break


import threading


def temp(url):
    # url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=ladder_war&&m=ladder_battle&&token_uid=31973&token="+get_content("yjz2012123","yjz2012123")["token"]+"&channel=9&lang=zh-cn&rand=158037374341422&id=3"
    # threading.Thread(target=requests.post,args=(url,))
    requests.post(url)


def tuitu():
    # index = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=mission&&token_uid=31973&token=yhxKPIReq-s48U6_wep8Dg&channel=9&lang=zh-cn&rand=158239778424833"
    token = "GFx6-tZ1TTqXZYqT-weW3A"
    index = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239787352490".format(
        token)
    action = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=action&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239787284178&l={}&s={}&id={}".format(
        token, 19, 5, 5)

    requests.post(index).content.decode()
    res = json.loads(requests.post(action).content.decode())

    while "info" in res and res["info"]["win"] < 0:
        requests.post(index)
        res = json.loads(requests.post(action).content.decode())
        print(res)


def qixielueduo():
    categories = ["stone", "tree"]
    for category in categories:
        token = get_content("yjz2012123", "yjz2012123")['token']
        wood_check = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot_index&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239849642689".format(
            category, token)
        res = json.loads(requests.post(wood_check).content.decode())
        uid = res["loot_list"][0]['uid']
        wood_attack = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239862309448&touid={}".format(
            category, token, uid)
        requests.post(wood_attack)
        finish_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=loot_lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239894482311".format(
            category, token)
        res = json.loads(requests.post(finish_url).content.decode())
        count = 0
        for item in res["reward"]:
            if item['reward_param'] != 2 and item['reward_param'] != 0:
                count += 1
        if count >= 4:
            print(res)
            lottery = "p://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239941428587".format(
                category, token)
            get_all_lottery = "p://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_{}&&m=get_all_lottery&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158239942078067".format(
                category, token)
            requests.post(lottery)
            requests.post(get_all_lottery)
def zhangu():
    get_content("yjz2012123", "yjz2012123")
    sweep_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=drum_forge&&m=go_sweep&&token_uid=31973&token=6dhxKf4FVG_qAYZzjy4dqw&channel=9&lang=zh-cn&rand=1617610232&signature=db4d0f6a3abc47833cfdd1bfc1516cd1"

def baowulianhua(content):
    #check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=jade_tower&&m=index&&token_uid=31973&token=" +content["token"] + "&channel=9&lang=zh-cn&rand=1620206249&signature=2d16bf7b1e99900d9fdc74ce009ef844"
    baowulianhua_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=jade_tower&&m=fight_refine&&token_uid=31973&token=" +content["token"] + "&channel=9&lang=zh-cn&rand=1620205970&signature=2905f94cd5959ea7d7007fafbc835932"
    for i in range(9):
        requests.post(
            baowulianhua_url,
            data={"refine_id": 15, "token": content["token"]})
def join_room(token, id):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=peace_art&&m=quick_join_team&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=1620279608&signature=e899a891901a67ffd0413df9c74c82d3"
    start = 100 * id
    end = 100 * (id + 1)
    # for i in range(start, end):
    #     pwd = str(i)
    #     pwd = "0" * (4 - len(pwd)) + pwd
    #     re = json.loads(requests.post(url,data={"id":1732,"pwd":pwd,"token":token}).content.decode())
    #     while "status" in re and re["status"] == 11:
    #         re = json.loads(requests.post(url, data={"id": 1732, "pwd": pwd, "token": token}).content.decode())
    #         if "status" in re and re["status"] == 1:
    #             print(pwd)
    #             print(re)
    #             exit(0)
    #     print(re)
    file = open("password/password" + str(id) + ".txt")
    used_password_last = start
    try:
        used_password_last = int(file.readlines()[-1].strip()) + 1
    except:
        pass
    file_appender = open("password/password" + str(id) + ".txt", "a")
    room_id = 1683
    for i in range(used_password_last, end):
        pwd = str(i)
        pwd = "0" * (4 - len(pwd)) + pwd
        re = json.loads(requests.post(url, data={"id": room_id, "pwd": pwd, "token": token}).content.decode())
        while "status" in re and re["status"] == 11:
            re = json.loads(
                requests.post(url, data={"id": room_id, "pwd": pwd, "token": token}).content.decode())
            if "status" in re and re["status"] == 1:
                print(pwd)
                print(re)
                answer = open("password/answer", 'w')
                answer.write(pwd)
                exit(0)
        print(re)
        print(pwd)
        file_appender.write(pwd + "\n")
        file_appender.flush()
def join_jade_room(token, id):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=jade_tower&&m=join_room&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=1620328888&signature=e976067821a526438fdd6fe8de08d880"
    start = 100 * id
    end = 100 * (id + 1)
    file = open("password/password" + str(id)+".txt")
    used_password_last = start
    try:
        used_password_last = int(file.readlines()[-1].strip()) + 1
    except:
        pass
    file_appender = open("password/password"+str(id)+".txt", "a")
    room_id = 42496
    for i in range(used_password_last, end):
        pwd = str(i)
        pwd = "0" * (4 - len(pwd)) + pwd
        re = json.loads(requests.post(url, data={"room_id": room_id, "password": pwd, "token": token}).content.decode())
        while "status" in re and re["status"] == 11:
            re = json.loads(requests.post(url, data={"room_id": room_id, "password": pwd, "token": token}).content.decode())
            if "status" in re and re["status"] == 1:
                print(pwd)
                print(re)
                answer = open("password/answer", 'w')
                answer.write(pwd)
                exit(0)
        print(re)
        print(pwd)
        file_appender.write(pwd + "\n")
        file_appender.flush()
def check_omitted(token):
    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=jade_tower&&m=join_room&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=1620328888&signature=e976067821a526438fdd6fe8de08d880"
    omitted = ['3604', '3605', '3606', '3607', '3608', '3609', '3610', '3611', '3612', '3613', '3614', '3615', '3616', '3617', '3618', '3619', '3620', '3621', '3622', '3623', '3624', '3625', '3626', '3627', '3628', '3629', '3630', '3631', '3632', '3633', '3634', '3635', '3636', '3637', '3638', '3639', '3640', '3641', '3642', '3643', '3644', '3645', '3646', '3647', '3648', '3649', '3650', '3651', '3652', '3653', '3654', '3655', '3656', '3657', '3658', '3659', '3660', '3661', '3662', '3663', '3664', '3665', '3666', '3667', '3668', '3669', '3670', '3671', '3672', '3673', '3674', '3675', '3676', '3677', '3678', '3679', '3680', '3681', '3682', '3683', '3684', '3685', '3686', '3687', '3688', '3689', '3690', '3691', '3692', '3693', '3694', '3695', '3696', '3697', '3698', '3699']
    for pwd in omitted:
        re = json.loads(requests.post(url, data={"room_id": 34722, "passw": pwd, "token": token}).content.decode())
        while "status" in re and re["status"] == 11:
            re = json.loads(requests.post(url, data={"room_id": 34722, "pwd": pwd, "token": token}).content.decode())
            if "status" in re and re["status"] == 1:
                print(pwd)
                print(re)
                answer = open("password/answer", 'w')
                answer.write(pwd)
                exit(0)
        print(pwd)
        print(re)

def vipReward():
    getVipScoreUrl = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=logined&&m=get_reward&&token_uid=31973&token=MoAS2-Yg-lF4-FmByD0FHA&channel=9&lang=zh-cn&rand=1626984151&signature=36838adba0a1d70b92012636acf7f094&id=165"
    getVipReward = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=vipwage&&m=get_vip_wage&&token_uid=31973&token=MoAS2-Yg-lF4-FmByD0FHA&channel=9&lang=zh-cn&rand=1626984151&signature=36838adba0a1d70b92012636acf7f094"
if __name__ == "__main__":



    # while True:
    #     pass
    # for i in range(14):
    #     qixielueduo()
    # tuitu(1,2)
    # content = get_content( "123456","buwzzxh53")
    # arena_jifen_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=arena&&m=get_reward&&token_uid=31973&token=" + content['token'] + "&channel=9&lang=zh-cn&rand=156255546745079"
    # print(requests.post(arena_jifen_url).content.decode())
    # token = get_content("123456","buwzzxh52")["token"]
    # longzhou(token)

    #all_longzhou()
    #all_longzhou()
    # # xinnian_rob()
    # all_longzhou("buy")
    # # xiaohao_donation()
    #all_longzhou("buy")
    # all_longzhou("buy")
    # all_longzhou("buy")
    # tuitu()
    # response = requests.post("http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=worldboss&&m=battle&&token_uid=31973&token=FS5ybWAd6z6nnApI33oYJg&channel=9&lang=zh-cn&rand=15600525866585&now=0")
    # response = json.loads(response.content.decode())
    # print(response)
    # check_lottery_list()

    # harvest()
    # occupy_fukuang()
    # lianxiaohao()
    # print(json.loads(re.content.decode()))

    # r = requests.post(
    #  "http://s32a.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=15509886868924&devicetoken=0000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    content = get_content("yjz2012123", "yjz2012123")
    # url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=quyuan_festival&&m=burn_grass&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=1616120707&signature=c6a6e118b270542aa586a7fad942e152"
    # url2 = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=quyuan_festival&&m=grass_index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=1616120707&signature=c6a6e118b270542aa586a7fad942e152"
    # for i in range(300):
    #     requests.post(url)
    #     requests.post(url2)

    choose_tribe = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=happy_double_festival&&m=treasure_hunter&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=1617400608&signature=23da00a4e3973ec3c1bda1f436d3e713"
    tanbao_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=happy_double_festival&&m=treasure_hunter&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=1617303308&signature=eb5f258c9e5be321af9d9a3b94255d88&tribe=1"
    for i in range(44):
        re = requests.post(tanbao_url)
        time.sleep(0.5)
        print(json.loads(re.content.decode()))
    # for i in range(26):
    #    chaogong("a")
    # response = requests.post("http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=15565922387968&p=3")
    # content = json.loads(response.content.decode())
    # for key,item in content.items():
    #     if key == "list":
    #         for i in item:
    #             print(i)
    #     else:
    #         print(key,item)
    # login

    # r = requests.post("http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # token = json.loads(content)['token']
    # donate(content,2200)
    """

    print(content)
    sign_in(content)

    shenjiangzhimen(content)
    #url = "http://s1.game.baozouwushuang.com/index.php?v=0&c=island&&m=index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155100655174835"
    silver_hole(content)

    business(content)

    sacfirice_for_nation(content)
    try:
        jianghunxinglu(content)
    except:
        pass
    dice(content)
    atk_roll(content)
    tongtianta(content)
    jewel(content)
    daily_lottery(content)
    shenzhu(content)

    #re = jade_mine(content)
    #lis = re['list']
    #print(re['list'])
    #print(r)
    #business(content)
    hero_throne(content)

    donate(content, 400)


    #hero_throne(content)



    yellow_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246113594820&refine_type=1&id=2"
    blue_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246130416038&id=1&refine_type=1"
    purple_url  = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246130416038&id=3&refine_type=1"
    trade_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246249389873"
    for i in range(20):

        requests.post(trade_url)
        requests.post(yellow_url)


        requests.post(purple_url)
    """


    # token = get_content("yjz2012123","yjz2012123")['token']
    # yellow_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246113594820&refine_type=1&id=2"
    # blue_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246130416038&id=1&refine_type=1"
    # purple_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246130416038&id=3&refine_type=1"
    # trade_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155246249389873"
    # def xinghun(url,time):
    #     q = []
    #     for i in range(time):
    #
    #         q.append(threading.Thread(target=requests.post,args=(url,)))
    #         q[-1].start()
    #     for t in q:
    #         t.join()
    # queue = []
    # queue.append(threading.Thread(target=xinghun, args=(trade_url, 2000)))
    # #queue.append(threading.Thread(target=xinghun,args=(blue_url,16000)))
    # #queue.append(threading.Thread(target=xinghun, args=(yellow_url,8000)))
    # queue.append(threading.Thread(target=xinghun, args=(purple_url,50)))
    # for t in queue:
    #     t.start()
    # for t in queue:
    #     t.join()


    # xinghun(blue_url,2000)
    # for t in queue:
    #     t.start()
    # queue[-1].join()
    # for i in range(20):
    #
    #     requests.post(trade_url)
    #     requests.post(yellow_url)
    #
    #     requests.post(purple_url)
    # trade_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246249389873"
    # for i in range(200):
    #     requests.post(trade_url)

    # r = requests.post(
    #     "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    #
    #
    # url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=essence_map&&m=pk&&d=newequip&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15542097741062&monster_id="
    # for j in range(1,4):
    #     for k in range(1, 4):
    #         for i in range(1,11):
    #
    #             requests.post(url + str(i)+"&id="+str(j)+"&diff_id="+str(k))
    # # url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=beauty&&m=conversion_chip&&token_uid=31973&token=eTUqRvGKyM0kQF1BNuXyYg&channel=9&lang=zh-cn&rand=1615098074&signature=9fc89675a7e0466d6c6dbf4d7a34c4b4&beauty_id=7"
    # # for i in range(45):
    # # #     requests.post(url)
    # zhangu_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=drum_forge&&m=go_sweep&&token_uid=31973&token="+content["token"]+"&channel=9&lang=zh-cn&rand=1619118946&signature=c5fa3bc3f15744220da4bf3c9e0553d5&materials_id=50&l={}&s={}&check=1"
    # for l in range(18, 20):
    #     for s in range(1, 8):
    #         requests.post(zhangu_url.format(l, s))
    # check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token="+content["token"]+"&channel=9&lang=zh-cn&rand=1619327579&signature=4c7e6040e5ffce732c4a33dedbf5cabd&l=20s=1"
    # zhangu_huangjiinurl = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=action&&token_uid=31973&token="+content["token"]+"&channel=9&lang=zh-cn&rand=1619119451&signature=3ea9458557058f122bdee856db05b525&l=20&s=1&times=5&id="
    # requests.post(check_url)
    # for i in range(1, 8):
    #     requests.post(zhangu_huangjiinurl + "i")
    # baowulianhua(content)
    # for i in range(100):
    #     file_appender = open("password/password"+str(i)+".txt", "w")
    # token = content['token']
    # queue = []
    # for i in range(100):
    #     queue.append(threading.Thread(target=join_jade_room, args=(token, i)))
    # for t in queue:
    #     t.start()
    # for t in queue:
    #     t.join()
    # join_room(token, 0)
    #check_omitted(content['token'])




        