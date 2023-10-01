import streamlit as st
import pandas as pd
import torch
import joblib
import time
from main import predict

    
st.markdown("<h1 style='text-align: center;'>Student Performance</h1>", unsafe_allow_html=True)
st.markdown('')
st.markdown("""Welcome to our Student Performance Prediction web application! Are you interested in forecasting a student's academic success in secondary education? Our platform is dedicated to precisely that—utilizing artificial neural networks developed with PyTorch to predict student performance based on a diverse set of attributes, including grades, demographics, social elements, and school-related features.

Our data originates from two Portuguese schools and is centered on student achievements in two pivotal subjects: Mathematics and Portuguese language. These datasets have been meticulously refined and modeled to excel in binary/five-level classification and regression tasks, as detailed in [Cortez and Silva, 2008].

It's important to note that the target attribute G3 is significantly correlated with G2 and G1, where G3 represents the final year grade (issued at the 3rd period), while G1 and G2 correspond to the 1st and 2nd period grades. While predicting G3 without considering G1 and G2 presents challenges, it holds immense value, as outlined in the research.

As a visitor to our website, you can leverage our predictive model to achieve the following:

1. **Predict Student Performance**: Simply input relevant attributes, and our PyTorch-powered artificial neural network will provide accurate predictions of a student's performance in secondary education. This forecasting can be immensely valuable for educators, students, and parents alike.

2. **Educational Planning**: For educators and administrators, our platform is a valuable tool for identifying students who may require additional support or tailored interventions, ultimately helping to enhance educational strategies for improved outcomes.

3. **Data-Driven Decisions**: Researchers and policymakers can harness our platform to make data-driven decisions and gain deeper insights into student performance, potentially leading to positive reforms in the education system.

Our web application offers a user-friendly interface, making it easy to access the power of our predictive model. Our model has been rigorously trained and validated using state-of-the-art machine learning techniques. Additionally, if you're interested in reviewing the methodology and the code behind this project, you can find it on [GitHub](https://github.com/shre-db/Student-Performance). This open-source approach allows you to explore the inner workings of our predictive model and gain a deeper understanding of how it functions.

Unlock the potential to predict student performance with precision and make informed decisions to support educational success. Get started on your journey to better understanding and improving academic achievements today!""")
            
st.markdown('***')

# Nominal
school = st.selectbox('SCHOOL', options=["Select an option", 'Gabriel Pereira', 'Mousinho da Silveira'])
if school == 'Select an option':
    st.warning('No option is selected!', icon='⚠')
elif school == 'Gabriel Pereira':
    school = 'GP'
elif school == 'Mousinho da Silveira':
    school = 'MS'
st.markdown('***')

# Nominal
sex = st.selectbox('SEX', options=['Select an option', 'Female', 'Male'])
if sex == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif sex == 'Female':
    sex = 'F'
elif sex == 'Male':
    sex = 'M'
st.markdown('***')

# Discrete/Interval
age = st.slider('AGE', min_value=15, max_value=22, step=1)
st.markdown('***')

# Nominal
address_type = st.selectbox('ADDRESS TYPE', options=["Select an option", "Urban", "Rural"])
if address_type == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif address_type == 'Urban':
    address_type = 'U'
elif address_type == 'Rural':
    address_type = 'R'
st.markdown('***')

# Nominal
family_size = st.selectbox('FAMILY SIZE', options=["Select an option", "Less than 3", "Greater than 3"])
if family_size == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif family_size == 'Less than 3':
    family_size = 'LE3'
elif family_size == 'Greater than 3':
    family_size = 'GT3'
st.markdown('***')

# Nominal
par_cohab = st.selectbox("PARENT'S COHABITATION STATUS", options=["Select an option", "Living Together", "Apart"])
if par_cohab == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif par_cohab == 'Living Together':
    par_cohab = 'T'
elif par_cohab == 'Apart':
    par_cohab = 'A'
st.markdown('***')

# Ordinal
mother_edu = st.selectbox("MOTHER'S EDUCATION", options=['None (default)', 'Primary Education (4th grade)', '5th to 9th grade', 'Secondary Education', 'Higher Education'])
if mother_edu == 'None (default)':
    mother_edu = 0
