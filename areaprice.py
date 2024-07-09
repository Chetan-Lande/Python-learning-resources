import pickle
import sklearn
import streamlit as st

model2=pickle.load(open('area.pkl',"rb"))

def myf1():
  st.title("Area Price Prediction")
  area = st.number_input("Enter the area value...")
  pred=st.button("Predict")

  if pred:
    op1 = model2.predict([[area]])
    st.write("price of the area is :",op1[0])

myf1()