import streamlit as st
import math

from game import Game, Player, Time, Student
import static


if "page" not in st.session_state:
    st.session_state.page = "main"

if "game" not in st.session_state:
    st.session_state.game = Game()

g = st.session_state.game

def update(g): st.session_state.game = g

def goto(page): st.session_state.page = page

format_dict = {
    "sciences": "Science", 
    "humanities": "Humanities", 
    "com_skills": "Commercial Skills",
    "fine_arts": "Fine Arts",
    "life_skills": "Life Skills",
    "visual_art": "Visual Arts",
    "music": "Music",
    "perform": "Performing Arts",
    "poetry": "Poetry",
    "health": "Health and Fitness",
    "cooking": "Food and Nutrition",
    "mechanics": "Crafting and Mechanics",
    "oral_com": "Oral Communication",
    "animal_science": "Animal Science Club", 
    "soccer": "Football / Soccer", 
    "staff": "Staff Fencing",
    "debate": "Debate Team", 
    "band": "Marching Band", 
    "mancala": "Mancala Club", 
    "theater": "Theater", 
    "art_club": "Art Club", 
    "service": "Volunteer Service Club", 
    "newspaper": "School Newspaper",
    "school": "Social at School",
    "solo": "One-on-One",
    "group": "Group Activity",
    "resting": "Resting",
    "reading": "Reading",
    "practice": "Practicing Skills",
    "eating": "Eating Out",
    "traveling": "Traveling",
    "dropout": "Dropout Boy",
    "jock": "Jock Girl",
    "rich": "Rich Boy",
    "stuco": "StuCo Girl",
    "nerd": "Band Boy",
    "engineer": "Nerd Girl",
    "theater": "Theater Boy",
    "art": "Art Girl",
    "rival": "Rival Sydney",
    "mom": "Mom",
    "dad": "Dad",
    "brother": "Younger Brother",
    "granny": "Granny Bea",
    "sister": "Elder Sister",
    "homeroom": "Homeroom Teacher",
    "sponsor": "Newspaper Sponsor"
}

def initialize_new_game(input_data):
    ply = Player()
    ply.name = input_data[0]
    ply.att = input_data[1]
    ply.initialize_skills()
    ply.curriculum = input_data[2]
    ply.art_elective = input_data[3]
    ply.life_elective = input_data[4]
    ply.extracurriculars = input_data[5]
    return ply

def make_save_string(ply, week):
    save_string = ""
    # week
    if week < 10:
        save_string = save_string + '0' + str(week)
    else:
        save_string = save_string + static.encode[int(str(week)[0:-1])] + str(week)[-1]
    # attributes
    for a in ply.att:
        save_string = save_string + static.encode[ply.att[a]]
    # skills
    for s in ply.skills:
        save_string = save_string + static.encode[(math.floor(ply.skills[s]/10)*10)]
    # curriculum
    save_string = save_string + static.cdict[ply.curriculum] + static.cdict[ply.art_elective] + static.cdict[ply.life_elective]
    # class scores
    for cs in ply.class_points:
        save_string = save_string + static.encode[(math.floor(ply.class_points[cs]/10)*10)]
    # class scores quarter
    for csq in ply.class_points_quarter:
        save_string = save_string + static.encode[(math.floor(ply.class_points_quarter[csq]/10)*10)]
    # class grades
    for cg in ply.class_grades:
        save_string = save_string + static.encode[ply.class_grades[cg]]
    # rapport
    for r in ply.rapport:
        save_string = save_string + static.encode[(math.floor(ply.rapport[r]/10)*10)]
    # number of extracurriculars
    save_string = save_string + static.encode[len(ply.extracurriculars)]
    # extracurriculars
    for e in ply.extracurriculars:
        save_string = save_string + static.edict[e]
    # club ranks
    for cr in ply.club_ranks:
        save_string = save_string + static.encode[ply.club_ranks[cr]]
    # length of name
    save_string = save_string + static.encode[len(ply.name)]
    # name
    save_string = save_string + ply.name
    return save_string

