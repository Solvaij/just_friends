import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = 0

placeholder = st.empty()

def mainbutton(): st.session_state.page = 0
def contbutton(): st.session_state.page = 1
def newbutton(): st.session_state.page = 2
def loadbutton(): st.session_state.page = 3

if st.session_state.page == 0:
    with placeholder.container():
        st.header(f"Just Friends")
        st.button("Continue",on_click=contbutton,disabled=(True))
        st.button("New Game",on_click=newbutton)
        st.button("Load Game",on_click=loadbutton)



def load_student_string(student_string):
    st.session_state.page = 4



def cont_game():
    pass

if st.session_state.page == 1:
    placeholder.text(f"Continue your local save:")



def new_game():
    pass

def valid_student():
    return True

if st.session_state.page == 2:
    with placeholder.container():
        st.header(f"ENROLLMENT FORM")
        with st.form("admission"):
            st.header("Curriculum")

            core = st.radio("Core Curriculum:", ["Science", "Humanities", "Commercial Skills"])
            art = st.radio("Fine Arts Elective:", ["Visual Art", "Music", "Performing Arts", "Poetry"])
            life = st.radio("Life Skills Elective:", ["Health and Fitness", "Food and Nutrition", "Mechanics and Handicraft", "Oral Communication"])

            electives = st.pills("Electives (Choose 1-3)", ["Animal Science Club", "Soccer", "Staff Fencing", "Debate Club", "Marching Band", "Mancala Club", "Theater", "Art Club", "Service Club", "Newspaper"], selection_mode="multi")

            st.header("Annual Physical")
            body = st.slider("Body: ",1,7)
            eyes = st.slider("Eyes: ",1,7)
            mind = st.slider("Mind: ",1,7)
            heart = st.slider("Heart: ",1,7)

            st.write("Special Notes: Patient’s behavioral health scores indicate moderate to severe depression in line with failure to complete spring coursework. Treatment ongoing. Recommended for special permission to resit Year 10 National Exams on medical grounds.")
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("Core Curriculum: ", core)
                st.write("Art Elective: ", art)
                st.write("Life Skills Elective: ", life, "\n")
                st.write("Extracurriculars: ", str(electives), "\n")
                st.write("Body: ", str(body), "Eyes: ", str(eyes), "Mind: ", str(mind), "Heart ", str(heart), "\n")

        student_string = ""
        st.button("Confirm",on_click=load_student_string(student_string),disabled=(not valid_student()))


def load_game():
    pass

if st.session_state.page == 3:
    with placeholder.container():
        st.header(f"Load GAME")
        st.text("Enter your save string: ")


def loop():
    pass

if st.session_state.page == 4:
    placeholder.text(f"Welcome to the main game loop.")



st.button("Main Menu",on_click=mainbutton,disabled=(st.session_state.page == 0))



