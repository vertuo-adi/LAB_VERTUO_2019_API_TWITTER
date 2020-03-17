# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
import os 
import pandas as pd


#Lecture des json 
df_all = pd.DataFrame() 
Dossier_tweet = [x for x in os.listdir("sure")]
for file_json in Dossier_tweet:
    tweets = []
    file = "sure/" + file_json 
    nom_requete = file_json [:-30]
    with open(file, 'r') as f:
        for line in f.readlines():
            tweets.append(json.loads(line))
    df = tweet_df(tweets)   
    df = df[['id_str','created_at','full_text','in_reply_to_status_id_str','retweet_count']]
    df['name_request'] = nom_requete
    df['begin_by_RT'] = df.full_text.map(lambda x: 1 if x.startswith('RT ') == True else 0)
    df['Tweet_natif_bq'] = df.full_text.map(lambda x: 1 if x.startswith('RT ' + nom_requete) == True else 0)
    frames = [df_all, df]
    df_all = pd.concat(frames)   

df_all = df_all.drop_duplicates(subset=['created_at','full_text','name_request'])
#Patch pour Carrefour banque 
df_all.at[df_all.full_text.str.contains('@CarrefourBanque'), 'name_request'] = '@CarrefourBanque'
df_all = df_all[df_all.name_request != '@CarrefourFrance']

emotes =  ['😀','😁','😂','🤣','😃','😄','😅','😆','😉','😊','😋','😎','😍','😘','😗','😙','😚','🙂','🤗','🤩','🤔','🤨','😐','😑','😶','🙄','😏','😣','😥','😮','🤐','😯','😪','😫','😴','😌','😛','😜','😝','🤤','😒','😓','😔','😕','🙃','🤑','😲','🙁','😖','😞','😟','😤','😢','😭','😦','😧','😨','😩','🤯','😬','😰','😱','😳','🤪','😵','😡','😠','🤬','😷','🤒','🤕','🤢','🤮','🤧','😇','🤠','🤥','🤫','🤭','🧐','🤓']
pattern = '|'.join(emotes)

df_with_emote = df_all[df_all['full_text'].str.contains(pattern)][['full_text','name_request']]
 
Res=pd.DataFrame()
for j in emotes :
    temp  = df_with_emote[df_with_emote['full_text'].str.contains(j)]
    temp = temp.groupby(['name_request']).size().reset_index(name='effec')
    temp['emote'] = j
    frames = [Res, temp]
    Res = pd.concat(frames) 

#Emotes à definir
only = Res[['emote']].drop_duplicates('emote')

Freq_emotes = pd.DataFrame()
Freq_emotes = Res.groupby(['emote']).size().reset_index(name='nb_occcurence')

#Affectation des catégories
categorie = pd.read_excel('emote_coresp.xlsx') 
Res = Res.merge(categorie, on='emote', how='left')
Freq_final = Res.groupby(['name_request','Categorisation']).sum().reset_index()