def load_save_string(student_string):
    ply = Player()
    week = 1
    # week
    week = static.decode[student_string[0]] * 10 + int(student_string[1])
    # attributes
    index = 0
    for at in ply.att:
        ply.att[at] = static.decode[student_string[2 + index]]
        index += 1
    # skills
    index = 0
    for sk in ply.skills:
        ply.skills[sk] = static.decode[student_string[6 + index]]
        index += 1
    # curriculum
    ply.curriculum = static.cdict[student_string[26]]
    ply.art_elective = static.cdict[student_string[27]]
    ply.life_elective = static.cdict[student_string[28]]
    # class scores
    index = 0
    for cs in ply.class_points:
        ply.class_points[cs] = static.decode[student_string[29 + index]]
        index += 1
    # class scores quarter
    index = 0
    for csq in ply.class_points_quarter:
        ply.class_points_quarter[csq] = static.decode[student_string[34 + index]]
        index += 1
    # class grades
    index = 0
    for cg in ply.class_grades:
        ply.class_grades[cg] = static.decode[student_string[39 + index]]
        index += 1
    # rapport
    index = 0
    for r in ply.rapport:
        ply.rapport[r] = static.decode[student_string[44 + index]]
        index += 1
    # number of extracurriculars
    num_extracurriculars = static.decode[student_string[60]]
    # extracurriculars
    ply.extracurriculars = []
    for i in range(num_extracurriculars):
        ply.extracurriculars.append(static.edict[student_string[61 + i]])
    # club ranks
    index = 0
    for cr in ply.club_ranks:
        ply.club_ranks[cr] = static.decode[student_string[61 + num_extracurriculars + index]]
        index += 1
    # length of name
    name_length = static.decode[student_string[61 + 2 * num_extracurriculars]]
    # name
    for i in range(name_length):
        ply.name += student_string[62 + 2 * num_extracurriculars + i]
    return ply, week



def main_menu():
    st.header(f"Just Friends")
    with st.container(horizontal=True):
        st.button("New Game",on_click=goto, args=["new"])
        st.button("Load Game",on_click=goto, args=["load"])

def new_game():
    g = Game()
    with st.container(horizontal=True):
        st.header(f"ENROLLMENT FORM")
        st.button("Back to Main",on_click=goto, args=["main"], key="main_new")
    # name = st.text_input("Name: ")

    st.subheader("Curriculum")

    core = st.radio("Core Curriculum:", ["sciences", "humanities", "com_skills"], format_func=lambda x: format_dict[x])
    art = st.radio("Fine Arts Elective:", ["visual_art", "music", "perform", "poetry"], format_func=lambda x: format_dict[x])
    life = st.radio("Life Skills Elective:", ["health", "cooking", "mechanics", "oral_com"], format_func=lambda x: format_dict[x])

    extracurriculars = st.pills("Electives (Choose 1-3)", ["animal_science", "soccer", "staff", "debate", "band", "mancala", "theater", "art_club", "service", "newspaper"], selection_mode="multi", format_func=lambda x: format_dict[x])
    att = {"body": 1, "eyes": 1, "mind": 1, "heart": 1}
    st.subheader("Annual Physical")

    # presets
    # athletic: 5,4,2,3  (6,5,1,2)
    # studious: 2,3,5,4  (1,3,6,4)
    # sociable: 4,3,2,5  (3,3,2,6)
    # creative: 2,5,4,3  (1,6,4,3)
    defaults = [1,1,1,1]
    preset = st.segmented_control(
        label="Presets:",
        options=["athletic", "studious", "sociable", "creative"],
        format_func=lambda x: x.capitalize()
    )
    if preset == "athletic":
        defaults = [5,4,2,3]
    elif preset == "studious":
        defaults = [2,3,5,4]
    elif preset == "sociable":
        defaults = [4,3,2,5]
    elif preset == "creative":
        defaults = [2,5,4,3]
    att["body"] = st.slider("Body: ",1,7,defaults[0])
    att["eyes"] = st.slider("Eyes: ",1,7,defaults[1])
    att["mind"] = st.slider("Mind: ",1,7,defaults[2])
    att["heart"] = st.slider("Heart: ",1,7,defaults[3])
    total = sum(att.values())
    st.write(f"Points Remaining: {14 - total}")

    st.write("Special Notes: Patient's behavioral health scores indicate moderate to severe depression in line with failure to complete spring coursework. Treatment ongoing. Recommended for special permission to resit Year 10 National Exams on medical grounds.")

    submitted = st.button("Submit", disabled=(total != 14))
    if submitted:
        g.ply = initialize_new_game(["Rowan", att, core, art, life, extracurriculars])
        update(g)
        goto("loop")
        st.rerun()


