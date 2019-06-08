# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:52:58 2019

@author: karen(hui) xiao
"""



'''Component 1
-Import data, remove unnecessary columns '''
import csv
#This method is to import the original csv data into a list of only 4 columns of interest 
def get_app_data():
    app_list = []
    app_dict = {}
    #because of coding is a bit different between Python and the database csv file, 
    #we have to add the encoding note
    with open('AppleStore.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for column in spamreader: 
            #the column numbers here correspond to the attribute column numbers in the csv file
            app_dict = {'Genre': column[12],
                        'app_id': column[1],
                        'app_name': column[2],
                        'total_ratings': column[6]}
            app_list.append(app_dict) #appending each datapoint to the list
            app_dict = {}
    del app_list[0] #because row 1 would be the headers, not the actual datapoints, we remove it
    return app_list

#call the fundtion to see if it works
'''uncomment to see the result,just testing, not mendatory'''
#get_app_data()

'''Component 2
-create a new dict stores the max rated app in every genre
-keys are the Genre names, and the values are total_ratings, app_id, and app_name'''
def get_max_rated():
    most_rated_app_in_genre = {} 
    #create another list to store only the most rated applications in each genre
    for i in get_app_data():   
        if i['total_ratings'].isdigit() and i['Genre'][0].isdigit() == False:
            #some datapoints were imported improperly with wrong columns being aligned,
            #so we elimiinate those datapoints by testing if the rating column is digital 
            #and if the genre column is not digital
            most_rated_app_in_genre.setdefault(i['Genre'], {'total_ratings':0})
            #if it passes, we assign the genre name and its starting total rating being 0
            if int(i['total_ratings']) > int(most_rated_app_in_genre[i['Genre']]['total_ratings']):
                #another iternation comparing the value of 'total_ratings'
                most_rated_app_in_genre[i['Genre']]['total_ratings'] = int(i['total_ratings'])   
                most_rated_app_in_genre[i['Genre']]['app_id'] = i['app_id']
                most_rated_app_in_genre[i['Genre']]['app_name'] = i['app_name']
    return(most_rated_app_in_genre) 
    
 #call the fundtion to see if it works   
#result should be only 1 application per genre
'''uncomment to see the result, just testing, not mendatory'''
#get_max_rated()

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
    
    #open a new file for writing 
    filename = "mostRatedApp.csv"
    f = open(filename,'w', encoding='utf-8')
    #new file has 6 headers/columns
    headers = "app_id, app_name, current_rank, app_seller, sellerAppPreview, sellerWebsite\n"
    f.write(headers)
   
    #use google library to return the first resulted link
    #should be 'iTunes.com...'
    for i in (get_max_rated()).values(): 
        #assigning values to keyword in the google search bar
        keyword=' itunes app store ' + (str(i['app_id'])) 
        for x in search(keyword,start=0, stop=1, pause=2): 
            googleurl = x
            #use 'requests' library to get to the website returned above
            res2 = requests.get(googleurl)
            res2.raise_for_status()
            res2.close()
            #use 'bs4' to start web scrapping
            soup_2 = BeautifulSoup(res2.text, 'html.parser')

        #scrapping the current rank of the application
        currentRank = soup_2.find('li', class_ = 'inline-list__item').get_text("|", strip=True)  
        
        #scrapping the application seller 
        sellerResult = soup_2.find('dd', class_='information-list__item__definition l-column medium-9 large-6').get_text("|", strip=True)

        #scrapping the seller website
        sellerWebsite = soup_2.find('a', class_ = 'link icon icon-after icon-external')   
        sellerWebsiteLink = sellerWebsite.get('href')    
 
        #scrapping the seller application preview at app store
        sellerAppPreview = soup_2.find('h2', class_ = 'product-header__identity app-header__identity')   
        sellerAppPreviewLink = sellerAppPreview.a.get('href')

        #writing the scrapping results into the new file
        f.write((str(i['app_id']))  + "," + (str(i['app_name']))  + "," + currentRank + "," +sellerResult + ","+sellerWebsiteLink +"," +sellerAppPreviewLink +"\n")
    f.close()
    
    
#call the last function
'''MENDATORY!!!'''
getFirstURL()







                
           
            
            
            
            
            
