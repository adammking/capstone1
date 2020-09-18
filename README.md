##First Capstone Project 

This website was built to provide information and assistance with depression. It is deployed through heroku and can be accessed through the link below. 

Link: https://capstoneone.herokuapp.com/
 

###Installation

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb capstone1`
5. `flask run`


###Features

- Community
	- Community provides people with the opportunity to create a profile and create posts to talk about issues or skill that help them manage their symptoms.
 
- Crisis
	- The crisis program will ask three questions, and based on the responses, will provide referrals for assistance, or coping skills to help reduce crisis symptoms.

- Cheer me up
	- Cheer me up utilizes the API's listed below to provide various distractions and humor for people. 

- Info
	- The info page offers information on depression along with a list of resources that can be utilized for assistance and treatment.  

###API's Utilized
Jokes API: 
https://icanhazdad1joke.com/

Cats API:
https://api.thecatapi.com/v1/images/search?limit=30

Dogs API: 
https://dog.ceo/api/breeds/image/random

###Roadmap for future

In the future I would like to get a database of all of the local mental health centers in every state in the U.S along with their contact information. I would also like to continue adding features to the community page (likes, comments on posts, messages) so users would be able to have more interaction with each other. Eventually I would also like to have support for additional mental health issues and broaden the scope of the site beyond depression. 
