# Read in the data
heart = read.csv("heart_disease_data.csv")

# Explore the data
names(heart)
heart$age
head(heart, n =2)
tail(heart, n =2)

# scatter plot of restecg on condition
plot(
  heart$restecg,
  heart$condition,
  col="red",
  main="restecg on condition",
  xlab="restecg",
  ylab="condition",
  pch=24
)

# box plot of trestbps on condition
boxplot(
  condition~trestbps,
  data=heart,
  col="red",
  main="trestbps on condition",
  xlab="trestbps",
  ylab="condition"
)


# histogram for condition
hist(
  heart$condition,
  breaks=10,
  col="red",
  main="histogram for condition",
  xlab="condition",
)

# histogram for age
hist(
  heart$age,
  breaks=10,
  col="red",
  main="histogram for age",
  xlab="age",
)

# histogram for cholesterol
hist(
  heart$chol,
  breaks=10,
  col="red",
  main="histogram for cholesterol",
  xlab="cholesterol",
)


# scatter plot of all features
plot(heart)


# histogram that loops through all variables
par(mfrow=c(4, 4))
  
for (name in names(heart)){
    hist(
      heart[, name],
      main=paste("Histogram of ", name, sep = ""),
      xlab=name,
      col="red"
    )
}

# linear regression
lm_age = lm(condition ~ age, data=heart)
lm_chol = lm(condition ~ chol, data=heart)

# get attributes of lm object
names(lm_univariate)

# see more details about the model
summary(lm_age)
summary(lm_chol)

# predict heart disease at different ages
predict(lm_age, data.frame(age=c(35,50,65)))

# predict heart disease at different cholesterols
predict(lm_chol, data.frame(chol=c(175,275,375)))
        

# get attributes of lm object
# names(lm_univariate)

# see more details about the model



# predict heart disease at different ages
predict(lm_age, data.frame(age=c(35,50,65)))

# predict heart disease at different cholesterols
predict(lm_chol, data.frame(chol=c(175,275,375)))


# plot heart disease v.s. age with trendline from the univariate model
lm_age = lm(condition ~ age, data=heart)

summary(lm_age)

plot(
  heart$age,
  heart$condition,
  xlab = "age",
  ylab = "condition",
  main = "heart disease v.s. age",
  pch = 20
)

abline(
  lm_age,
  lwd=3,
  col="red"
)

# plot heart disease v.s. sex with trendline from the univariate model
lm_sex = lm(condition ~ sex, data=heart)

summary(lm_sex)

plot(
  heart$sex,
  heart$condition,
  xlab = "sex",
  ylab = "condition",
  pch = 20
)

abline(
  lm_sex,
  lwd=3,
  col="red"
)


# plot heart disease v.s. cp with trendline from the univariate model
lm_cp = lm(condition ~ cp, data=heart)

summary(lm_cp)

plot(
  heart$cp,
  heart$condition,
  xlab = "cp",
  ylab = "condition",
  pch = 20
)

abline(
  lm_cp,
  lwd=3,
  col="red"
)


# plot heart disease v.s. trestbps with trendline from the univariate model
lm_trestbps = lm(condition ~ trestbps, data=heart)

summary(lm_trestbps)

plot(
  heart$trestbps,
  heart$condition,
  xlab = "trestbps",
  ylab = "condition",
  pch = 20
)

abline(
  lm_trestbps,
  lwd=3,
  col="red"
)

# plot heart disease v.s. cholesterol with trendline from the univariate model
lm_chol = lm(condition ~ chol, data=heart)

summary(lm_chol)

plot(
  heart$chol,
  heart$condition,
  xlab = "cholesterol",
  ylab = "condition",
  main = "heart disease v.s. cholesterol",
  pch = 20
)

abline(
  lm_chol,
  lwd=3,
  col="red"
)

# heart disease v.s. fbs 
lm_fbs = lm(condition ~ fbs, data=heart)
summary(lm_fbs)


# heart disease v.s. restecg 
lm_restecg = lm(condition ~ restecg, data=heart)
summary(lm_restecg)


# heart disease v.s. thalach 
lm_thalach = lm(condition ~ thalach, data=heart)
summary(lm_thalach)


# heart disease v.s. exang 
lm_exang = lm(condition ~ exang, data=heart)
summary(lm_exang)


# heart disease v.s. oldpeak 
lm_oldpeak = lm(condition ~ oldpeak, data=heart)
summary(lm_oldpeak)


# heart disease v.s. slope 
lm_slope = lm(condition ~ slope, data=heart)
summary(lm_slope)


# heart disease v.s. ca 
lm_ca = lm(condition ~ ca, data=heart)
summary(lm_ca)


# heart disease v.s. thal 
lm_thal = lm(condition ~ thal, data=heart)
summary(lm_thal)


# show the diagnositc plots
par(mfrow=c(2,2))
plot(lm_age)


# multivariate linear regression plots
names(heart)

lm_age_chol = lm(condition ~ age + chol, data=heart)
summary(lm_age_chol)

# is age + chol better than just age (no)
anova(lm_age_chol, lm_age)
# is age + chol better than just chol (yes)
anova(lm_age_chol, lm_chol)

par(mfrow=c(2,2))
plot(lm_age_chol)
plot(lm_age)


lm_common_sense = lm(condition ~ age + chol + sex + cp + trestbps + fbs + exang + thalach, data=heart)
summary(lm_common_sense)


lm_kitchen = lm(condition~., data=heart)
summary(lm_kitchen)

anova(lm_kitchen, lm_common_sense)
anova(lm_kitchen, lm_ca)
anova(lm_common_sense, lm_ca)