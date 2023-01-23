import json 
from urllib import request
from bs4 import BeautifulSoup




def length(data):
    return len(data)

def extract_title(url):
    try:
        html = request.urlopen(url,timeout=5).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')
        return title.string

    except:
        pass
    

def tokenized_title(title,count_response):
    try:
        count_response+=1
        return title.split()
    except:
        print("There is no title!")

def token_dictonnary(title,dictonnary,count,count_response):
    token_liste=tokenized_title(title,count_response)
    try:
        for token in token_liste:
            sub_count=0
            if token in dictonnary.keys():
                if str(count) in dictonnary[token].keys():
                    dictonnary[token][str(count)]+=1
                else:
                    dictonnary[token][str(count)]=1
            else : 
                sub_dic={}
                dictonnary[token]=sub_dic
                dictonnary[token][str(count)]=1

    except :
        print("There is no token!")
    



def create_reversed_index(link):
    f=open(link)
    data=json.load(f)
    dic={}
    count=0
    count_response=0
    for line in data:
        print(line)
        count+=1
        title=extract_title(line)
        token_dictonnary(title,dic,count,count_response)


    with open("index.json", "w",encoding='utf8') as fp:
        json.dump(dic,fp,ensure_ascii=False)








if __name__=="__main__":
    create_reversed_index("crawled_urls.json")

