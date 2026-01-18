import streamlit as st
from datetime import date
import pandas as pd
import random

st.title("The Lord of the Rings Watch Reminder")

st.subheader("Hey! Come merry dol! Hey! Come derry dol! Hop along, my hearties! Hobbits! Ponies, all! We are fond of parties. Now let the fun begin! Let us sing together!")

st.subheader("Have you ever seen The Lord of the Rings trilogy?")

if "seen_lotr" not in st.session_state:
    st.session_state.seen_lotr = None

if "read_books" not in st.session_state:
    st.session_state.read_books = None

if "new_book" not in st.session_state:
    st.session_state.new_book = ""

if "book_list" not in st.session_state:
    st.session_state.book_list = []

if "quiz_unlocked" not in st.session_state:
    st.session_state.quiz_unlocked = False

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

if "show_correct" not in st.session_state:
    st.session_state.show_correct = False

if st.button("Yes I have seen The Lord of the Rings."):
    st.session_state.seen_lotr = "Yes"

if st.button("No I haven't seen it."):
    st.session_state.seen_lotr = "No"

min_date = date(2001, 1, 10)

def add_book_enter():
    new_book = st.session_state.new_book.strip()
    if new_book:
        st.session_state.book_list.append(new_book)

extra_questions = [{"question": "Who forged the Silmarils?", "options": ["Thingol", "Melkor", "Tulkas", "Elrond", "Fëanor"], "answer": "Fëanor", "hint": "He was one of the greatest Elven craftsmen in the First Age."},
    {"question": "What is the tragic fate of Túrin Turambar?", "options": ["He becomes King of Gondor", "He marries Lúthien", "He was turned to stone", "He kills himself", "He becomes a Maia"], "answer": "He kills himself", "hint": "His life is marked by sorrow and doom in the First Age stories."},
    {"question": "What city is hidden and later falls to betrayal in the First Age?", "options": ["Minas Tirith", "Gondolin", "Rivendell", "Osgiliath", "Erebor"], "answer": "Gondolin", "hint": "This secret Elven city is betrayed from within." },
    {"question": "What is the name of the human hero in who enetes Angband and escapes alive?", "options": ["Túrin", "Hurin", "Beren", "Beregond", "Haldir"], "answer": "Beren", "hint": "He falls in love with the most beautiful Elven lady."},
    {"question": "Who is the mother of Elrond and Elros?", "options": ["Idril", "Lúthien", "Galadriel", "Celebrían", "Varda"], "answer": "Idril", "hint": "She is an Elf of Gondolin and key in the tale of Tuor."},
    {"question": "What great enemy first corrupts Elves and Men in the legendarium?", "options": ["Sauron", "Ungoliant", "Morgoth", "Saruman", "Glaurung"], "answer": "Morgoth", "hint": "He is the original Dark Lord of the First Age."},
    {"question": "Who becomes King of the Havens after the downfall of Númenor?", "options": [ "Isildur", "Arvedui","Elendil", "Círdan", "Tar-Meneldur"], "answer": "Elendil", "hint": "He later co-founds the realms of Arnor and Gondor in the Third Age."},
    {"question": "In *Unfinished Tales*, what race are the Drúedain?", "options": ["Elves", "Dwarves", "Men of the West", "Wild Men of the Woods", "Orcs"], "answer": "Wild Men of the Woods", "hint": "They aid the Númenóreans."},
    {"question": "What creature carries the One Ring to the river's edge after Isildur's death?", "options": ["Bilbo", "Déagol", "Sméagol", "Sauron", "Lurtz"], "answer": "Sméagol", "hint": "He finds it while fishing with a relative."},
    {"question": "What is the name of the Dark Lord defeated by the Last Alliance?", "options": ["Morgoth", "Sauron", "Ungoliant", "Witch-king of Angmar", "Gothmog"], "answer": "Sauron", "hint": "He is first defeated at the end of the Second Age."},
    {"question": "What tree did Telperion and Laurelin belong to?", "options": ["Mallorn", "Laurelin & Telperion", "Trees of Valinor", "The White Tree", "The Two Trees"], "answer": "The Two Trees", "hint": "They lit Valinor before the Sun and Moon existed."},
    {"question": "Who was the father of Fëanor?", "options": ["Feä", "Maedhros", "Finwë", "Túrin", "Thingol"], "answer": "Finwë","hint": "He was High King of the Noldor."},
    {"question": "What forced the Noldor to leave Valinor?", "options": ["A plague", "Death of Finwë", "Theft of Silmarils", "War with Orcs", "Melkor's imprisonment"], "answer": "Theft of Silmarils", "hint": "This event sparked the First Age conflicts."},
    {"question": "Who raised Lúthien after her mother died?", "options": ["Thingol", "Melian", "Elrond", "Galadriel", "Celebrían"], "answer": "Melian", "hint": "She was a Maia who became Queen of Doriath."},
    {"question": "Which mountain did Glaurung first awaken under?", "options": ["Thangorodrim", "Mount Doom", "Caradhras", "Ered Nimrais", "Mount Gundabad"], "answer": "Thangorodrim", "hint": "It was a triple peak above Morgoth's fortress."},
    {"question": "What is the name of the River in Beleriand where the Noldor landed?", "options": ["Anduin", "Lhûn", "Brandywine", "Sirion", "Isen"], "answer": "Sirion", "hint": "Many First Age tales occur near it."},
    {"question": "What gift did Ulmo give to Turgon?", "options": ["A sword", "A hidden city", "A ring", "A horse", "A ship"], "answer": "A hidden city", "hint": "Ulmo's gift helped Turgon keep something precious safe from Morgoth for many years."},
    {"question": "What was the name of Aragorn's mother?", "options": ["Elwing", "Idril", "Galadriel", "Morwen", "Gilraen"], "answer": "Gilraen", "hint": "She raised him after his father's death."},
    {"question": "What is the Sindarin name for Rivendell?", "options": ["Lothlórien", "Minas Tirith", "Edhellond", "Imladris", "Thranduil"], "answer": "Imladris", "hint": "It means 'Deep Dale of the Cleft.'"},
    {"question": "Who is the Lord of the Eagles that helps Thorin & Company?", "options": ["Huan", "Beren", "Gwaihir", "Landroval", "Radagast"], "answer": "Gwaihir", "hint": "He also aids Gandalf later on."},
    {"question": "Which realm did Thranduil rule?", "options": ["Lothlórien", "Mirkwood", "Rivendell", "Gondor", "Dale"], "answer": "Mirkwood", "hint": "It's a great forest in the northeast of Middle-earth."},
    {"question": "What is the name of Éowyn's brother?", "options": ["Theodred", "Faramir", "Éomer", "Boromir", "Denethor"], "answer": "Éomer", "hint": "He becomes Marshal of the Riddermark."},
    {"question": "Which Valar is associated with fire and craftsmanship?", "options": ["Aulë", "Manwë", "Ulmo", "Yavanna", "Tulkas"], "answer": "Aulë", "hint": "He created the Dwarves."},
    {"question": "What was the name of the first Orc that Túrin killed?", "options": ["Gothmog", "Azog", "Bolg", "Uldor", "Snaga"], "answer": "Uldor", "hint": "It occurred during the Nirnaeth Arnoediad battle."},
    {"question": "Who is the Lady of Lórien that gifts the Fellowship cloaks?", "options": ["Galadriel", "Arwen", "Melian", "Celebrían", "Finduilas"], "answer": "Galadriel", "hint": "She is one of the mightiest of the Elves remaining."},
    {"question": "What was the original language of the Dwarves?", "options": ["Sindarin", "Quenya", "Adûnaic", "Westron", "Khuzdul"], "answer": "Khuzdul", "hint": "It was kept secret from other races."},
    {"question": "Who were the parents of Elrond?", "options": ["Túrin & Morwen", "Thingol & Melian", "Celeborn & Galadriel", "Finwë & Míriel", "Eärendil & Elwing"], "answer": "Eärendil & Elwing", "hint": "They played a major role in the fate of the Silmarils."},
    {"question": "Which Maia became the primary servant of Morgoth?", "options": ["Radagast", "Gandalf", "Saruman", "Sauron", "Ilmarë"], "answer": "Sauron", "hint": "He is Tolkien's main antagonist in the Second and Third Ages."},
    {"question": "What is the name of the land where Men first went in the east?", "options": ["Hildórien", "Aman", "Valinor", "Númenor", "Rhun"], "answer": "Hildórien", "hint": "It's referenced as the ancestral home of Men."},
    {"question": "Which creature did Beren and Lúthien defeat to claim a Silmaril?", "options": ["Ungoliant", "Carcharoth", "Glaurung", "Dragon of Mount Gram", "Watcher in the Water"], "answer": "Carcharoth", "hint": "He was a massive wolf guarding the treasure."},
    {"question": "Who was the first King of Númenor?", "options": ["Elros", "Elrond", "Isildur", "Ar-Pharazôn", "Anárion"], "answer": "Elros", "hint": "He was a Half-elven who chose to be counted among Men."},
    {"question": "What was the name of Morgoth's lieutenant in the First Age?", "options": ["Gothmog", "Sauron", "Ungoliant", "Azog", "Bolg"], "answer": "Gothmog", "hint": "He was the Lord of Balrogs."},
    {"question": "Who becomes King of Gondor at the end of the War of the Ring?", "options": ["Boromir", "Faramir", "Aragorn", "Théoden", "Denethor"], "answer": "Aragorn", "hint": "He is crowned in Minas Tirith after the city is freed from siege."},
    {"question": "Which Elf helped Beren and Lúthien escape from Sauron?", "options": ["Huan", "Thingol", "Carcharoth", "Finrod", "Maedhros"], "answer": "Finrod", "hint": "He sacrificed his life to help them."},
    {"question": "What is the name of the mountain where Smaug dwelt?", "options": ["Caradhras", "Mount Gram", "Erebor", "Thangorodrim", "Mindolluin"], "answer": "Erebor", "hint": "Also called the Lonely Mountain."},
    {"question": "Who was the captain of the Nazgûl?", "options": ["Khamûl", "The Mouth of Sauron", "Gríma Wormtongue", "The Witch-king of Angmar", "Saruman"], "answer": "The Witch-king of Angmar", "hint": "He leads the Ringwraiths and besieges Minas Tirith."},
    {"question": "Who taught Aragorn about healing and herbs?", "options": ["Gandalf", "Radagast", "Elrond",  "Galadriel", "Faramir"], "answer": "Elrond", "hint": "He is the lord of Imladris (Rivendell)."},
    {"question": "What is the name of the giant spider in Mirkwood that Bilbo encounters?", "options": ["Shelob", "Ungoliant", "Kankra", "Aragog", "Mirkspider"], "answer": "Kankra", "hint": "A spider guarding treasures and captured dwarves."},
    {"question": "Who becomes King under the Mountain after Thorin Oakenshield?", "options": ["Balin", "Fili", "Kili", "Dáin Ironfoot", "Gloin"], "answer": "Dáin Ironfoot", "hint": "He is Thorin's cousin who survives the Battle of Five Armies."},
    {"question": "What is the name of the sword of Éomer?", "options": ["Herugrim", "Andúril", "Glamdring", "Gúthwinë", "Sting"], "answer": "Gúthwinë", "hint": "Rohirric sword known for its family lineage."},
    {"question": "What is the name of the sea-faring land of Men that sinks?", "options": ["Gondor", "Harad", "Rhun", "Umbar", "Númenor"], "answer": "Númenor", "hint": "Its downfall is a warning about pride and defying the Valar."}]

