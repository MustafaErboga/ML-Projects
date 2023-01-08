import pandas as pd      
import pickle
import streamlit as st
from PIL import Image


# here we define some of the front end elements of the web page like the font and background color,
# the padding and the text to be displayed

html_temp = """
	<div style ="background-color:#3d2fd6; padding:13px">
	<h1 style ="color:#f0f0f5; text-align:center; ">Streamlit Car Price Prediction  </h1>
	</div>
	"""
    
# this line allows us to display the front end aspects we have defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)

# İmages of Car Price Prediction
image = Image.open("Car.png")
st.image(image, use_column_width=True)


# Display Iris Dataset
st.header("_Car Price Prediction Dataset_")
df = pd.read_csv('car_pred.csv')
st.write(df.head())

# Loading the models to make predictions
lasso_model = pickle.load(open("lasso_model", "rb"))


# User input variables that will be used on predictions


make_model = st.sidebar.radio("Make&Model", df.make_model.unique())
hp_kW = st.number_input("hp_kW", min_value=40, max_value=300, step=2)
km = st.number_input("KM", min_value=0, max_value=350000,step=10000)
age = st.sidebar.radio("Age", df.age.unique())
Gearing_Type = st.sidebar.radio("Gearing Type", ('Manual', 'Automatic', 'Semi-automatic'))
Gears = st.sidebar.radio("Gears", (5,6,7,8))
Type = st.sidebar.radio("Type", df.Type.unique())


# Converting user inputs to dataframe 

my_dict = {
        "make_model":make_model,
        "hp_kW":hp_kW,
        "km":km,
        "age":age,
        "Gearing_Type":Gearing_Type, 
        "Gears":Gears,
        "Type":Type
}

df = pd.DataFrame.from_dict([my_dict])

st.table(df)

if st.button("Predict"):
    pred = lasso_model.predict(df)
    st.write(pred[0])
    


