import streamlit as st
import pickle

num2label = {1 : "Good Review", 0 : "Bad Review"}
    
rev = st.text_area("Enter any review for your product", height = 200)

review = [rev]

with open("Notebook/model_pickle", "rb") as f:
    cv, mod = pickle.load(f)
    
review_count = cv.transform(review)

result = mod.predict(review_count)[0]

if result == 1:
    st.markdown("<h1 style='text-align: center; :green[Good Review. :+1:]</h1>", unsafe_allow_html=True)
elif result == 0:
    st.markdown("<h1 style='text-align: center; color: red;'>Bad Review :disappointed:</h1>", unsafe_allow_html=True)
    
st.markdown(":sunglasses:")