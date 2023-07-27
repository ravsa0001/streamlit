# Importing libraries
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Taking the input or rather person review for analysys
st.markdown("<h1 style = 'text-align : center'> Enter the review for you product </h1>", unsafe_allow_html=True)    
rev = st.text_area("", height = 200)

# Converting the string into a list
review = [rev]

# Importing the file for sentiment analysys
with open("model_pickle.pkl", "rb") as f:
    cv, mod = pickle.load(f)
# Performing counvectorizer that converts a string into float values
review_count = cv.transform(review) 
# Analysing the review given by the user
result = mod.predict(review_count)[0]

# Giving the Output whether the given review is positive or not
if len(rev) != 0:
    if result == 1:
        st.title(":green[Good Review] :smiley:")
    elif result == 0:
        st.title(":red[Bad Review] :disappointed: ")
