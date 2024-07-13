# Python-Twitter-Bot
Python Twitter Bot 

1. To use Twitter bot,you need to have Python 3 installed on your system.This bot uses tweepy module.You can install tweepy by using pip.To install tweepy, use this command :

 $ pip install tweepy

2. Now,you need to create a new application on Twitter. Either you can use your existing account or you can create a new one.Creating a new account for bot  is better so that your original Twitter account does not get banned.To create a new application on Twitter,open this URL in your browser :
 https://apps.twitter.com/

3. Fill all details required to create the new app.After that ,click on "Key and Access Token" tab under app settings.You will get your app's Consumer Key (API Key , Consumer Secret (API Secret) .You also need to get Access Token and Access Token Secret of your app.We will use these valuse in next step.You need to generate Access Token for first time.


4. Edit credentials.py and copy-paste  all your details carefully. Make sure the application has read and write settings turned on. 


5. Now,you can run  twitterbot_text.py file to run bot which will tweet The Zen of Python texts by using this command :


 $ python twitterbot_text.py 
 



6. Add tweet text in the sample.txt file with each tweet in new line. You can also use any file instead of sample.txt . To do that,you need to open twitterbot_text.py file and edit this line my_file=open('sample.txt','r') and enter your desired filename instead of 'sample.txt'.

7. Change the image path to point to the image that you want to publish with the tweet.

8. `tweet_text()` tweets text and `tweet_with_image()` tweets text with the image. 

9. You can also deploy Twitter bot on online based servers if you want to run the bot 24 hours continously.Take care of sleep/delay if you run bot the whole day.You should try to use large sleep time so that your account does not get banned.