elif mother_edu == 'Primary Education (4th grade)':
    mother_edu = 1
elif mother_edu == '5th to 9th grade':
    mother_edu = 2
elif mother_edu == 'Secondary Education':
    mother_edu = 3
elif mother_edu == 'Higher Education':
    mother_edu = 4  
st.markdown('***')

# Ordinal
father_edu = st.selectbox("FATHER'S EDUCATION", options=['None (default)', 'Primary Education (4th grade)', '5th to 9th grade', 'Secondary Education', 'Higher Education'])
if father_edu == 'None (default)':
    father_edu = 0
elif father_edu == 'Primary Education (4th grade)':
    father_edu = 1
elif father_edu == '5th to 9th grade':
    father_edu = 2
elif father_edu == 'Secondary Education':
    father_edu = 3
elif father_edu == 'Higher Education':
    father_edu = 4
st.markdown('***')

# Nominal
mother_job = st.selectbox("MOTHER'S JOB", options=['Select an option', 'Teacher', 'Health care related', 'Civil Services (e.g. Administrative or Police)', 'At home', 'Other'])
if mother_job == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif mother_job == 'Teacher':
    mother_job = 'teacher'
elif mother_job == 'Health care related':
    mother_job = 'health'
elif mother_job == 'Civil Services (e.g. Administrative or Police)':
    mother_job = 'services'
elif mother_job == 'At home':
    mother_job = 'at_home'
elif mother_job == 'Other':
    mother_job = 'other'
st.markdown('***')

# Nominal
father_job = st.selectbox("FATHER'S JOB", options=['Select an option', 'Teacher', 'Health care related', 'Civil Services (e.g. Administrative or Police)', 'At home', 'Other'])
if father_job == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif father_job == 'Teacher':
    father_job = 'teacher'
elif father_job == 'Health care related':
    father_job = 'health'
elif father_job == 'Civil Services (e.g. Administrative or Police)':
    father_job = 'services'
elif father_job == 'At home':
    father_job = 'at_home'
elif father_job == 'Other':
    father_job = 'other'
st.markdown('***')

# Nominal
reason = st.selectbox("REASON TO CHOOSE THIS SCHOOL", options=['Select an option', 'Close to Home', 'School Reputation', 'Course Preference', 'Other'])
if reason == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif reason == 'Close to Home':
    reason = 'home'
elif reason == 'School Reputation':
    reason = 'reputation'
elif reason == 'Course Preference':
    reason = 'course'
elif reason == 'Other':
    reason = 'other'
st.markdown('***')

# Nominal
guardian = st.selectbox("GUARDIAN", options=['Select an option', 'Mother', 'Father', 'Other'])
if guardian == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif guardian == 'Mother':
    guardian = 'mother'
elif guardian == 'Father':
    guardian = 'father'
elif guardian == 'Other':
    guardian = 'other'
st.markdown('***')

# Discrete/Ratio
travel_time = st.text_input("HOME TO SCHOOL TRAVEL TIME", placeholder='minutes')
if travel_time == '':
    st.warning('Field is empty!', icon='⚠')
else:
    try:
        travel_time = int(travel_time)
    except ValueError:
        st.warning('Please enter only numbers!', icon='⚠')
        study_time = ''
st.markdown('***')

# Discrete/Ratio
study_time = st.text_input("WEEKLY STUDY TIME", placeholder='hours')
if study_time == '':
    st.warning('Field is empty!', icon='⚠')
else:
    try:
        study_time = int(study_time)
    except ValueError:
        st.warning('Please enter only numbers!', icon='⚠')
        study_time = ''
st.markdown('***')

# Discrete/Ratio
failures = st.text_input("NUMBER OF PAST CLASS FAILURES") # Some Confusion *************************************************************
if failures == '':
    st.warning('Field is empty!', icon='⚠')
else:
    try:
        failures = int(failures)
    except ValueError:
        st.warning('Please enter only numbers!', icon='⚠')
        failures = ''
st.markdown('***')