def load_game():
    with st.container(horizontal=True):
        st.header("LOAD GAME")
        st.button("Back to Main",on_click=goto, args=["main"], key="main_new")
    save_string = st.text_input("Please paste your save string in the box!")
    submitted = st.button("Submit")
    if submitted:
        if len(save_string) < 73:
            st.error("Save string is too short!")
        else:
            ply, w = load_save_string(save_string)
            g.ply = ply
            g.t.load_time(w)
            update(g)
            goto("loop")
            st.rerun()


core_format_dict = {
    'sciences': 'Coursework: Sciences',
    'humanities': 'Coursework: Humanities',
    'com_skills': 'Coursework: Commercial Skills',
    'fine_arts': 'Coursework: Fine Arts',
    'life_skills': 'Coursework: Life Skills',
    "animal_science": "Extracurricular: Animal Science",
    "soccer": "Extracurricular: Soccer",
    "staff": "Extracurricular: Staff Fencing",
    "debate": "Extracurricular: Debate Team",
    "band": "Extracurricular: Marching Band",
    "mancala": "Extracurricular: Mancala Club",
    "theater": "Extracurricular: Theater",
    "art_club": "Extracurricular: Art Club",
    "service": "Extracurricular: Volunteer Service Club",
    "newspaper": "Extracurricular: School Newspaper",
    "rest": "Personal: Rest",
    "practice": "Personal: Practice Skills",
    "school": "Social: Be Personable (School)",
    "group": "Social: Group",
    "solo": "Social: One-on-One"
}

