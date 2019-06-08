# Python-I-Final-Project
Final Project by Karen(Hui) Xiao

* Commit and upload your final project using Github like previous homeworks. 
* Add instructions in this README.md file to demonstrate your project.
* We will demonstrate our projects on June 12, 2019. If you can't attend, I will try to run your program for the class.
* If the program does not run, I will have to deduct major points, so please make sure it runs!
* If I can't get it to run, I may reach out and ask you to fix your program. 

Overview:

-My project is called "Trendy Applications Hunter". I used the database from 'kaggles.com'(https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps). The databse contains a csv file, listing 16 attributes (e.g. app_id, app_name, genre, total_ratings, price, etc) of 7200 Applications from July 2017 Apple IOS store. \n
-My goal is to first find the most rated application for every genere, and then scrapping more information about the application from 'iTunes.com'. Finally I will write the additional information into a new csv file. 


Component 1:Import data, remove unnecessary columns\n
-a. the original csv file contains 16 columns, but I don't need that many,I only need 4 attributes: app_id, app_name, genre, and total_ratings\n
-b. I open and read the original table, and create a new empty list called 'app_list = []' to store only the needed columns

Component 2: Retrieve the most rated applications\n
-a. create a new dict stores the max rated app in every genre\n
-b. keys are the Genre names, and the values are total_ratings, app_id, and app_name

Component 3: web scrapping and writing into a file\n
-a. use google library to return the first resulted link
    -used this method because the tag in 'google.com' changes when opened in Python
-b. scrap more information on itunes.apple.com about the app
    -additional info includes: current rank, app seller, seller website, and seller app preview
-c. writes the additional info into a new csv file
    -the final output should be a csv file called 'mostRatedApp.csv' in the same folder of my working directory

**I ran the program and it work alright on my end. If the program crashes at the middle part where it scraps the website, maybe just try one more time.**

**Thank you!!***