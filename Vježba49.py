import streamlit as st
from datetime import date
import pandas as pd

st.title("The Lord of the Rings Watch Reminder")

st.subheader("Hey! Come merry dol! Hey! Come derry dol! Hop along, my hearties! Hobbits! Ponies, all! We are fond of parties. Now let the fun begin! Let us sing together!")

st.subheader("Have you ever seen The Lord of the Rings trilogy?")

if "seen_lotr" not in st.session_state:
    st.session_state.seen_lotr = None

if "read_books" not in st.session_state:
    st.session_state.read_books = None

if "book_list" not in st.session_state:
    st.session_state.book_list = []

if st.button("Yes I have seen The Lord of the Rings."):
    st.session_state.seen_lotr = "Yes"

if st.button("No I haven't seen it."):
    st.session_state.seen_lotr = "No"
min_date = date(2002, 1, 10)

if st.session_state.seen_lotr == "Yes":
    st.subheader("My Friend! You bow to no one! Let us explore the date of your last adventure!")
    last_watched = st.date_input("Date of the last adventure:", value=date.today(), max_value=date.today(), min_value=min_date)
    formatted_date = last_watched.strftime("%d/%m/%Y")
    st.success(f"Last adventure was: {formatted_date}") 
    days_since_watched = (date.today() - last_watched).days
    if days_since_watched < 7:
        st.write("You're consistent! Have you considered books?")
        st.radio("Have you read any LOTR books?",("Yes", "No"), key="read_books")
        if st.session_state.read_books == "Yes":
            st.write("Mae Govannen hén-o Ilúvatar! What books have you read?")
            new_book = st.text_input("Enter books you have read:", key="new_book")
            if st.button("Add book!", key="add_book"):
                 if new_book.strip():
                    st.session_state.book_list.append(new_book.strip())
                    st.success(f"Awesome! You've read: {st.session_state.book_list}")
                    if st.session_state.book_list:
                        df_books = pd.DataFrame({"Books Read": st.session_state.book_list})
                        st.subheader("Books you’ve read:")
                        st.dataframe(df_books, height=200)
            else:
                st.warning("Take heed! Please enter book before clicking Add.")
        elif st.session_state.read_books == "No":
            st.write("The wast lore of Middle-Earth is waiting for you! If is thy desire you can explore it.")
    elif 7 <= days_since_watched < 14:
        st.write("You're fresh from Middle-Earth! Aproching the time of rewatching!")
    elif 14 <= days_since_watched < 30:
        st.write("Palantíri have seen that you're aproaching the shadows! Rewatch it as soon as possible!")
    elif 30 <= days_since_watched < 180:
        st.write("The ring won't be carried itself to Mordor! Ordinary people desplay great curage! Watch it to help the free folk of Middle-Earth!")
    elif days_since_watched >= 180:
        st.write("The Audacity! Gandalf insists! You should stop what you're doing and rewatch it immediately!")
elif st.session_state.seen_lotr == "No":

    st.subheader("Fool of a Took! Take heed! Your adventure should start immediatly!")               

