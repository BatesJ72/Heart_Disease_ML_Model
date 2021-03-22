# Heart Disease Machine Learning Project

This is a project we built to help someone self-diagnose their risk of developing heart disease. The website associated with this repo is: https://heart-disease-risk.herokuapp.com/

On the site, the user answers the questions with their information, which is all information they could gather from at home tests, and the model tells them if they are at risk of developing heart disease or not. An interesting thing we noticed was that age is one of the most impactful factors - being older is worse for your health than high cholesterol! 

After comparing decision trees, logistic regression, and random forests, we determined that a random forest model performed the best. We used a pipeline for the categorical features (sex, exercise induced angina, chest pain type, and fasting blood sugar) , created 10,000 trees (the default was only 100), and used criterion of gini over entropy. With these settings, the random forest model scored in the mid to upper 70s overall. While the logistic model had a slightly higher accuracy score (0.77 vs 0.76), the holistic view of the models led to the random forest being the superior one.

This dataset contains the medical records of 299 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical features. We decided to select only 8 of the features. The 4 features that we eliminated required a doctor’s interpretation of test results that could not be obtained outside of a lab, and we wanted to build something people could use as an at home diagnostic tool.
The data is balanced regarding the target (160 people did not have heart disease, and 137 did), and there is a standard distribution around age 60.
