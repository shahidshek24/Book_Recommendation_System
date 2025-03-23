import streamlit as st
import pickle
import pandas as pd
import numpy as np
books=pickle.load(open('books.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
def recommend(book_name):
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title']))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author']))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M']))
        data.append(item)
    return data
st.title("📚 Book Recommendation System")
selected_book_title = st.selectbox("Enter the book title", pt.index)
if st.button("Recommend"):
    books_list = recommend(selected_book_title)
    st.write(f"**Recommendations for {selected_book_title}:**")
    cols = st.columns(len(books_list))
    for idx, col in enumerate(cols):
        with col:
            st.image(books_list[idx][2], caption=f"{books_list[idx][0]} by {books_list[idx][1]}")