advanced_questions = [{"question": "What is the name of the great fortress of Fingolfin in the First Age?", "options": ["Himring", "Tol-in-Gaurhoth", "Nargothrond", "Gondolin", "Angband"], "answer": "Himring", "hint": "It was captured and held by Morgoth multiple times."},
    {"question": "Who was the eldest son of Fëanor?", "options": ["Maglor", "Maedhros", "Celegorm", "Caranthir", "Curufin"], "answer": "Maedhros", "hint": "He is famous for being captured by Morgoth and rescued by his brothers."},
    {"question": "What are the names of the two great lamps created by the Valar before the Two Trees?", "options": ["Telperion and Laurelin", "Illuin and Ormal", "Vingilótë and Lorien", "Aule and Yavanna", "Manwe and Tulkas"], "answer": "Illuin and Ormal", "hint": "They illuminated the world during the earliest ages."},
    {"question": "Which Maia was sent by Eru Ilúvatar to teach the Noldor arts but later fell into shadow?", "options": ["Sauron", "Melian", "Olorin", "Aulë", "Ulmo"], "answer": "Sauron", "hint": "He served Morgoth and later became the Dark Lord in the Second and Third Ages."},
    {"question": "What was the original Elvish name of Gondolin?", "options": ["Turgon's City", "Nargothrond", "Ondolindë", "Hithlum", "Angband"], "answer": "Ondolindë", "hint": "It means 'The Rock of the Music of Water.'"},
    {"question": "Who was the first to find the hidden paths into Menegroth, the Thousand Caves?", "options": ["Melian", "Finrod Felagund", "Thingol", "Maeglin", "Beleg"], "answer": "Thingol", "hint": "The Sindarin King ruled Doriath and discovered its secrets."},
    {"question": "Which character is called the Hound of Valinor?", "options": ["Carcharoth", "Gothmog", "Beleg", "Huan", "Ancalagon"], "answer": "Huan", "hint": "He helps Beren and Lúthien in their quest for a Silmaril."},
    {"question": "What is the name of the spider that helped Morgoth to steal the Silmarils?", "options": ["Shelob", "Aragog", "Kankra", "Ungoliant", "Mirkspider"], "answer": "Ungoliant", "hint": "She was the mother of all spiders and she devoured herself due to hunger."},
    {"question": "What was the name of the river from which the Elves fled the destruction of Gondolin?", "options": ["Gelion", "Sirioneth", "Esgalduin", "Adurant", "Sirion"], "answer": "Sirion", "hint": "It flows from the northern mountains into Beleriand."},
    {"question": "Who was the Lord of the Balrogs of Morgoth?", "options": ["Azog", "Sauron", "Ungoliant", "Gothmog", "Thangorodrim"], "answer": "Gothmog", "hint": "He commanded in the Nirnaeth Arnoediad and Morgoth's wars."},
    {"question": "What is the name of the strognest dragon that destroyed three mountain peaks of Thangorodrim by fallig on them?", "options": ["Smaug", "Glaurung", "Chrysophylax Dives", "Scatha", "Ancalagon the Black"], "answer": "Ancalagon the Black", "hint": "This dragon was the mightiest of all Morgoth's fire-drakes in the First Age during the War of Wrath."},
    {"question": "Which Edain hero sailed with Eärendil to Aman carrying a Silmaril?", "options": ["Tuor", "Eärendil", "Húrin", "Turgon", "Finarfin"], "answer": "Eärendil", "hint": "He became the Evening Star after pleading to the Valar."}]

