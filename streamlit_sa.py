# Importing libraries
import streamlit as st
import pickle
import requests

# Taking the input or rather person review for analysys
st.markdown("<h1 style = 'text-align : center'> Enter the review for you product </h1>", unsafe_allow_html=True)    
rev = st.text_area("", height = 200)

# Converting the string into a list
review = [rev]

url = "https://github.com/ravsa0001/Sentiment_Analysis/blob/main/model_pickle.pkl"
response = requests.get(url)
# Importing the file for sentiment analysys
with open("model_pickle.pkl", "rb") as f:
    cv, mod = pickle.load(ff)
# Performing counvectorizer that converts a string into float values
review_count = cv.transform(review) 
# Analysing the review given by the user
result = mod.predict(review_count)[0]

# Giving the Output whether the given review is positive or not
m=st.markdown("""<style> div.stTitle { font-size:40px; } </style>""",unsafe_allow_html=True)
if len(rev) != 0:
    if result == 1:
        st.title(":green[Good Review] :smiley:")
    elif result == 0:
        st.title(":red[Bad Review] :disappointed: ")
