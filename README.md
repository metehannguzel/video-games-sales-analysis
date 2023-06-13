# ABSTRACT

  In this report we will mention about codes and what we have done. In this project we use a dataset which includes 11563 unique values in different categories. We aim to make a prediction project which is going to predict video games’ global sales. We are going to predict video games’ global sales with three different ways. These are KNN Regressor, Linear Regression, and Decision Tree. Then, in the project, we talked about loading data, released games by year, sales analysis, sales distribution, distribution of sales by genre, sales distribution by ESRB rating and publisher analysis. We mentioned them step by step and showed the graphs for each topic by writing code in Python. Also we used Plotly library for data visualization. After that, based on the dataset, we created a system that will display the estimated values when new data is added. There are too many data in different categories. So for making categorization for new data we use KNN, Decision Tree and Linear Regression. KNN is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point. A decision tree is a type of supervised machine learning algorithm used to categorize or making predictions based on the previous data. Linear Regression is a machine learning algorithm based on supervised learning. It is mostly used for finding out the relationship between variables and forecasting.


## 1. INTRODUCTION

  In a year, many games of different genres are released in different regions by different people or companies. So , the goal of this project is , when someone or somebody make a decision to creating new game , they do not know how much they will earn. So with our project, each publisher will know roughly how much they will earn. In our project using knn, decision tree and linear regression, we show how much a newly released game will sell according to the place where it is released, the person who released it, the year it was released, and the platform it was released on. In this way, the person or people who will release the game see the estimated data before the game is out of the profit that the game will bring thanks to this project. We can also see the data visualization graphs for the video games.


## 2. GAME DEVELOPMENT PROCESS

  When a company decided to make a video game, they will spend money a lot. Because they will needlots of workers for each part of the game. Any game can be made by just a person but in this situation, the game will be released after too many years later. So companies should hire workers. While some games are made and presented in 1 month, some games take 4 years to make. Main reason of that is quaility of the some games affects time. After that time , companies release the games and sell to the users in some platforms but some games sell well and some games sell less. When game sell less , companies may suffer financial loss. Moreover some may even go bankrupt. So for that some programmers and us made this project. With this project compines may know how much money they will earn before the calculating the cost. Companies can easily calculate how much a new game will be sold by seeing how much a game is sold in which region, on which platform, in which category, and by looking at this dataset(). In this way, companies calculate the company's earnings and expenses before starting the production of a game. Over the years, the game industry has been developing a lot and companies are trying to keep up with this development.


## 3. RELEASE OF THE GAME

  While companies are making the game, they announce the game that will be released after a certain period of time. This creates a curiosity on the players and they wait for the release date of the game. The closer to the specified date, the more the impact on the game will be, so the estimated sales data of the game will increase greatly. When the date comes, there is a great intensity in the game and users write their opinions about the game. Some famous players also promote the game if they like it. All these factors greatly affect how much the game will be sold.


## 4. ESTIMATED SALES DATA OF THE GAME

  The number of sales of the game depends on many factors. The number of sales depends on which platforms the game will be sold on, the advertisements of the game, which famous players the game has sponsorship agreements with, in which year it was released, how many users play the game, and so on. For these reasons, the number of sales of the game varies greatly. Events in the game and items for the game affect users, which contribute to the constant updating and growth of the game.


## 5. DATASET

  We are going to use a dataset which has 16719 rows and 16 columns. The columns are:

    Name – Name of the game
    Platform – Game console
    Year_of_Release – Year of the game’s release date
    Genre – Game type (action, sports, exc.)
    Publisher – Game studio
    NA_Sales – Sales in North America
    EU_Sales – Sales in Europe
    JP_Sales – Sales in Japan
    Other_Sales – Sales in other regions
    Global_Sales – Sales around the globe
    Critic_score – Aggregate score compiled by Metacritic staff
    Critic_Count – The number of critics used in coming up with the Criticscore
    User_Score – Score by Metacritic’s subscribers
    User_Count – Number of users who gave the userscore
    Developer – Party responsible for creating the game
    Rating – The ESRB ratings


## 6. REGRESSION

### 6.1 Decision Tree

  Decision Tree is a supervised learning technique that can be used for both classification and Regression problems . It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.

  In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. Decision nodes are used to make any decision and have multiple branches, whereas Leaf nodes are the output of those decisions and do not contain any further branches.

  The decisions or the test are performed on the basis of features of the given dataset.

  It is called a decision tree because, similar to a tree, it starts with the root node, which expandson further branches and constructs a tree-like structure.
  
  
## 6.2 K-Nearest Neighbors

  K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.

  K-NN algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.

  K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using KNN algorithm.

  K-NN algorithm can be used for Regression as well as for Classification.
  
  
## 6.3 Linear Regression

  Linear Regression is a supervised machine learning algorithm where the predicted output is continuous and has a constant slope. It’s used to predict values within a continuous range, (e.g. sales, price) rather than trying to classify them into categories.
