# HELPIT

## Inspiration
Since we are nearing the end of mental health week, we felt that mental health is such an important topic with 
not a lot of small-scale resources. Therefore, we thought of making something that could help improve someone's 
quality of living through a website that leads you to self-evaluate.

## What it does
helpIt asks you questions to assess how you are feeling, followed by another question based on your answers, 
and so on. These questions are often thought provoking and lead you through a self evaluating journey to make a better you.

## How we built it
We found a dataset that can be used to categorize how a user feels based on their input. This training set 
uses machine learning algorithms to train the dataset and refine the classifier's execution. 
The classifier is used to make a token indicating what the user is feeling and choose the next question that needs to be asked accordingly.

## Challenges we ran into
This problem was quite challenging first we had to create multiple routes and manage them and provide them through the ngrok tunnel
such that the frontend can access without any issue. Then whenever the user submits his response it is classified using machineLearning
algorithm that tells us the user emotion and on that results we give them a new question that is completely based on their response.
For the Frontend the challenging part was to make multiple API calls using Axiom in React and State Management because whenever the user
submit the response for the question it goes to the backend gets proccessed and sends a new question that user has to answer. So by this way
we had to create multiple states and onClick functions that are interconnected and depends on one another that makes it really complex.

## Accomplishments that we're proud of
We're proud of being able to make a self-learning algorithm that can detect the emotions a person feels and accordingly
choose the question that best suits a person's mood.
 
## What we learned
We learnt how to make the most out of everyones strengths and weaknesses to successfully realize the project. 
As it was our first time machine learning and web development, some of us learnt how to incorporate machine learning 
in an efficient manner, while others learnt how to create a complex web interface for users to interact with. 
We are proud that we could produce such a project while realizing how important it is to never stop learning. 

## What's next for HelpIt?
We plan on adding more emotions, questions, and a few tips on where you can get started to lead a 
healthier life! All based on user inputs.


## Backend Routes
* tips
[Sample : localhost:5000/tips/allTips]
    (GET)
    * allTips - Retuns all the tips in the Database 
    * oneTip/<int:id> - Returns a particular tip based on the id value passed
    * randomTip - Returns a random tip from the Database
    * create - Returns a HTML webpage that can be used to add data to the database
    (POST)
    * create/process - only accepts post request to add data (do not use this) (Internal use only)

* goals
[Sample : localhost:5000/goals/allGoals]
    (GET)
    * allGoals - Returns all the goals in the database
    * oneGoal/<int:id> - Returns a particular goal based on the id value passed
    * randomGoal - Returns a random goal from the database
    * suggestedGoals/<string:userID> - Returns suggestedGoals based on the user prefered categories. 
                               	       userID is the unique ID given to user when adding to database
    * create - Returns a HTML webpage that can be used to add data to the database
    (POST)
    * create/process - only accepts post request to add data (do not use this) (Internal use only)

* question
    (GET)
    * allQuestions - Retuns all the questions in the Database 
    * oneQuestion/<int:id> - Returns a particular question based on the day value passed
    * randomQuestion - Returns a random tip from the Database
    * create - Returns a HTML webpage that can be used to add data to the database
    (POST)
    * create/process - only accepts post request to add data (do not use this) (Internal use only)

* user
    (GET)
    * get/<string:userID> - Get the user from the Database
    (POST)
    * add/ - accepts POST request and submit userInfo to Database

* getUserData (POST)
	Receives the Username and the password as POST request. If the user exists in the database
	it returns all the questions and answers he has answered such that he can continue from where
	he left. Or add the user to the database.

* submitUserData/<string:userID> (POST)
	Receives the userID in URL and User Question and his Response as a JSON body, parse it and 
	add to the respective user database

* machineLearning/<string:userID>
	Receives the userID on which the machineLearning will classify and process the response and 
	returns the output. Based on that output a new question is given back from the database that
	matches the response emotion as given by the user.

* finalResult/<string:userID>
	Sends the Final results of the user responses in a JSON format to the frontend.
