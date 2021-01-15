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