if "remaining_questions" not in st.session_state:
    st.session_state.remaining_questions = extra_questions.copy()
    random.shuffle(st.session_state.remaining_questions)

if "advanced_questions" not in st.session_state:
    st.session_state.advanced_questions = advanced_questions.copy()
    random.shuffle(st.session_state.advanced_questions)

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

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
                    add_book_enter()
                    st.success(f"Awesome! You've read: {st.session_state.book_list}")
                    if st.session_state.book_list:
                        df_books = pd.DataFrame({"Books Read": st.session_state.book_list})
                        st.subheader("Books you’ve read:")
                        st.dataframe(df_books, height=200)
                        if len(st.session_state.book_list) > 3:
                            st.session_state.quiz_unlocked = True
                            st.subheader("Conglatulations! You have unlocked the book quiz!")
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

if st.session_state.quiz_unlocked:
    if st.session_state.show_correct:
        st.success("Correct!")
        st.session_state.show_correct = False
    if st.session_state.quiz_step == 0:
        answer = st.radio(
            "What is the name of the only character who resisted the tempation of the one ring?", ["Samwise Gamgee", "Tom Bombadil", 'Gandalf', 'Pipin Took', 'Aragon'], key="q1")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("This charater is shown in The Fellowship of the Ring.")
        if st.button("Submit Answer"):
            if answer == "Tom Bombadil":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 1
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 1:
        answer2 = st.radio("What is the name of Gandalf's horse in second and third film?", ["Pony", "Krom", "Snowflake", "Shadowfax", "Lightbearer"], key="q2")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("He is the lord of all horses and incredibly fast, described in the Two Towers.")
        if st.button("Submit Answer"):
            if answer2 == "Shadowfax":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 2
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 2:
        answer3 = st.radio("In Minas Tirith, who carries the wounded King Théoden from the battlefield during the Battle of the Pelennor Fields?", ["Aragon", "Merry", "Gandalf", "Faramir", "Éowyn"], key="q3")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("This character is first shown in the Two Towers but this event happens in the Return of the King.")
        if st.button("Submit Answer"):
            if answer3 == "Éowyn":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 3
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 3:
        answer4 = st.radio("What is the Arkenstone also known as?", ["The White Gem of Gondor", "The Stone of Erebor", "The Jewel of Durin", "The Heart of the Mountain", "The King's Diamond"], key="q4")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("It was Thorin's most prized treasure, found deep within Erebor, dectribed in the Hobbit.")
        if st.button("Submit Answer"):
            if answer4 == "The Heart of the Mountain":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 4
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 4:
        answer5 = st.radio("Who originally owned the sword Sting before Bilbo?", ["Thorin Oakenshield", "Elrond", "An Elven king of Gondolin", "Aragorn", "Dain Ironfoot"], key="q5")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("Its true origin is revealed in Rivendell, during the Hobbit.")
        if st.button("Submit Answer"):
            if answer5 == "An Elven king of Gondolin":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 5
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 5:
        answer6 = st.radio("What gift does Galadriel give Frodo in Lothlórien?", ["An Elven cloak", "A silver horn", "A rope", "A star of Eärendil", "A sword"], key="q6")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("Something that will help him when in darkness, and he first uses it in Two Towers even tho he got it in the Fellowship of the Ring.")
        if st.button("Submit Answer"):
            if answer6 == "A star of Eärendil":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 6
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 6:
        answer7 = st.radio("What do the beacons of Gondor signal?", ["Victory over Mordor", "The crowning of the king",  "A call for aid from Rohan", "The fall of Minas Tirith", "The return of Gandalf"], key="q7")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("It happened in the Return of the King and in the movie diffetent characters set it on fire and see and deliver a message.")
        if st.button("Submit Answer"):
            if answer7 == "A call for aid from Rohan":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 7
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 7:
        answer8 = st.radio("Who frees Théoden from Saruman's influence?", ["Aragorn", "Gandalf", "Éomer", "Gríma Wormtongue", "Legolas"], key="q8")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("Character who 'dies' in the Fellowship of the Ring.")
        if st.button("Submit Answer"):
            if answer8 == "Gandalf":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 8
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 8:
        answer9 = st.radio("What kind of creature is Gollum originally?", ["Hobbit", "Man", "Dwarf", "Goblin", "Elf"], key="q9")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.radio("This creature's life was forever changed after discovering The one Ring and abide in dark places with prolonged lifespan.")
        if st.button("Submit Answer"):
            if answer9 == "Hobbit":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 9
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 9:
        answer10 = st.radio("Where did Saruman die?", ["Isengard", "Mordor", "Gondor", "Shire", "Rohan"], key="q10")
        if st.button("Hint"):
            st.session_state.show_hint = True
        if st.session_state.show_hint == True:
            st.write("It is compleatly wrong in the movies, in the book it happens in the Return of the King.")
        if st.button("Submit Answer"):
            if answer10 == "Shire":
                st.session_state.show_correct = True
                st.session_state.quiz_step = 10
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.text("Incorrect! Try again.")
    elif st.session_state.quiz_step == 10:
        if st.session_state.current_question is None and st.session_state.remaining_questions:
            st.session_state.current_question = st.session_state.remaining_questions.pop()
            st.session_state.show_hint = False
        if st.session_state.current_question:
            q = st.session_state.current_question
            answer = st.radio(q["question"], q["options"], key=f"q{st.session_state.quiz_step}")
            if st.button("Hint", key=f"hint{st.session_state.quiz_step}"):
                st.session_state.show_hint = True
            if st.session_state.show_hint:
                st.write(q["hint"])
            if st.button("Submit Answer", key=f"submit{st.session_state.quiz_step}"):
                if answer == q["answer"]:
                    st.session_state.show_correct = True
                    st.session_state.quiz_step = 10
                    st.session_state.current_question = None
                    st.session_state.show_hint = False
                    st.rerun()
                else:
                    st.error("Incorrect! Try again.")
        elif not st.session_state.remaining_questions:
            st.session_state.quiz_step = 11
            st.session_state.current_question = None
            st.rerun()
    elif st.session_state.quiz_step == 11:
        if st.session_state.current_question is None and st.session_state.advanced_questions:
            st.session_state.current_question = st.session_state.advanced_questions.pop()
            st.session_state.show_hint = False
        if st.session_state.current_question:
            q = st.session_state.current_question
            answer = st.radio(q["question"], q["options"], key=f"q_{q['question']}")
            if st.button("Hint", key=f"hint{st.session_state.quiz_step}"):
                st.session_state.show_hint = True
            if st.session_state.show_hint:
                st.write(q["hint"])
            if st.button("Submit Answer", key=f"submit{st.session_state.quiz_step}"):
                if answer == q["answer"]:
                    st.session_state.show_correct = True
                    st.session_state.quiz_step = 11
                    st.session_state.current_question = None
                    st.session_state.show_hint = False
                    st.rerun()
                else:
                    st.error("Incorrect! Try again.")
        elif not st.session_state.advanced_questions:
            st.session_state.quiz_step = 12
            st.success("Conglatulations! You have compleated the quiz! Your Tolkien knowledge is unparalleled!")
            st.session_state.current_question = None
