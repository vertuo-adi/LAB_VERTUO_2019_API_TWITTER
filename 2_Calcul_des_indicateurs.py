# -*- coding: utf-8 -*-
import json
import os 
#os.chdir("D:/VERTUO\2019\LAB\data_intelligence\Perso")
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

#Construction de l'indicateur 1 : Tweet natif à récupérer avec les RT
pd_ind1 = df_all[df_all['Tweet_natif_bq']==1]
pd_ind1 = pd_ind1.drop_duplicates(subset=['full_text','name_request'])

Freq_ind1 = pd.DataFrame()
Freq_ind1 = pd_ind1.groupby(['name_request']).size().reset_index(name='Frequence_Ind1')
Freq_ind1['Pourcentage_Ind1'] = Freq_ind1['Frequence_Ind1'] / Freq_ind1['Frequence_Ind1'].sum() 
Freq_ind1 = Freq_ind1.sort_values('Frequence_Ind1', ascending = False )

#Construction de l'indicateur 2 : Tweet natif qui mentionnent le @
pd_ind2 = df_all[df_all['begin_by_RT']==0]
pd_ind2 = pd_ind2[pd_ind2['in_reply_to_status_id_str'].isnull()]

Freq_ind2 = pd.DataFrame()
Freq_ind2 = pd_ind2.groupby(['name_request']).size().reset_index(name='Frequence_Ind2')
Freq_ind2['Pourcentage_Ind2'] = Freq_ind2['Frequence_Ind2'] / Freq_ind2['Frequence_Ind2'].sum() 
Freq_ind2 = Freq_ind2.sort_values('Frequence_Ind2', ascending = False )

#Construction de l'indicateur 3 : parle-t-on d'eux en terme de retweet
pd_ind3 = df_all[df_all['begin_by_RT']==1]
pd_ind3 = pd_ind3.drop_duplicates(subset=['full_text','name_request'])
pd_ind3 = pd_ind3.sort_values('retweet_count', ascending = False )

Freq_ind3 = pd.DataFrame()
Freq_ind3 = pd_ind3.groupby(['name_request'])['retweet_count'].sum().reset_index(name='nb_retweet_tot')
Freq_ind3['Pourcentage_Ind3'] = Freq_ind3['nb_retweet_tot'] / Freq_ind3['nb_retweet_tot'].sum() 
Freq_ind3 = Freq_ind3.sort_values('nb_retweet_tot', ascending = False )

#Construction de l'indicateur 4 : parle-t-on d'eux en terme de non retweet tweet natif individuels et Reply
pd_ind4 = df_all[df_all['begin_by_RT']==0]
pd_ind4 = pd_ind4.drop_duplicates(subset=['full_text','name_request'])
pd_ind4 = pd_ind4.sort_values('retweet_count', ascending = False )

Freq_ind4 = pd.DataFrame()
Freq_ind4 = pd_ind4.groupby(['name_request']).size().reset_index(name='Frequence_Ind4')
Freq_ind4['Pourcentage_Ind4'] = Freq_ind4['Frequence_Ind4'] / Freq_ind4['Frequence_Ind4'].sum() 
Freq_ind4 = Freq_ind4.sort_values('Frequence_Ind4', ascending = False )

common = Freq_ind4.merge(Freq_ind3,on=['name_request'], how='left').merge(Freq_ind2,on=['name_request'], how='left').merge(Freq_ind1,on=['name_request'], how='left')
Resultat = common[['name_request','Frequence_Ind1','Frequence_Ind2','nb_retweet_tot','Frequence_Ind4']]







test = df_all[df_all['full_text'].str.contains('Revolut')]

test1 = test[test['created_at'].str.contains('May 23')]



