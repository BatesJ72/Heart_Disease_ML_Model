# Heart Disease Machine Learning Project

### Goal: Take data on heart disease and predict if a person is likely to develop this condition. The input portion of the project will allow a person to input their information and receive a result of the likelihood of developing heart disease.

### Routes 
- Home: Explains the project. Users put in their information, and it tells them how likely they are to develop heart disease
- Ghost route to transfer data between front end and back end
- Data Information: Visualization(s). Explanation of what model was chosen and why. Dictionary of terms (i.e. exercise induced angina). Limitations of dataset. 

### Workflow
(1a) Data wrangling and writing ML code: Loading/cleaning the data first to prep it to go into a ML model, then determine the best model. <br>
(1b) Design the basic frontend/flask app: The frontend/flask app could be developed in parallel with data wrangling, since we can plug in the actual data once we finish the ML part. <br>
(2) Design the user input section: Once we know what the important factors are for ML we could design the user input section. For example, there are 14 factors listed in the heart disease data, but if 3-4 are highly correlated then we would want the input focused on those rather than all 14.  <br>
(3) Finish the frontend/flask app with the competed analysis <br>
(4) Develop visuals: Once all the analysis is done, we'll develop visualization(s). <br>

### Data
https://www.kaggle.com/cherngs/heart-disease-cleveland-uci
 <br> <br>
<i>Data Attributes  </i><br>
age: age in years <br>
sex: sex (1 = male; 0 = female) <br>
cp: chest pain type <br>
-- Value 0: typical angina <br>
-- Value 1: atypical angina <br>
-- Value 2: non-anginal pain <br>
-- Value 3: asymptomatic <br>
trestbps: resting blood pressure (in mm Hg on admission to the hospital) <br>
chol: serum cholestoral in mg/dl <br>
fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) <br>
restecg: resting electrocardiographic results <br>
-- Value 0: normal <br>
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) <br>
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria <br>
thalach: maximum heart rate achieved <br>
exang: exercise induced angina (1 = yes; 0 = no) <br>
oldpeak = ST depression induced by exercise relative to rest <br>
slope: the slope of the peak exercise ST segment <br>
-- Value 0: upsloping <br>
-- Value 1: flat <br>
-- Value 2: downsloping <br>
ca: number of major vessels (0-3) colored by flourosopy <br>
thal: 0 = normal; 1 = fixed defect; 2 = reversable defect <br>
condition: 0 = no disease, 1 = disease <br>



Notes from Ed:
It's important to know the why - why did the person get heart disease? Use something like Lime or Shap to determine "causality".
Try to get a working prototype asap. No need for a database - just use the CSV. 