# Nominal
edu_support = st.radio("EXTRA EDUCATIONAL SUPPORT", ["Yes", "No"])
if edu_support == 'Yes':
    edu_support = 'yes'
elif edu_support == 'No':
    edu_support = 'no' 
st.markdown('***')

# Nominal
fam_edu_support = st.radio("FAMILY EDUCATIONAL SUPPORT", ["Yes", "No"])
if fam_edu_support == 'Yes':
    fam_edu_support = 'yes'
elif fam_edu_support == 'No':
    fam_edu_support = 'no'
st.markdown('***')

# Nominal
paid_classes = st.radio("EXTRA PAID CLASSES WITHIN THE COURSE SUBJECT", ["Yes", "No"])
if paid_classes == 'Yes':
    paid_classes = 'yes'
elif paid_classes == 'No':
    paid_classes = 'no'
st.markdown('***')

# Nominal
extra_curr = st.radio("EXTRA-CURRICULAR ACTIVITIES", ["Yes", "No"])
if extra_curr == 'Yes':
    extra_curr = 'yes'
elif extra_curr == 'No':
    extra_curr = 'no'
st.markdown('***')

# Nominal
nursery = st.radio("ATTENDED NURSERY SCHOOL", ["Yes", "No"])
if nursery == 'Yes':
    nursery = 'yes'
elif nursery == 'No':
    nursery = 'no'
st.markdown('***')

# Nominal
higher_edu = st.radio("WANTS TO TAKE HIGHER EDUCATION", ["Yes", "No"])
if higher_edu == 'Yes':
    higher_edu = 'yes'
elif higher_edu == 'No':
    higher_edu = 'no'
st.markdown('***')

# Nominal
int_access = st.radio("INTERNET ACCESS AT HOME", ["Yes", "No"])
if int_access == 'Yes':
    int_access = 'yes'
elif int_access == 'No':
    int_access = 'no'
st.markdown('***')

# Nominal
romantic_rel = st.radio("ROMANTIC RELATIONSHIP", ["Yes", "No"])
if romantic_rel == 'Yes':
    romantic_rel = 'yes'
elif romantic_rel == 'No':
    romantic_rel = 'no'
st.markdown('***')

# Ordinal
fam_rel = st.selectbox("QUALITY OF FAMILY RELATIONSHIPS", options=['Select an option', 'Poor', 'Bad', 'Neutral', 'Good', 'Excellent'])
if fam_rel == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif fam_rel == 'Poor':
    fam_rel = 1
elif fam_rel == 'Bad':
    fam_rel = 2
elif fam_rel == 'Neutral':
    fam_rel = 3
elif fam_rel == 'Good':
    fam_rel = 4
elif fam_rel == 'Excellent':
    fam_rel = 5
st.markdown('***')

# Ordinal
free_time = st.selectbox("FREE TIME AFTER SCHOOL", options=['Select an option', 'Very Low', 'Low', 'Balanced', 'High', 'Very High'])
if free_time == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif free_time == 'Very Low':
    free_time = 1
elif free_time == 'Low':
    free_time = 2
elif free_time == 'Balanced':
    free_time = 3
elif free_time == 'High':
    free_time = 4
elif free_time == 'Very High':
    free_time = 5
st.markdown('***')

# Ordinal
go_out = st.selectbox("GOING OUT WITH FRIENDS", options=['Select an option', 'Very Low', 'Low', 'Balanced', 'High', 'Very High'])
if go_out == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif go_out == 'Very Low':
    go_out = 1
elif go_out == 'Low':
    go_out = 2
elif go_out == 'Balanced':
    go_out = 3
elif go_out == 'High':
    go_out = 4
elif go_out == 'Very High':
    go_out = 5
st.markdown('***')

# Ordinal
wkday_alcohol = st.selectbox("WORKDAY ALCOHOL CONSUMPTION", options=['Select an option', 'Very Low', 'Low', 'Moderate', 'High', 'Very High'])
if wkday_alcohol == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif wkday_alcohol == 'Very Low':
    wkday_alcohol = 1
elif wkday_alcohol == 'Low':
    wkday_alcohol = 2
