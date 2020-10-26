# Predicting the cost of a car based on its characteristics, description, and photos.
**Training project within the Data Science specialization of the SkillFactory school**

The task is to create a model that will predict the cost of a car based on various 
types of data (table data, text, images). If the model works well, the customer will be 
able to quickly identify profitable offers (when the seller's desired price is lower than 
the predicted market price), which will significantly speed up the work of managers and increase 
the company's profit.

MAPE was chosen as the quality metric.

General pipeline of the project:
+ We will conduct EDA and work on the features.
+ Building a classic model based on gradient boosting using CatBoost.
+ We make a second model based on neural networks and compare the results.
+ Let's create a multi-input neural network for analyzing table data and text simultaneously.
+ Adding image processing to the multi-input network
