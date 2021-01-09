# Heart Disease Machine Learning Project

### Goal: Take data on heart disease and predict if a person is likely to get it. The input portion would be a person putting in data on their lifestyle and it would give them the likelihood that they would develop heart disease.

### Routes 
- Home: Explains the project
- User Input: Users put in their information, and it tells them how likely they are to develop heart disease
- Visualization(s)
- Data Information: Explanation of what model was chosen and why. Dictionary of terms (i.e. exercise induced angina). Limitations of dataset. 

#### Workflow
(1a) Data wrangling and writing ML code: Loading/cleaning the data first to prep it to go into a ML model, then determine the best model. 
(1b) Design the basic frontend/flask app: The frontend/flask app could be developed in parallel with data wrangling, since we can plug in the actual data once we finish the ML part.
(2) Design the user input section: Once we know what the important factors are for ML we could design the user input section. For example, there are 14 factors listed in the heart disease data, but if 3-4 are highly correlated then we would want the input focused on those rather than all 14. 
(3) Finish the frontend/flask app with the competed analysis
(4) Develop visuals: Once all the analysis is done, we'll develop visualization(s).

### Data
https://www.kaggle.com/cherngs/heart-disease-cleveland-uci

Data Attributes: 
age: age in years
sex: sex (1 = male; 0 = female)
cp: chest pain type
-- Value 0: typical angina
-- Value 1: atypical angina
-- Value 2: non-anginal pain
-- Value 3: asymptomatic
trestbps: resting blood pressure (in mm Hg on admission to the hospital)
chol: serum cholestoral in mg/dl
fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
restecg: resting electrocardiographic results
-- Value 0: normal
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
thalach: maximum heart rate achieved
exang: exercise induced angina (1 = yes; 0 = no)
oldpeak = ST depression induced by exercise relative to rest
slope: the slope of the peak exercise ST segment
-- Value 0: upsloping
-- Value 1: flat
-- Value 2: downsloping
ca: number of major vessels (0-3) colored by flourosopy
thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
and the label
condition: 0 = no disease, 1 = disease