def core_loop():
    options = ['sciences',
                'humanities',
                'com_skills',
                'fine_arts',
                'life_skills',
                'rest',
                'practice',
                'school'
                ]
    group_ready = set()
    solo_ready = set()
    for friend in g.ply.rapport:
        if g.ply.rapport[friend] > 2:
            group_ready.add(friend)
        if g.ply.rapport[friend] > 4:
            solo_ready.add(friend)
    if len(group_ready) > 1:
        options.append('group')
    if len(solo_ready) > 0:
        options.append('solo')
    for ec in g.ply.extracurriculars:
        options.append(ec)

    st.header(f"Week {g.t.total_week}")

    weekly_plan = st.multiselect("Select 3 things to focus on this week",
                            options,
                            max_selections=3,
                            format_func=lambda x: core_format_dict[x]
                            )
    friends = []
    parameter = ""
    for task in weekly_plan:
        if task == "group":
            friends = st.multiselect(f"{format_dict[task]} with whom?", group_ready, max_selections=static.social["group"]["capacity"], format_func=lambda x: format_dict[x])
        elif task == "solo":
            friends = [st.selectbox(f"{format_dict[task]} with whom?", solo_ready, format_func=lambda x: format_dict[x])]
        elif task == "practice":
            parameter = st.selectbox(f"Practice which skill?", g.ply.skills, format_func=lambda x: x.capitalize())
    submitted = st.button("Advance",disabled=((len(weekly_plan)<3) or (("group" in weekly_plan or "solo" in weekly_plan) and len(friends) == 0) or g.t.total_week >= 105))
    update_container = st.container()

    st.divider()

    if submitted:
        updated = {"rapport": set(), "skills": set(), "clubs": set()}
        for task in weekly_plan:
            if task in static.courses:
                c_updated = g.advance_course(task)
                updated["skills"].update(c_updated["skills"])
                updated["rapport"].update(c_updated["rapport"])
                updated["clubs"].update(c_updated["clubs"])
                update(g)
            elif task in static.extracurriculars:
                e_updated = g.advance_extracurricular(task)
                updated["skills"].update(e_updated["skills"])
                updated["rapport"].update(e_updated["rapport"])
                updated["clubs"].update(e_updated["clubs"])
                update(g)
            elif task in static.social:
                s_updated = g.advance_social(task, friends)
                updated["skills"].update(s_updated["skills"])
                updated["rapport"].update(s_updated["rapport"])
                updated["clubs"].update(s_updated["clubs"])
                update(g)
            elif task in static.personal:
                p_updated = g.advance_personal(task, parameter)
                updated["skills"].update(p_updated["skills"])
                updated["rapport"].update(p_updated["rapport"])
                updated["clubs"].update(p_updated["clubs"])
                update(g)
        if g.t.total_week < 105:
            grades_updated = g.update_grades({"sciences":1,"humanities":1,"com_skills":1,"fine_arts":1,"life_skills":1})
            update_container.empty()
            g.t.advance_time()
            if len(updated["skills"]) > 0:
                update_container.write(f"Skills updated!! {', '.join([s.capitalize() for s in updated['skills']])} increased!")
            if len(updated["rapport"]) > 0:
                update_container.write(f"Rapport updated!! Friendship with {', '.join([r.capitalize() for r in updated['rapport']])} increased!")
            if len(updated["clubs"]) > 0:
                update_container.write(f"Club Ranks updated!! {', '.join([c.capitalize() for c in updated['clubs']])} increased!")
            if grades_updated:
                update_container.write(f"Exams have been graded!\nSciences: {g.ply.class_grades['sciences']}, Humanities: {g.ply.class_grades['humanities']}, Com Skills: {g.ply.class_grades['com_skills']}, Fine Arts: {g.ply.class_grades['fine_arts']}, Life Skills: {g.ply.class_grades['life_skills']}")
            update(g)
        else:
            st.header("CONGRATULATIONS! You have graduated and reached the end of the game!")
    save = make_save_string(g.ply, g.t.total_week)
    st.write("Copy your save below to preserve current progress!")
    st.code(save, wrap_lines=True)

    with st.sidebar:
        st.header("Menu")
        st.write(f"{static.calendar["month_names"][g.t.month]} {str(g.t.day)}, {str(g.t.year)}")
        quarter = static.calendar["school"][g.t.sc_index]
        st.write(f"{quarter["quarter"].capitalize()} Quarter, {quarter["semester"].capitalize()} Year {quarter["school_year"]}")
        st.divider()
        tab1, tab2, tab3, tab4 = st.tabs([g.ply.name, "Enrollment", "Rapport", "Quit"])
        with tab1:
            st.subheader("Attributes")
            with st.container(horizontal = True):
                st.write("Body: " + str(g.ply.att["body"]))
                st.write("Eyes: " + str(g.ply.att["eyes"]))
                st.write("Mind: " + str(g.ply.att["mind"]))
                st.write("Heart: " + str(g.ply.att["heart"]))
            st.divider()
            st.subheader("Skills:")
            with st.container(horizontal = True):
                for s in g.ply.skills:
                    st.write(f"{s.capitalize()}: {g.ply.skills[s]}")
                    # st.write(str(s).capitalize() + ": " + str(math.floor(g.ply.skills[s]/10)))
        with tab2:
            st.subheader("Course Grades")
            with st.container(horizontal = True):
                for c in g.ply.class_grades:
                    if c == "fine_arts":
                        st.write(f"{format_dict[g.ply.art_elective]}: {g.ply.class_grades[c]}")
                    elif c == "life_skills":
                        st.write(f"{format_dict[g.ply.life_elective]}: {g.ply.class_grades[c]}")
                    else:
                        st.write(f"{format_dict[c]}: {g.ply.class_grades[c]}")
            st.divider()
            st.subheader("Extracurriculars")
            for e in g.ply.extracurriculars:
                st.write(f"{format_dict[e]}: Rank {g.ply.club_ranks[e]}")
                # st.write(f"{format_dict[e]}: Rank {str(math.floor(g.ply.club_ranks[e]/10))}")
        with tab3:
            with st.container(horizontal = True):
                for f in g.ply.rapport:
                    st.write(f"{format_dict[f]}: {g.ply.rapport[f]}")
                    # st.write(f"{format_dict[f]}: " + str(math.floor(g.ply.rapport[f]/10)))
        with tab4:
            st.button("Quit to Main Menu",on_click=goto, args=["main"])
            st.write("BE SURE TO COPY YOUR SAVE!")
        st.divider()



if st.session_state.page == "loop":
    core_loop()
elif st.session_state.page == "new":
    new_game()
elif st.session_state.page == "load":
    load_game()
elif st.session_state.page == "main":
    main_menu()


with st.bottom:
    st.caption("Just Friends v 0.0.1.1")


# 015432ttssrrqqrrqqppppooee25800000000005555500Veopo0000000031890000000005Rowan



