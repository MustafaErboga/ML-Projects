import pandas as pd      
import pickle
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Employee Churn Prediction',
    page_icon='employee churn.jpeg'
                  )

st.markdown("<h1 style='text-align: center; color: red;'>Employee Churn Prediction Application</h1>", unsafe_allow_html=True)





_, col2, _ = st.columns([2, 3, 2])

with col2:  
    img = Image.open("employee churn2.jpg")
    st.image(img, width=300)

st.success('###### Our model is trained using 14,999 samples with the following parameters.')


st.info("###### Satisfaction Level: It is employee satisfaction point, which ranges from 0-1 :smiley:\n"
        "###### Last Evaluation: It is evaluated performance by the employer, which also ranges from 0-1 :male-detective:\n"
        "###### Number of Projects: How many of projects assigned to an employee? :older_adult:\n"
        "###### Average Monthly Hours: How many hours in averega an employee worked in a month? :stopwatch:\n"
        "###### Time Spent Company: time_spent_company means employee experience. The number of years spent by an employee in the company :\n"
        "###### Work Accident: Whether an employee has had a work accident or not. :face_with_head_bandage:\n"
        "###### Promotion Last 5 years: Whether an employee has had a promotion in the last 5 years or not :gift:\n"
        "###### Departments: Employee's working department/division  :female-mechanic:\n"
        "###### Salary: Salary level of the employee such as low, medium and high :moneybag:\n"
        "###### Left: Whether the employee has left the company or not :slightly_frowning_face:")

st.success("###### Information about your employee")

import pickle


models = {}

filename1 = 'knn_final_model.pkl'
models['KNN'] = pickle.load(open(filename1, 'rb'))

filename2 = 'RF_final_model.pkl'
models['Random_Forest'] = pickle.load(open(filename2, 'rb'))

filename3 = 'xgb_final_model.pkl'
models['XGBoost'] = pickle.load(open(filename3, 'rb'))

# Kullanıcının seçeceği modelin adını alın
model_choice = input("Which model would you like to use? (KNN, Random_Forest or XGBoost)")

# Seçilen modelin kullanımı örneği
if model_choice == 'KNN':
    prediction = models['KNN'].predict(data)
elif model_choice == 'Random_Forest':
    prediction = models['Random_Forest'].predict(data)
elif model_choice == 'XGBoost':
    prediction = models['XGBoost'].predict(data)
else:
    print("Invalid model selection!")

    
    
col, col2 = st.columns([4, 4])
with col:
    st.markdown("###### Select Your Employee's Department")
    departments = st.selectbox("Departments",
            ('sales', 'accounting', 'hr', 'technical', 'support', 'management',
        'IT', 'product_mng', 'marketing', 'RandD')
        )
with col2:
    st.markdown("###### Select Your Employee's Salary")
    salary = st.radio(
        "Salary",
        ('low', 'medium', 'high')
        )
    
        
col1, col2 = st.columns([4, 4])

with col1:
    st.markdown("#####")
    st.markdown("###### Has the employee had a work accident?")
    work_accident = st.radio(
        "Work Accident",
        ('No', 'Yes')
        )   

    if work_accident == "Yes":   
        work_accident = 1 
    elif work_accident == "No":     
        work_accident = 0
        
with col2:
    st.markdown("#####")
    st.markdown("###### Has the employee been promoted in the last 5 years?")   
    promotion_last_5years = st.radio(
        "Promotion Last 5 years",
        ('Yes', 'No')
        )   
if promotion_last_5years == "Yes":   
    promotion_last_5years = 1 
elif promotion_last_5years == "No":     
    promotion_last_5years = 0


satisfaction_level = st.sidebar.slider("Satisfaction level:", 0, 1.0, 0.5)
st.write("Satisfaction level:", satisfaction_level)
last_evaluation = st.sidebar.slider("Last Evaluation Score:", 0, 1.0, 0.5)
st.write("Last Evaluation Score is:", last_evaluation)
number_project = st.sidebar.slider("Number of Projects:",min_value=1, max_value=10)
st.write("Number of Projects:", number_project)
average_montly_hours = st.sidebar.slider("Monthly Working Hours:",min_value=40, max_value=350)
st.write("Monthly Working Hours:", average_montly_hours)
time_spend_company = st.sidebar.slider("Years in the Company:",min_value=1, max_value=10)
st.write("Years in the Company:", time_spend_company)


my_dict = {
    'satisfaction_level': satisfaction_level,
    'last_evaluation': last_evaluation,
    'number_project': number_project,
    'average_montly_hours': average_montly_hours,
    'time_spend_company': time_spend_company,
    'work_accident': work_accident,
    'promotion_last_5years': promotion_last_5years,  
    'departments': departments,
    'salary': salary
}


df=pd.DataFrame.from_dict([my_dict])

col, col2 = st.columns([4, 4])

with col: 
    st.info("Your Choices for the Employee")
    my_dict

st.subheader("Press predict if configuration is okay")

with col2: 
    if st.button("Predict"):
        pred = model.predict(df)
        if int(pred[0]) == 1:
            st.error("Your employee has a high probability of churn")
            img = Image.open("churn.jpeg")
            st.image(img, width=300)
        else:
            st.success("Your employee loves the company")
            img = Image.open("not churn.png")
            st.image(img, width=300)
            
