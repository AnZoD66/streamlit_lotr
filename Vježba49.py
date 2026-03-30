import streamlit as st
from datetime import date
import pandas as pd
import random
from lotr_library.questions import easy_questions, extra_questions, advanced_questions
from lotr_library.books import tolkien_books
from rapidfuzz import fuzz, process
from streamlit_searchbox import st_searchbox

st.title("The Lord of the Rings Watch Reminder")

st.subheader("Hey! Come merry dol! Hey! Come derry dol! Hop along, my hearties! Hobbits! Ponies, all! We are fond of parties. Now let the fun begin! Let us sing together!")

st.subheader("Have you ever seen The Lord of the Rings trilogy?")

if "seen_lotr" not in st.session_state:
    st.session_state.seen_lotr = None

if "read_books" not in st.session_state:
    st.session_state.read_books = None

if "book_input" not in st.session_state:
    st.session_state.book_input = ""

if "book_list" not in st.session_state:
    st.session_state.book_list = []

if "books_entered" not in st.session_state:
    st.session_state.books_entered = []

if "quiz_unlocked" not in st.session_state:
    st.session_state.quiz_unlocked = False

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

if "show_correct" not in st.session_state:
    st.session_state.show_correct = False

if "book_input" not in st.session_state:
    st.session_state.book_input = ""

if "enter_pressed_once" not in st.session_state:
    st.session_state.enter_pressed_once = False

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.quiz_pool = []
    st.session_state.failed = False

if "show_correct_message" not in st.session_state:
    st.session_state.show_correct_message = False

if "success_message" not in st.session_state:
    st.session_state.success_message = ""

if "last_added_book" not in st.session_state:
    st.session_state.last_added_book = None

if st.button("Yes I have seen The Lord of the Rings."):
    st.session_state.seen_lotr = "Yes"

if st.button("No I haven't seen it."):
    st.session_state.seen_lotr = "No"

min_date = date(2001, 1, 10)

if "clear_book_input" not in st.session_state:
    st.session_state.clear_book_input = False

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
            st.write("Greetings the child of Ilúvatar! What books have you read?")
            def search_tolkien_books(query: str):
                if not query:
                    return []
                available = [b for b in tolkien_books if b not in st.session_state.book_list]
                results = process.extract(query, available, scorer=fuzz.token_sort_ratio, limit=5)
                return [r[0] for r in results if r[1] >= 40]
            def handle_book_submit(book_name=None):
                if not book_name:
                    st.session_state.success_message = "Please select a book from the suggestions."
                    return
                if book_name not in st.session_state.book_list:
                    st.session_state.book_list.append(book_name)
                    st.session_state.success_message = f"Added '{book_name}' to your list!"
                else:
                    st.session_state.success_message = f"You already entered '{book_name}'."
            selected_book = st_searchbox(
                search_tolkien_books,
                label="Type a book name:",
                key="book_searchbox",
                placeholder="e.g. The Hobbit...")
            if selected_book and selected_book != st.session_state.get("last_added_book"):
                handle_book_submit(book_name=selected_book)
                st.session_state.last_added_book = selected_book
            if st.button("Add book"):
                handle_book_submit(book_name=selected_book)
            if "success_message" in st.session_state and st.session_state.success_message:
                st.info(st.session_state.success_message)
            if st.session_state.book_list:
                df_books = pd.DataFrame({"Books Read": st.session_state.book_list})
                st.subheader("Books you've read:")
                st.dataframe(df_books, height=200)
            if len(st.session_state.book_list) > 3:
                st.session_state.quiz_unlocked = True
                st.subheader("Congratulations! You have unlocked the book quiz!")
        elif st.session_state.read_books == "No":
            st.write("The vast lore of Middle-Earth is waiting for you! If is thy desire you can explore it.")
    elif 7 <= days_since_watched < 14:
        st.write("You're fresh from Middle-Earth! Approaching the time of rewatching!")
    elif 14 <= days_since_watched < 30:
        st.write("Palantíri have seen that you're approaching the shadows! Rewatch it as soon as possible!")
    elif 30 <= days_since_watched < 180:
        st.write("The ring won't be carried itself to Mordor! Ordinary people display great courage! Watch it to help the free folk of Middle-Earth!")
    elif days_since_watched >= 180:
        st.write("The Audacity! Gandalf insists! You should stop what you're doing and rewatch it immediately!")
elif st.session_state.seen_lotr == "No":
    st.subheader("Fool of a Took! Take heed! Your adventure should start immediately!")

if st.session_state.quiz_unlocked:
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.quiz_pool = []
        st.session_state.failed = False
    total_questions = len(easy_questions) + len(extra_questions) + len(advanced_questions)
    if not st.session_state.quiz_started:
        st.subheader("The Adventure of Middle-earth awaits...")
        if st.button("Start Quiz"):
            easy = easy_questions.copy()
            extra = extra_questions.copy()
            advanced = advanced_questions.copy()
            random.shuffle(easy)
            random.shuffle(extra)
            random.shuffle(advanced)
            st.session_state.quiz_pool = easy + extra + advanced
            st.session_state.quiz_started = True
            st.rerun()
    else:
        progress = st.session_state.current_index / total_questions
        st.progress(progress)
        st.write(f"Score: {st.session_state.score}/{total_questions}")
        if st.session_state.failed:
            st.error(f"Wrong answer! Final score: {st.session_state.score}/{total_questions}")
            if st.session_state.score < len(easy_questions):
                st.write("You have much to learn, young hobbit.")
            elif st.session_state.score < len(easy_questions) + len(extra_questions)// 2:
                st.write("You are displaying decent knowlage of Middle-earth!")
            elif st.session_state.score < len(easy_questions) + len(extra_questions):
                st.write("A respectable lore-master of Middle-earth!")
            else:
                st.write("You stand among the wisest of the Eldar.")
            if st.button("Restart Quiz"):
                for key in ["quiz_started", "score", "current_index", "quiz_pool", "failed"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
            st.stop()
        i = st.session_state.current_index
        if i < len(easy_questions):
            st.info("Easy Questions — A gentle beginning in the Shire...")
        elif i < len(easy_questions) + len(extra_questions):
            st.info("Extra Questions — The road goes ever on...")
        else:
            st.info("Advanced Questions — The final test of lore mastery...")
        if st.session_state.current_index >= total_questions:
            st.success("Perfect score! You are a true master of Tolkien lore!")
            st.balloons()
            st.stop()
        q = st.session_state.quiz_pool[st.session_state.current_index]
        answer = st.radio(
            q["question"],
            q["options"],
            key=f"question_{st.session_state.current_index}")
        if st.button("Hint", key=f"hint_{st.session_state.current_index}"):
            st.write(q["hint"])
        if st.button("Submit", key=f"submit_{st.session_state.current_index}"):
            if answer == q["answer"]:
                st.session_state.score += 1
                st.session_state.show_correct_message = True
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.session_state.failed = True
                st.rerun()
        if st.session_state.show_correct_message:
            st.success("Correct!")
            st.session_state.show_correct_message = False
