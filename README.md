### Project_4

# Music-Genre-Classification

## Table of Contents 

- Introduction
- Requirements 
- Objectives 
- Datasets 
- Technology used 
- Introduction
- Data and Models
- Data Preprocessing
- Classification
- Model Optimisation 
- Table summary of result after optimizing
- Result Visulisation Using Tableau
- Conclusion 



## Itroduction 

Companies nowadays use music classification, either to be able to place recommendations to their customers or simply as a product
Determining music genres is the first step in that direction. Machine Learning techniques have proved to be quite successful in extracting trends and patterns from a large data pool. The same principles are applied in Music Analysis also.

## Requirements
- Find a problem worth solving, analyzing, or visualizing
- Use ML in the context of technologies learned. 
- You must use Scikit-learn and/or another machine learning library
- You must use at least two of the below: Python Pandas 
    ****Python Pandas, Python Matplotlib, HTML/CSS/Bootstrap, JavaScript Plotly, JavaScript D3.js JavaScript Leaflet, SQL Database ,MongoDB Database, Google Cloud SQL Amazon AWS     or Tableau
 
 ## Objectives
 
 - This project is primarily aimed to create an automated system for classification model for music genres.
 - The objectives of music genre classification are as follows:
 - To extract the features from the given music.
 - To classify the input music based on the extracted features and label a class(genre) name to it.
 - To quantify the match of any input music to the listed genres.
 - To improve upon the accuracy of genre classification.


## Data and Models 

Our dataset is extracted frop Kaggle platform (GTAZAN Music classification Dataset)
 It contains 8 music genres: 
Rock, Folk, Experimental, Hip-hop, International, Pop, Instrumental,   Electronic 

![image 1](https://user-images.githubusercontent.com/83431185/137943140-2df9c8ca-c99e-42c5-b196-d1edbc8cdd84.png)


 It consists of 79. 994 audio tracks, and have a length of 30 seconds long each           
Approximately 10. 000 samples for each class 
58 Features (Numerical)
Meta Attribute (File name)                                     


The algorithms we applied for our data set are:

 - KNN (k-Nearest Neighbors)
 - Logistic Regression
 - Random Forest Classification
 

 ## Data Preprocessing
 
 
 For Music Genres Data, it is necessary to decide which of the 58 features are required for this supervised learning algorithm and which features are more effective because a    low quality dataset causes a low quality of accuracy.
So we decided to remove all the variance features so we reduced the number of features from 58 to 30
Drop unnecessary columns _id, filename.
Convert categorical genre target labels to integers 0 through 9 so that entire data set is numerical.

 
 ## Project Process Architecture 
 
 
 ![image](https://user-images.githubusercontent.com/83431185/137944744-0d77907b-cd90-41a1-939b-4eca594bf4a9.png)


## Classification 


- KNN model:


Separate feature data from target genre (column = label)
Split data into 75% training and 25% testing using sklearn.model_selection.train_test_split
Scaling data using StandardScaler.
Initializing the model and determining the best K value which is the number 3 and then refit the knn classifier by using this k value 

Result: ![image](https://user-images.githubusercontent.com/83431185/137945301-61709c49-934b-4387-bec1-2b9b9151a5d6.png)

![image](https://user-images.githubusercontent.com/83431185/137945457-4f22d45d-b474-4353-abf9-2cba41eb6df9.png)



- Random Forest Classification Model: 


Separate feature data from target genre (column = label)
Split data into 75% training and 25% testing using sklearn.model_selection.train_test_split
Scaling data using StandardScaler.
Initialize the model, training, prediction and determining the confusion matrix, then testing the accuracy.

    - Confusion matrix for RFC: 

![image](https://user-images.githubusercontent.com/83431185/137945829-edf69b9c-43f3-4ea2-a2fc-802004182e78.png)

 Result: 

 ![image](https://user-images.githubusercontent.com/83431185/137946428-2ee6c272-f2bc-4a0e-8f11-26ecff57fd94.png)
 
 
 - Logistics Regression Model
 
Separate feature data from target genre (column = label)
Split data into 75% training and 25% testing using sklearn.model_selection.train_test_split
Scaling data using StandardScaler.
Initialize the model, training, prediction and 
Determine the confusion matrix to evaluate the perfection of the classification model 

Result: 

   - Confusion Matrix Evaluation Metrics: 

 ![image](https://user-images.githubusercontent.com/83431185/137946875-bf3d323a-ae6b-46f5-bd15-6a17196ca2d7.png)

  - Score: 
  ![image](https://user-images.githubusercontent.com/83431185/137947052-a0d2e765-a9b3-4867-a0e0-01121557c869.png)

##  Optimisation models 

  In order to optimize our models we divided the the label classification into 4 binaries genres: 

 Pop$ Folk
 Hip-hop & Rock
 Instrumental & International
 Electronic & Experimental 

- Random Forest after Optimisation: 

The model is able to accurately recognize each binary genre music with recall values between 87% and 94%,  however the model is overtrained in each classification.


- Logistic Regression after Optimization:

The model is well performed using 2 genres rather than 8 

The model generated an accuracy between 83% and 84% for Hip-Hop/Rock binary and Instrumental/International however it is less adept at recognizing Folk/Pop and electronic/Experimental with a testing score between 75% and 76% .


##  Table summary of result after optimizing 

![image](https://user-images.githubusercontent.com/83431185/137949582-ff4aa08f-b526-4209-acf0-501ac54e5011.png)

## Result Visualisation using Tableau

![image](https://user-images.githubusercontent.com/83431185/137948242-89690de9-2f03-4dbf-942d-7b9844683df0.png)
![image](https://user-images.githubusercontent.com/83431185/137948276-ad194d69-8658-4f2c-826e-3302d4b071d1.png)
![image](https://user-images.githubusercontent.com/83431185/137948307-62cec275-e2de-4e8e-940b-a663153ed08e.png)


## Conclusion 

We have tried various machine learning algorithms for this project. Our aim is to get maximum accuracy. We found from our research that we can get maximum accuracy of 96% model with 2 genre classes but for the web application we decided to use the K-nearest neighbor since it was able to recognise all the genres with a good accuracy of 82%. 

Link to web app : https://ak-project4.herokuapp.com/

Presetation : https://docs.google.com/presentation/d/10A28XM4cztSf64swjDU4QkRiD4ExW76fUu_sCk6S6OM/edit#slide=id.gf99ae8e458_0_96

## Some References 
 
1.	https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
2.	https://www.freecodecamp.org/news/how-to-deploy-an-application-to-heroku/
3.	https://data-flair.training/blogs/python-project-music-genre-classification/#google_vignette
4.	https://www.kaggle.com/lakshyagupta/music-genre-prediction
5.	https://www.analyticssteps.com/blogs/music-genre-classification-using-machine-learning
6.	https://dev.to/hackersandslackers/connect-flask-to-a-database-with-flask-sqlalchemy-5d15#:~:text=%20Connect%20Flask%2[…]0our%20database...%20More%20
7.	https://www.youtube.com/watch?v=6wojjJoRxRM


