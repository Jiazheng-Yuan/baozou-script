import requests
import json

import time


def lottery_rank(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=springlottery&&m=index&&token_uid=31973&token=" + content['token'] + "&channel=9&lang=zh-cn&rand=155099070112696"
    while True:
        r = requests.post(url)
        content = json.loads(r.content)
        userlist = content['userlist']
        if len(userlist) == 3:
            break
    # print(len(userlist))

    url_lottery = "http://s32.game.baozouwushuang.com/index.php?v=0&c=springlottery&&m=action&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099234854935"
    # print(r.content[])
    requests.post(url_lottery)
def silver_hole(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=island&m=pk&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155099000816495&id="
    for i in range(84,86):
        requests.post(url + str(i))
    url += "85"
    for i in range(17):
        re = requests.post(url)#silver hole
        #print(re.content)
def sign_in(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=sign&&m=sign_index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099296558640"
    r = requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=logined&m=get_reward&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132492285595&id=15"
    requests.post(url)
def donate(content,times):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=donate&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099312403245&type=1"
    for i in range(times):
        #pool.apply_async(requests.post, [url])
        requests.post(url)
def sacfirice_for_nation(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=countrysacrifice&m=action&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099341822220&id=1"
    r = requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=country&&m=get_salary&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102761189739"
    requests.post(url)
def business(content):
    token = content['token']
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=business&&m=index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099586487582"
    re = requests.post(url)
    content = json.loads(re.content.decode())
    traders = content['trader']

    #url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=business&m=go_business&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099356533783&id=6"
    #for i in range(80):
    #re = requests.post(url)
    #content = json.loads(re.content.decode())

    while True:
        trader_id = str(traders[0]['id'])
        #print(trader_id)
        url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=business&m=go_business&token_uid=31973&token=" + \
              token + "&channel=9&lang=zh-cn&rand=155099356533783&id="+trader_id
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
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=countrymine&&m=index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099446630583"
    re = requests.post(url)
    response_content = json.loads(re.content.decode())
    user_list = response_content['list']
    time = response_content['log']['times']
    if time > 1:
        pass
    return response_content
def shenjiangzhimen(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=generaltask&m=action&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099655983030&id=399&type=0&gid=362120"
    for i in range(10):
        requests.post(url)
def hero_throne(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=herothrone&&m=index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155176609795753"
    requests.post(url)
    for i in range(4):
        try:
            url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=herothrone&&m=start&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102736139239"
            requests.post(url)
        except:
            return
        url_391 = "http://s32.game.baozouwushuang.com/index.php?v=0&c=herothrone&&m=action&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155099683928379"
        #url_392 = "http://s32.game.baozouwushuang.com/index.php?v=0&c=herothrone&&m=action&&token_uid=31973&token=FJ8ZTtOt96no73HhibG9mQ&channel=9&lang=zh-cn&rand=155099693188373"
        for i in range(10):
            re = requests.post(url_391)
            print(json.loads(re.content.decode()))
        #print(json.loads(re.content.decode()))
def dice(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=dice&&m=shake_dice&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102770131520"
    for i in range(7):
        requests.post(url)
def jianghunxinglu(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=tower&m=get_mopup_price&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102830162193&id=118"
    re = requests.post(url)
    condition = json.loads(re.content.decode())
    if int(condition['info']['ten_sub']) == 0:
        url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=tower&m=mop_up&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102790179643&id=118&times=10"
        re = requests.post(url)
        #print(re.content)

def atk_roll(content):
    check_status_url_pre = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=mission&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155102870704658&"

    necessary_pre_check_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155103095467635"
    battle_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=action&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155103095467635&"#l=18&s=1&id=8&times=5"
    map_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15510326043749"
    for l in range(17,19):
        for s in range(1,8):
            map_param = "&l="+str(l)+"&s="+str(s)
            requests.post(map_url+map_param)
            for id in range(6,7,2):
                params = "l="+str(l)+"&s="+str(s) + "&id="+str(id)
                check_status_url = check_status_url_pre + params
                condition = json.loads(requests.post(check_status_url).content.decode())
                nowmaxtimes = int(condition['info']['nowmaxtimes'])
                if nowmaxtimes > 0:
                    #re = requests.post(necessary_pre_check_url)
                    #print(json.loads(re.content.decode()))
                    battle_params = "l="+str(l)+"&s="+str(s)+"&id="+str(id)+"&times="+str(nowmaxtimes)
                    true_battle_url = battle_url+battle_params
                    #print(true_battle_url)
                    requests.post(true_battle_url)
                    #print(json.loads(re.content.decode()))

    param = []

def jewel(content) :
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=sanctum&m=action&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132506502966&id=250&times=1"
    for i in range(10):
        requests.post(url)
def tongtianta(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=heaven&m=mop_up&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132527649516&id=177&times=10"
    requests.post(url)
def shenzhu(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15513239203246&times=5&monster_id=6&diff_id=3&id=3"
    requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15513239203246&times=5&monster_id=10&diff_id=3&id=3"
    requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132427716932&id=1&diff_id=3&monster_id=10&times=5"
    requests.post(url)
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=copies&m=mop_up&d=newequip&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132427716932&id=1&diff_id=3&monster_id=6&times=5"
    requests.post(url)
def daily_lottery(content):
    url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=lottery&&m=action&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155132452941485"
    for i in range(7):
        requests.post(url)

def xiaohao():
    password = "zzz2012123"
    usr = "zzz2012123"
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)

    check_status_url_pre = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=mission&token_uid=31973&token=" + \
                           content['token'] + "&channel=9&lang=zh-cn&rand=155102870704658&"

    necessary_pre_check_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token=" + \
                              content['token'] + "&channel=9&lang=zh-cn&rand=155103095467635"
    battle_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=action&token_uid=31973&token=" + content[
        'token'] + "&channel=9&lang=zh-cn&rand=155103095467635&"  # l=18&s=1&id=8&times=5"
    map_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token=" + \
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
    check_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=flop&&m=index&&token_uid=31973&token=3Bx_0YOTbrWYQ9dPC4_jOg&channel=9&lang=zh-cn&rand=155655985061498"
    flop_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=flop&&m=turnover&&token_uid=31973&token=3Bx_0YOTbrWYQ9dPC4_jOg&channel=9&lang=zh-cn&rand=155655979346793&id=5"
    response = json.loads(requests.post(check_url).content.decode())
    response = json.loads(requests.post(check_url).content.decode())
    for key,item in response.items():
        if key == "box_reward":
            for i in item:
                print(i)
        print(key,item)

    response = json.loads(requests.post(flop_url).content.decode())
    print(response)


def fukuang_harvest(content):
    for i in range(1,10):
        spot_num = i
        collect_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=harvest_mine&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15565919538656&s=" + str(spot_num)
        response = json.loads(requests.post(collect_url).content.decode())
        print(response)
def fukuang_available_spots(content):
    check_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155680885761671&p="
    available_spots = []
    for p in range(1,6):
        response = json.loads(requests.post(check_url+str(p)).content.decode())
        for spot in response['list']:
            if str(spot['status']) == '0':
                available_spots.append([str(spot['page']),str(spot['id']),str(spot['type'])])
    return available_spots

    p= 1
    id= 1
    t= 1
    formdata = "&p="+str(p)+"&id="+str(id) + "&t="+str(t)
    take_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=action_mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=155659196548989"+formdata
# response = requests.post("http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=15565922387968&p=3")
    # content = json.loads(response.content.decode())
    # for key,item in content.items():
    #     if key == "list":
    #         for i in item:
    #             print(i)
    #     else:
    #         print(key,item)
def lianxiaohao():
    for i in range(2,3):
        click = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=map&&m=mission&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659926245678&l=1&s=1&id="+str(3)
        requests.post(click)

    battle = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    get_mission_list = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    index = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=member&&m=index&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=15565993617769"
    hit = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=map&&m=action&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659897286217"

    update_guide = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=member&&m=updateguidestep&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659867833050"
    mission_list = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=map&&m=get_mission_list&&token_uid=6823695&token=ExOaFJpFZIWFzY8p4q7BHw&channel=1&lang=zh-cn&rand=155659942527825"
    pool = [click,get_mission_list,index,hit,update_guide,index,mission_list]
    for url in pool:
        response = requests.post(url)
        content = json.loads(response.content.decode())
        for key,item in content.items():
            print(key,item)
    # r = requests.post(
    #     "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    #
    # check_status_url_pre = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=mission&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155102870704658&"
    #
    # necessary_pre_check_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=member&&m=index&&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155103095467635"
    # battle_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&m=action&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=155103095467635&"  # l=18&s=1&id=8&times=5"
    # map_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=map&&m=get_mission_list&&token_uid=31973&token=GghT-JRKpcWSBUo5BoPvHw&channel=9&lang=zh-cn&rand=15510326043749"
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
def get_content(password,user):
    r = requests.post(
        "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content

def get_available():
    content = get_content('123456', "buwzzxh52")
    return fukuang_available_spots(content)

def occupy_fukuang():
    userprefix = "buwzzxh"
    password = "123456"
    user_info = [[password,userprefix + str(j)] for j in range(1,3)] + [[password,userprefix + str(j)] for j in range(51,86)]
    spots = get_available()
    for i in range(len(user_info)):
        #if i >= len(spots):
        #    break

        p = spots[i][0]
        id =spots[i][1]
        t = spots[i][2]
        formdata = "&p="+str(p)+"&id="+str(id) + "&t="+str(t)
        content = get_content(user_info[i][0],user_info[i][1])
        take_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=action_mine&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=155659196548989"+formdata

        response = json.loads(requests.post(take_url).content.decode())

        print(response)
        print(user_info[i])

def harvest():
    userprefix = "buwzzxh"
    password = "123456"
    for i in range(51,86):
        fukuang_harvest(get_content(password,userprefix + str(i)))
    for i in range(1,6):
        fukuang_harvest(get_content(password,userprefix + str(i)))
def check_lottery_list():
    checkurl = "http://s32.game.baozouwushuang.com/index.php?v=undefined&c=springlottery&&m=index&&token_uid=31973&token=5Fwn1RVD45EzUNU2efCSuw&channel=1&lang=zh-cn&rand=155716722639280"
    response = json.loads(requests.post(checkurl).content.decode())
    while 'userlist' in response and len(response['userlist'])!=3:
        response = json.loads(requests.post(checkurl).content.decode())
    draw_url ="http://s32.game.baozouwushuang.com/index.php?v=undefined&c=springlottery&&m=index&&token_uid=31973&token=5Fwn1RVD45EzUNU2efCSuw&channel=1&lang=zh-cn&rand=155716722639280"
    if 'userlist' in response and len(response['userlist'])==3:
        requests.post(draw_url)

def longzhou(token):
    start = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=go_boat&&token_uid=6826319&token="+token+"&channel=1&lang=zh-cn&rand=156988429136212"
    response = json.loads(requests.post(start).content.decode())
    print(response)
    direction = response['direction']
    for i in range(9):
        print("ere")
        direction_answer = "%2C".join([str(dir) for dir in direction])
        rowing_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=rowing_boat&&token_uid=6826319&token="+token+"&channel=1&lang=zh-cn&rand=156988432015486&list="+direction_answer
        resp = json.loads(requests.post(rowing_url).content.decode())
        print(resp)
        refresh_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=boat_index&&token_uid=6826319&token="+token+"&channel=1&lang=zh-cn&rand=156988432072668"
        new_resp =  json.loads(requests.post(refresh_url).content.decode())
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
                                                                          range(51, 86)]#86
    for i in range(len(user_info)):

        content = get_content(user_info[i][0], user_info[i][1])
        token = content['token']
        yuanbao_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=actjubao&&m=action&&token_uid=31973&token=" + token + "&channel=9&lang=zh-cn&rand=157732067703616&type=1"
        requests.post(yuanbao_url)
        print(user_info[i])
        if buy == "buy":
            buytimes = "http://bzws-s32.game.zhanyougame.com/index.php?v=undefined&c=go_boating&&m=buy_time&&token_uid=31973&token="+token+"&channel=1&lang=zh-cn&rand=156986608815118"
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
    content = get_content("yjz2012123","yjz2012123")
    token = content['token']
    harvest_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=harvest&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=157988700903840&id=1"
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
    check_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=occupy_list&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=157988860002249&id=1"
    res = json.loads(requests.post(check_url).content.decode())
    harvest_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=harvest&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=157988700903840&id=1"
    requests.post(harvest_url)
    for val in res["list"]:
        if val["country"] == "jiaz":
            rob_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=newyear_act&&m=rob&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=157988813627385&cid=1&id="+str(val["id"])
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
    #url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=ladder_war&&m=ladder_battle&&token_uid=31973&token="+get_content("yjz2012123","yjz2012123")["token"]+"&channel=9&lang=zh-cn&rand=158037374341422&id=3"
    #threading.Thread(target=requests.post,args=(url,))
    requests.post(url)
if __name__ == "__main__":
    #content = get_content( "123456","buwzzxh53")
    #arena_jifen_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=arena&&m=get_reward&&token_uid=31973&token=" + content['token'] + "&channel=9&lang=zh-cn&rand=156255546745079"
    #print(requests.post(arena_jifen_url).content.decode())
    #token = get_content("123456","buwzzxh52")["token"]
    #longzhou(token)


    #all_longzhou()
    #all_longzhou()
    #xinnian_rob()
    #all_longzhou("buy")
    #xiaohao_donation()
    # all_longzhou("buy")

    #response = requests.post("http://s32.game.baozouwushuang.com/index.php?v=0&c=worldboss&&m=battle&&token_uid=31973&token=FS5ybWAd6z6nnApI33oYJg&channel=9&lang=zh-cn&rand=15600525866585&now=0")
    #response = json.loads(response.content.decode())
    #print(response)
    #check_lottery_list()

    #harvest()
    #occupy_fukuang()
    #lianxiaohao()
                    # print(json.loads(re.content.decode()))

    # r = requests.post(
    #  "http://s32a.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    # donate(content,2200)
    #for i in range(26):
    #    chaogong("a")
    # response = requests.post("http://s32.game.baozouwushuang.com/index.php?v=0&c=fukubukuro&&m=mine&&token_uid=31973&token=GotTWqgn3UIeryJn-jhBsA&channel=9&lang=zh-cn&rand=15565922387968&p=3")
    # content = json.loads(response.content.decode())
    # for key,item in content.items():
    #     if key == "list":
    #         for i in item:
    #             print(i)
    #     else:
    #         print(key,item)
    #login

    # r = requests.post("http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
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



    yellow_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246113594820&refine_type=1&id=2"
    blue_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246130416038&id=1&refine_type=1"
    purple_url  = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246130416038&id=3&refine_type=1"
    trade_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token=FfoBJfdZqVuLB6Ck8ehcfw&channel=9&lang=zh-cn&rand=155246249389873"
    for i in range(20):

        requests.post(trade_url)
        requests.post(yellow_url)


        requests.post(purple_url)
    """

    # token = get_content("yjz2012123","yjz2012123")['token']
    # yellow_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246113594820&refine_type=1&id=2"
    # blue_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246130416038&id=1&refine_type=1"
    # purple_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=star&m=refining&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246130416038&id=3&refine_type=1"
    # trade_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246249389873"
    # def xinghun(url,time):
    #     q = []
    #     for i in range(time):
    #
    #         q.append(threading.Thread(target=requests.post,args=(url,)))
    #         q[-1].start()
    #     for t in q:
    #         t.join()
    # queue = []
    # queue.append(threading.Thread(target=xinghun,args=(blue_url,3200)))
    # queue.append(threading.Thread(target=xinghun, args=(yellow_url,800)))
    # queue.append(threading.Thread(target=xinghun, args=(purple_url,200)))
    # #queue.append(threading.Thread(target=xinghun, args=(trade_url, 2000)))
    # for t in queue:
    #     t.start()
    # queue[-1].join()
    # for i in range(20):
    #
    #     requests.post(trade_url)
    #     requests.post(yellow_url)
    #
    #     requests.post(purple_url)
    # trade_url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=tavern&&m=trade_batch&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=155246249389873"
    # for i in range(200):
    #     requests.post(trade_url)

    # r = requests.post(
    #     "http://s32.game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u=yjz2012123&p=yjz2012123&adid&channel=9&token=")
    # content = r.content.decode()
    # content = json.loads(content)
    #
    # content = get_content("yjz2012123","yjz2012123")
    # url = "http://s32.game.baozouwushuang.com/index.php?v=0&c=essence_map&&m=pk&&d=newequip&&token_uid=31973&token="+content['token']+"&channel=9&lang=zh-cn&rand=15542097741062&monster_id="
    # for j in range(1,4):
    #     for k in range(1, 4):
    #         for i in range(1,11):
    #
    #             requests.post(url + str(i)+"&id="+str(j)+"&diff_id="+str(k))
    token = get_content("yjz2012123","yjz2012123")['token']
    for i in range(1,7):
        tree_index = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_tree&&m=index&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=158218185981691"
        tree_gather = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_tree&&m=gather&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=15821818285074&site={}".format(token,str(i))
        tree_occupy = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_tree&&m=action&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158218291970117&site={}".format(token,i)
        stone_index = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_stone&&m=index&&token_uid=31973&token="+token+"&channel=9&lang=zh-cn&rand=158218268718163"
        stone_gather = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_stone&&m=gather&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158218268673528&site={}".format(token,i)
        stone_occupy = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=exploit_stone&&m=action&&token_uid=31973&token={}&channel=9&lang=zh-cn&rand=158218299778325&site={}".format(token,i)

        requests.post(tree_index)
        requests.post(tree_gather)
        requests.post(tree_index)
        requests.post(tree_occupy)
        requests.post(stone_index)
        requests.post(stone_gather)
        requests.post(stone_index)
        requests.post(stone_occupy)


