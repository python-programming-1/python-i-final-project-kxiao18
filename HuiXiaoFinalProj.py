# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:52:58 2019

@author: karen(hui) xiao
"""
import csv


'''Component 1
-Import data, remove unnecessary columns '''

def get_app_data():
    app_list = []
    app_dict = {}
    with open('AppleStore.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for column in spamreader:
            app_dict = {'Genre': column[12],
                        'app_id': column[1],
                        'app_name': column[2],
                        'total_ratings': column[6]}
            app_list.append(app_dict)
            app_dict = {}
    del app_list[0]
    return app_list



'''Component 2
-create a new dict stores the max rated app in every genre
-keys are the Genre names, and the values are total_ratings, app_id, and app_name'''
def get_max_rated():
    most_rated_app_in_genre = {}
    for i in get_app_data():   
        if i['total_ratings'].isdigit() and i['Genre'][0].isdigit() == False:
            most_rated_app_in_genre.setdefault(i['Genre'], {'total_ratings':0})
            if int(i['total_ratings']) > int(most_rated_app_in_genre[i['Genre']]['total_ratings']):
                most_rated_app_in_genre[i['Genre']]['total_ratings'] = int(i['total_ratings'])   
                most_rated_app_in_genre[i['Genre']]['app_id'] = i['app_id']
                most_rated_app_in_genre[i['Genre']]['app_name'] = i['app_name']
    return(most_rated_app_in_genre)
    


'''Component 3
-a. use google library to return the first resulted link
    -used this method because the tag in 'google.com' changes when opened in Python
-b. scrap more information on itunes.apple.com about the app
    -additional info includes: current rank, app seller, seller website, and seller app preview
-c. writes the additional info into a new csv file
'''

from googlesearch import search
import requests
from bs4 import BeautifulSoup 


def getFirstURL():
    
    filename = "mostRatedApp.csv"
    f = open(filename,'w', encoding='utf-8')
    headers = "app_id, app_name, current_rank, app_seller, sellerAppPreview, sellerWebsite\n"
    f.write(headers)
   
    for i in (get_max_rated()).values(): 
        app_id=' itunes app store ' + (str(i['app_id'])) 
        for x in search(app_id,start=0, stop=1, pause=2): 
            googleurl = x
            res2 = requests.get(googleurl)
            res2.raise_for_status()
            res2.close()
            soup_2 = BeautifulSoup(res2.text, 'html.parser')


        currentRank = soup_2.find('li', class_ = 'inline-list__item').get_text("|", strip=True)  

        sellerResult = soup_2.find('dd', class_='information-list__item__definition l-column medium-9 large-6').get_text("|", strip=True)

        sellerWebsite = soup_2.find('a', class_ = 'link icon icon-after icon-external')   
        sellerWebsiteLink = sellerWebsite.get('href')    
 

        sellerAppPreview = soup_2.find('h2', class_ = 'product-header__identity app-header__identity')   
        sellerAppPreviewLink = sellerAppPreview.a.get('href')

        f.write((str(i['app_id']))  + "," + (str(i['app_name']))  + "," + currentRank + "," +sellerResult + ","+sellerWebsiteLink +"," +sellerAppPreviewLink +"\n")
    f.close()
    








                
           
            
            
            
            
            
