from urllib.request import urlopen

def a1():
    url='http://www.baidu.com'
    resp=urlopen(url)
    texts=resp.read().decode('utf-8')
    svs(texts)


def svs(filename):
    with open('opsc1/mybaidu.html',mode='w',encoding='utf-8') as f:
        f.write(filename)
        print('end!')

def main():
    a1()

if __name__=='__main__':
    main()

