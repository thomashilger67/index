import json 
from urllib import request
from bs4 import BeautifulSoup



class index:
    def __init__(self,link):
        self.path=link
        self.data=json.load(open(self.path))
        self.count_response =0
        self.index={}
        self.count=0

    def extract_title(self,link):
        """
        Extrait le titre du corps html 
        """
        try:
            html = request.urlopen(link,timeout=5).read().decode('utf8')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('title')
            return title.string

        except:
            pass 
        

    def tokenized_title(self,title):
        """
        tokenise le titre du document 
        """
        try:
            self.count_response+=1
            return title.split()
        except:
            print("There is no title!")

    def token_dictonnary(self,title):
        """
        crée un index sous forme de ditoinnaire avec, pour chaque token unique, le nombre de fois où il apparaît dnas le titre du document.
        """
        token_liste=self.tokenized_title(title)
        try:
            for token in token_liste:
        
                if token in self.index.keys():
                    if str(self.count) in self.index[token].keys():
                        self.index[token][str(self.count)]+=1
                    else:
                        self.index[token][str(self.count)]=1
                else : 
                    sub_dic={}
                    self.index[token]=sub_dic
                    self.index[token][str(self.count)]=1

        except :
            print("There is no token!")
        



    def create_reversed_index(self):
        """création de l'index avec comme ensemble de départ l'ensemble de la base de donnée."""
        for line in self.data:
            print(line)
            self.count+=1
            title=self.extract_title(line)
            self.token_dictonnary(title)


        with open("title.non_pos_index.json", "w",encoding='utf8') as fp:
            json.dump(self.index,fp,ensure_ascii=False)
        
        
    def stat_length(self):
        """
        Nombre d'url disponible
        
        """
        return len(self.data)
        
    def stat_length_token(self):
        """
        Nombre de token unique après avoir tokensier l'ensemble de la base de données.
        """
        return len(self.index.keys())

    def stat_length_repsonse(self):
        """
        Nombre de document réellement disponible. Les sites n'ayant pas de titre où renvoyant une erreur 403 "problème de sécurité" 
        n'ont pas répondu et ne sont donc pas indexés.
        """
        return self.count_response

    def stat_mean(self):
        """
        moyenne de token par document
        
        """
        num=self.stat_length_token()
        denom=self.stat_length_repsonse()
        return num/denom

    def stat_export(self):
        """
        export des résultats statistiques dans un json
        """
        dic_stat={}
        dic_stat["nombres de documents"]=self.stat_length_repsonse()
        dic_stat["nombre de tokens"]=self.stat_length_token()
        dic_stat["moyenne des tokens par document"]=self.stat_mean()

        with open("metadata.json","w", encoding="utf8") as fp:
            json.dump(dic_stat,fp,ensure_ascii=False)
