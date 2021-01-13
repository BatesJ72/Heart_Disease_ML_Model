library(rpart)
library(MASS)

names(heart_disease_data)

# Plotting (Instructor)
# scatter plot of horsepower on miles per gallon
plot(
  heart_disease_data$chol,
  heart_disease_data$sex,
  col="red",
  main="Chol by Sex",
  xlab="Chol",
  ylab="Sex",
  pch=20
)


plot(heart_disease_data)



for (name in names(heart_disease_data)){
  hist(
    heart_disease_data[, name],
    main=paste("Histogram of ", name, sep = ""),
    xlab=name,
    col="red"
  )
}


# make a function to split the data into a training set and a validation set
test_train_split = function(data, test_size=.25){
  
  # the the number of observations in the data
  n_obs = dim(data)[1]
  
  # find the number of training observations by rounding up
  n_train_obs = ceiling(n_obs * (1 - test_size))
  
  # get the train indexes
  train_idx = sample(n_obs, n_train_obs)
  
  # split the data
  train = data[train_idx, ]
  test = data[-train_idx, ]
  
  # return the result
  result = list(train, test)
  return(result)
}

# write a function to calculate the MSE
calc_MSE = function (model, data){
  return (
    mean(
      (data$medv - predict(model, data)) ^ 2
    )
  )
}

# see a summary of the squirrel data
summary(heart_disease_data)


# plot the boston data
plot(heart_disease_data)

# split the data
set.seed(1)
result = test_train_split(heart_disease_data)
train = data.frame(result[1])
test = data.frame(result[2])

# train a decsion tree and show results
tree_unpruned = rpart(medv ~ ., data=train)
summary(tree_unpruned)

# plot the unpruned tree
plot(tree_unpruned)
text(tree_unpruned)




# Multivariate Linear Regression
# More than one regressor


# fit the univariate model
lm_univariate = lm(chol~sex, data=heart_disease_data)

# fit a linear model of horsepower and weight on mpg
lm_multivariate = lm(chol~sex + fbs, data=heart_disease_data)

# see the details of the model
summary(lm_multivariate)

# show the diagnostic plots
par(mfrow=c(2, 2))
plot(lm_multivariate)

# fit a linear model of every varialble on mpg
lm_kitchen = lm(sex ~ ., data=heart_disease_data)

# see the details of the model
summary(lm_kitchen)

# do an F-test comparing the kitchen sink to the multivariate model
anova(lm_kitchen, lm_multivariate)

# fit a linear model of horsepower, displacement and their interaction on mpg
lm_interaction = lm(mpg ~ hp * disp, data=heart_disease_data)

# see the details of the model
summary(lm_interaction)

# do an F-test comparing the model to the multivariate one
anova(lm_interaction, lm_multivariate)

# do an F-test comparing the model to the univariate one
anova(lm_interaction, lm_univariate)

# show the diagnostic plots
par(mfrow=c(2, 2))
par(mar=c(1,1,1,1))
plot(lm_interaction)

# fit the model regressing horsepower and it square on mpg
lm_quadratic = lm(mpg ~ poly(hp, 2), data=heart_disease_data)

# show some details of the quadratic model
summary(lm_quadratic)

# use an F-test to compare the univariate and quadratic models
anova(lm_quadratic, lm_univariate)

# fit the cubic model of horsepower on mpg
lm_cubic = lm(mpg ~ poly(hp, 3), data=heart_disease_data)

summary(lm_cubic)

# use an F-test to compare the cubic and quadratic models
anova(lm_cubic, lm_quadratic)

# show the diagnostic plots for the quadratic model
par(mfrow=c(2, 2))
par(mar=c(1,1,1,1))
plot(lm_quadratic)