elif wkday_alcohol == 'Moderate':
    wkday_alcohol = 3
elif wkday_alcohol == 'High':
    wkday_alcohol = 4
elif wkday_alcohol == 'Very High':
    wkday_alcohol = 5
st.markdown('***')

# Ordinal
wkend_alcohol = st.selectbox("WEEKEND ALCOHOL CONSUMPTION", options=['Select an option', 'Very Low', 'Low', 'Moderate', 'High', 'Very High'])
if wkend_alcohol == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif wkend_alcohol == 'Very Low':
    wkend_alcohol = 1
elif wkend_alcohol == 'Low':
    wkend_alcohol = 2
elif wkend_alcohol == 'Moderate':
    wkend_alcohol = 3
elif wkend_alcohol == 'High':
    wkend_alcohol = 4
elif wkend_alcohol == 'Very High':
    wkend_alcohol = 5
st.markdown('***')

# Ordinal
health = st.selectbox("CURRENT HEALTH STATUS", options=['Select an option', 'Poor', 'Bad', 'Average', 'Good', 'Excellent'])
if health == 'Select an option':
    st.warning('No option is selected', icon='⚠')
elif health == 'Poor':
    health = 1
elif health == 'Bad':
    health = 2
elif health == 'Average':
    health = 3
elif health == 'Good':
    health = 4
elif health == 'Excellent':
    health = 5
st.markdown('***')

# Discrete/Ratio
absenses = st.slider("NUMBER OF SCHOOL ABSENCES", min_value=0, max_value=93, step=1)
if absenses == 'Select an option':
    st.warning('No option is selected', icon='⚠')
st.markdown('***')

# Discrete/Ratio
g1 = st.slider("FIRST PERIOD GRADE", min_value=0, max_value=20, step=1)
if g1 == 'Select an option':
    st.warning('No option is selected', icon='⚠')
st.markdown('***')

# Discrete/Ratio
g2 = st.slider("SECOND PERIOD GRADE", min_value=0, max_value=20, step=1)
if g2 == 'Select an option':
    st.warning('No option is selected', icon='⚠')
st.text('')
st.text('')
st.text('')


variables = {
    'school': [school], 'sex': [sex], 'age': [age], 'address': [address_type], 'famsize': [family_size],
    'Pstatus': [par_cohab], 'Medu': [mother_edu], 'Fedu': [father_edu], 'Mjob': [mother_job], 'Fjob': [father_job],
    'reason': [reason], 'guardian': [guardian], 'traveltime': [travel_time], 'studytime': [study_time], 'failures': [failures],
    'schoolsup': [edu_support], 'famsup': [fam_edu_support], 'paid': [paid_classes], 'activities': [extra_curr],
    'nursery': [nursery], 'higher': [higher_edu], 'internet': [int_access], 'romantic': [romantic_rel], 'famrel': [fam_rel],
    'freetime': [free_time], 'goout': [go_out], 'Dalc': [wkday_alcohol], 'Walc': [wkend_alcohol], 'health': [health],
    'absences': [absenses], 'G1': [g1], 'G2': [g2] 
}

if st.button("Submit", help="When you click 'submit', the information you provided will be sent to the model for inference."):

    for k, v in variables.items():
        if v[0] in ['Select an option', '']:
            st.warning('One or more fields are either empty or contain inappropriate values.', icon='⚠')
            break
    else:
        data = pd.DataFrame(variables)

        cat_cols = data.select_dtypes(include=['object']).columns.to_list()
        num_cols = data.select_dtypes(exclude=['object']).columns.to_list()

        transf_pipeline = joblib.load('transformers/pipeline.joblib')

        inp = transf_pipeline.transform(data)
        inpT = torch.tensor(inp).view(1, 58).float()


        pred = predict(data=inpT)
        score = pred.detach().item()
        st.markdown('***')
        with st.spinner('Processing your information...'):
            time.sleep(3)
        with st.success('Success! Your predicted score is', icon="✔"):
            pass
        st.markdown(f'# :rainbow[{int(round(score, 0))}/20]')
        st.markdown('#### :rainbow[We wish you all the best!]')
        st.balloons()
