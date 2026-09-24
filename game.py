import json
import math
import os
import random

import static


class Player():
    def __init__(self):
        self.name = "Rowan"
        self.att = {
            "body": 1,
            "eyes": 1,
            "mind": 1,
            "heart": 1
        }
        self.skills = {
            "strength": 1,
            "vigor": 1,
            "acrobatics": 1,
            "instinct": 1,
            "body_mech": 1,
            "cooking": 1,
            "presence": 1,
            "comfort": 1,
            "motor_skill": 1,
            "reaction": 1,
            "perception": 1,
            "making": 1,
            "composure": 1,
            "arts": 1,
            "recall": 1,
            "logic": 1,
            "communication": 1,
            "persuasion": 1,
            "empathy": 1,
            "willpower": 1
        }
        self.curriculum = "com_skills"
        self.art_elective = "visual_art"
        self.life_elective = "health"
        self.extracurriculars = {}
        self.class_scores = {
            "sciences": 0,
            "humanities": 0,
            "com_skills": 0,
            "fine_arts": 0,
            "life_skills": 0
        }
        self.class_scores_quarter = {
            "sciences": 0,
            "humanities": 0,
            "com_skills": 0,
            "fine_arts": 0,
            "life_skills": 0
        }
        self.class_grades = {
            "sciences": 5,
            "humanities": 5,
            "com_skills": 5,
            "fine_arts": 5,
            "life_skills": 5
        }
        self.club_ranks = {
            "animal_science": 0,
            "soccer": 0,
            "staff": 0,
            "debate": 0,
            "band": 0,
            "mancala": 0,
            "theater": 0,
            "art_club": 0,
            "service": 0,
            "newspaper": 0
        }
        self.rapport = {
            "dropout": 0,
            "jock": 0,
            "rich": 0,
            "stuco": 0,
            "nerd": 0,
            "engineer": 0,
            "theater": 0,
            "art": 0,
            "rival": 0,
            "brother": 0,
            "mom": 0,
            "dad": 0,
            "granny": 0,
            "sister": 0,
            "sponsor": 0,
            "homeroom": 0
        }

    def initialize_skills(self):
        self.skills = {
            "strength": (self.att["body"]+self.att["body"])*10,
            "vigor": (self.att["body"]+self.att["body"])*10,
            "acrobatics": (self.att["body"]+self.att["eyes"])*10,
            "instinct": (self.att["body"]+self.att["eyes"])*10,
            "body_mech": (self.att["body"]+self.att["mind"])*10,
            "cooking": (self.att["body"]+self.att["mind"])*10,
            "presence": (self.att["body"]+self.att["heart"])*10,
            "comfort": (self.att["body"]+self.att["heart"])*10,
            "motor_skill": (self.att["eyes"]+self.att["eyes"])*10,
            "reaction": (self.att["eyes"]+self.att["eyes"])*10,
            "perception": (self.att["eyes"]+self.att["mind"])*10,
            "making": (self.att["eyes"]+self.att["mind"])*10,
            "composure": (self.att["eyes"]+self.att["heart"])*10,
            "arts": (self.att["eyes"]+self.att["heart"])*10,
            "recall": (self.att["mind"]+self.att["mind"])*10,
            "logic": (self.att["mind"]+self.att["mind"])*10,
            "communication": (self.att["mind"]+self.att["heart"])*10,
            "persuasion": (self.att["mind"]+self.att["heart"])*10,
            "empathy": (self.att["heart"]+self.att["heart"])*10,
            "willpower": (self.att["heart"]+self.att["heart"])*10
        }

class Time():
    def __init__(self):
        self.total_week = 1
        self.year = 1983
        self.month = 8
        self.day = 1
        self.sc_index = 0

    def load_time(self, wk):
        while self.total_week < wk:
            self.advance_time()

    def advance_time(self):
        self.total_week += 1
        self.day += 7
        days_this_month = static.calendar["month_days"][self.month]
        if self.month == 2 and (self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)):
            days_this_month = 29
        if self.day > days_this_month:
            self.day -= days_this_month
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        sc_year = (static.calendar["school"][self.sc_index]["year"])
        sc_end = static.calendar["school"][self.sc_index]["end_date"]
        end_month, end_day = sc_end.split("-")
        if int(end_month) == 1 and self.month == 12:
            pass
        elif (self.month > int(end_month)) or (self.month == int(end_month) and self.day > int(end_day)):
            self.sc_index += 1

class Student():
    def __init__(self, name, curriculum_track, art_elective, life_elective, extracurriculars):
        self.name = name
        self.curriculum_track = curriculum_track
        self.art_elective = art_elective
        self.life_elective = life_elective
        self.extracurriculars = extracurriculars
        self.rapport = 0
        self.rapport_rank = 0

class Game():
    def __init__(self):
        self.save_file = "last_save.txt"
        self.t = Time()
        self.ply = Player()
        self.students = {
            "dropout": Student("Ness", "sciences", "art", "health", {"animal_science"}),
            "jock": Student("Jock", "sciences", "music", "health", {"football"}),
            "rich": Student("Rich", "humanities", "art", "cooking", {"staff_arts"}),
            "stuco": Student("StuCo", "humanities", "poetry", "craft", {"debate"}),
            "nerd": Student("Nerd", "sciences", "music", "craft", {"marching_band"}),
            "engineer": Student("Autumn", "sciences", "music", "oral_com", {"mancala"}),
            "theater": Student("Theater", "humanities", "perform", "oral com", {"theater"}),
            "art": Student("Art", "humanities", "art", "craft", {"art_club"}),
            "rival": Student("Rival", "humanities", "poetry", "craft", {"volunteer"})
        }
        self.course_enroll = {
            "sciences": {"engineer", "nerd", "rich"},
            "humanities": {"stuco", "art", "theater"},
            "com_skills": {"jock", "dropout"},
            "visual_art": {"art"},
            "music": {"nerd"},
            "perform": {"theater"},
            "poetry": {"stuco"},
            "health": {"jock"},
            "cooking": {"rich"},
            "mechanics": {"dropout"},
            "oral_com": {"engineer"}
        }
        self.ec_enroll = {
            "soccer": {"jock"},
            "staff": {"rich"},
            "debate": {"stuco"},
            "band": {"nerd"},
            "mancala": {"engineer"},
            "theater": {"theater"},
            "art": {"art"},
            "animal_science": {"dropout"},
            "service": {"rival"},
            "newspaper": set()
        }

    def advance(self, weekly_focus):
        for focus in weekly_focus:
            ftype = focus.split("-")[0]
            findex = static.focus_codes[focus]
            if ftype == "ed":
                course = dict()
                if findex == "fine_arts":
                    course = static.courses[self.ply.art_elective]
                elif findex == "life_skills":
                    course = static.courses[self.ply.life_elective]
                else:
                    course = static.courses[findex]
                print(f"Education focus selected: {course['name']}")
                self.advance_course(course)
            elif ftype == "ex":
                exc = static.extracurriculars[findex]
                print(f"Extracurricular focus selected: {exc['name']}")
                self.advance_extracurricular(exc)
            elif ftype == "so":
                soc = static.social[findex]
                print(f"Social focus selected: {soc['name']}")
                self.advance_social(soc)
            elif ftype == "pr":
                per = static.personal[findex]
                print(f"Personal focus selected: {per['name']}")
                self.advance_personal(per)
        for person in self.ply.rapport:
            if person in self.students:
                old_rap = self.students[person].rapport
                new_rap = self.ply.rapport[person]
                if new_rap > 200:
                    new_rap = 200
                if old_rap < new_rap:
                    self.students[person].rapport = new_rap
                    self.students[person].rapport_rank = math.floor(new_rap / 10)
        self.t.advance_time()

    def advance_course(self, course):
        for character in self.course_enroll[course]:
            self.ply.rapport[character] += 1
        for skill in static.courses[course]["skills"]:
            self.ply.skills[skill] += 1
        if course in ("sciences", "humanities", "com_skills"):
            if self.ply.curriculum == course:
                self.ply.class_scores[course] += 3
                self.ply.class_scores_quarter[course] += 3
            else:
                self.ply.class_scores[course] += 2
                self.ply.class_scores_quarter[course] += 2
        elif course in ("visual_art", "music", "perform", "poetry"):
            self.ply.class_scores["fine_arts"] += 4
            self.ply.class_scores_quarter["fine_arts"] += 4
        elif course in ("health", "cooking", "mechanics", "oral_com"):
            self.ply.class_scores["life_skills"] += 4
            self.ply.class_scores_quarter["life_skills"] += 4
        for course in self.ply.class_scores:
            sc_index = self.t.sc_index
            if static.calendar["school"][sc_index]["quarter"] in {"midterms", "finals", "exams"}:
                self.ply.class_grades[course] = min(self.ply.class_scores_quarter[course], 5)
            elif static.calendar["school"][sc_index-1]["quarter"] in {"midterms", "finals", "exams"}:
                self.ply.class_scores_quarter[course] = 0

    def advance_extracurricular(self, ec):
        for character in self.ec_enroll[ec]:
            self.ply.rapport[character] += 1
        skill_count = 0
        for skill in static.extracurriculars[ec]["skills"]:
            if skill_count < 2:
                self.ply.skills[skill] += 2
                skill_count += 1
            else:
                self.ply.skills[skill] += 1
            if self.ply.skills[skill] > 300:
                self.ply.skills[skill] = 300

    def advance_social(self, social, friends):
        if social == "school":
            for character in self.students.keys():
                self.ply.rapport[character] += 1
                if self.ply.rapport[character] > 200:
                    self.ply.rapport[character] = 200
        elif social == "group":
            for student in friends:
                self.ply.rapport[student] += 2
                if self.ply.rapport[student] > 200:
                    self.ply.rapport[student] = 200
        elif social == "solo":
            self.ply.rapport[friends[0]] += 5
            if self.ply.rapport[friends[0]] > 200:
                self.ply.rapport[friends[0]] = 200

    def advance_personal(self, personal, parameter):
        if personal == "practice":
            self.ply.skills[parameter] += 5
            if self.ply.skills[parameter] > 300:
                self.ply.skills[parameter] = 300
        elif personal == "rest":
            skill = random.choice(list(self.ply.skills.keys()))
            if random.randint(1, 20) > math.floor(self.ply.skills[skill]/10):
                self.ply.skills[skill] += 10
            if self.ply.skills[skill] > 300:
                self.ply.skills[skill] = 300











# # current level up systems makes extracurriculars extremely strong for leveling skills
# # 6 points total distributed into skills for each extracurricular focuses as opposed to 1 or 0
# # classwork improves your grades and can up relations with multiple students
# # social is the fastest way to improve classmate relations but only rarely impacts skills


#         ## SOCIAL FOCUSES

#         elif focus == "so-l":
#             for character in glob.classmates["sciences"]:
#                 ply.rapport[character] += 1
#             for character in glob.classmates["humanities"]:
#                 ply.rapport[character] += 1
#             for character in glob.classmates["com_skills"]:
#                 ply.rapport[character] += 1

#         elif focus == "so-w":
#             ply.rapport["rival"] += 5

#         elif focus == "so-a":
#             for character in glob.classmates[ply.curriculum_track]:
#                 ply.rapport[character] += 3

#         elif focus == "so-we":
#             ply.rapport["rival"] += 10

#         elif focus == "so-g":
#             for character in glob.classmates[ply.curriculum_track]:
#                 ply.rapport[character] += 4

#         elif focus == "so-h":
#             for character in glob.classmates["sciences"]:
#                 ply.rapport[character] += 3
#             for character in glob.classmates["humanities"]:
#                 ply.rapport[character] += 3
#             for character in glob.classmates["com_skills"]:
#                 ply.rapport[character] += 3



# class Student():
#     def __init__(self, name, curriculum_track, art_elective, life_elective, extracurriculars):
#         self.name = name
#         self.curriculum_track = curriculum_track
#         self.art_elective = art_elective
#         self.life_elective = life_elective
#         self.extracurriculars = extracurriculars
#         self.rapport = 0
#         self.rapport_rank = 0

# class Global():
#     def __init__(self):
#         self.time = {"total_week": 1, "year": 1983, "month": 8, "day": 1, "sc_index": 0}
#         self.save_file = "last_save.txt"
#         self.students = {
#             "dropout": Student("Ness", "sciences", "art", "health", {"animal_science"}),
#             "jock": Student("Jock", "sciences", "music", "health", {"football"}),
#             "rich": Student("Rich", "humanities", "art", "cooking", {"staff_arts"}),
#             "stuco": Student("StuCo", "humanities", "poetry", "craft", {"debate"}),
#             "nerd": Student("Nerd", "sciences", "music", "craft", {"marching_band"}),
#             "engineer": Student("Autumn", "sciences", "music", "oral_com", {"mancala"}),
#             "theater": Student("Theater", "humanities", "perform", "oral com", {"theater"}),
#             "art": Student("Art", "humanities", "art", "craft", {"art_club"}),
#             "rival": Student("Rival", "humanities", "poetry", "craft", {"volunteer"})
#         }
#         self.course_enroll = {
#             "sciences": {"engineer", "nerd", "rich"},
#             "humanities": {"stuco", "art", "theater"},
#             "com_skills": {"jock", "dropout"},
#             "visual_art": {"art"},
#             "music": {"nerd"},
#             "perform": {"theater"},
#             "poetry": {"stuco"},
#             "health": {"jock"},
#             "cooking": {"rich"},
#             "mechanics": {"dropout"},
#             "oral_com": {"engineer"}
#         }
#         self.ec_enroll = {
#             "soccer": {"jock"},
#             "staff": {"rich"},
#             "debate": {"stuco"},
#             "band": {"nerd"},
#             "mancala": {"engineer"},
#             "theater": {"theater"},
#             "art": {"art"},
#             "animal_science": {"dropout"},
#             "service": {"rival"},
#             "newspaper": set()
#         }

#     def load_time(self, wk):
#         while self.time["total_week"] < wk:
#             self.advance_time()

#     def advance_time(self):
#         self.time["total_week"] += 1
#         self.time["day"] += 7
#         days_this_month = static.calendar["month_days"][self.time["month"]]
#         if self.time["month"] == 2 and (self.time["year"] % 4 == 0 and (self.time["year"] % 100 != 0 or self.time["year"] % 400 == 0)):
#             days_this_month = 29
#         if self.time["day"] > days_this_month:
#             self.time["day"] -= days_this_month
#             self.time["month"] += 1
#             if self.time["month"] > 12:
#                 self.time["month"] = 1
#                 self.time["year"] += 1
#         sc_year = (static.calendar["school"][self.time["sc_index"]]["year"])
#         sc_end = static.calendar["school"][self.time["sc_index"]]["end_date"]
#         end_month, end_day = sc_end.split("-")
#         if int(end_month) == 1 and self.time["month"] == 12:
#             pass
#         elif (self.time["month"] > int(end_month)) or (self.time["month"] == int(end_month) and self.time["day"] > int(end_day)):
#             self.time["sc_index"] += 1

# class Game():
#     def __init__(self):
#         self.glob = Global()
#         self.ply = Player()

#     def main_menu(self):
#         menu_choice = "0"
#         while menu_choice not in ("4", "quit"):
#             print("\nMenu Options:")
#             if os.path.isfile(os.path.join(os.path.dirname(__file__), "last_save.txt")):
#                 print("1. Continue Last Save")
#             print("2. New Game")
#             print("3. Load Game")
#             print("4. Quit Game\n")
#             menu_choice = input("c[MAIN] >> ")
#             if menu_choice.lower() in ("1", "continue"):
#                 self.load("last_save.txt")
#                 self.input_cycle()
#             elif menu_choice.lower() in ("2", "new"):
#                 self.new_game()
#                 self.input_cycle()
#             elif menu_choice.lower() in ("3", "load"):
#                 filename = input("Enter the name of save file to load: ")
#                 self.load(filename)
#                 self.input_cycle()
#             elif menu_choice.lower() in ("4", "quit", "q"):
#                 yn = input("\nAre you sure you want to quit? (y/n): ")
#                 if yn.lower() in {"y", "yes", "q", "quit"}:
#                     exit()

#     def new_game(self):
#         self.glob = Global()
#         self.ply = Player()
#         quit_to_main = False
#         print("\nWelcome to Just Friends!")
#         self.ply.name = self.input_confirm("Please enter your name: ", self.ply.name)
#         quit_to_main = self.input_attributes()
#         if quit_to_main:
#             return
#         quit_to_main = self.input_schedule()
#         if quit_to_main:
#             return
#         self.save()

#     def input_confirm(self, text, default="", valid=None):
#         confirmed = False
#         while not confirmed:
#             response = input(text) or default
#             if valid and response.lower() not in valid:
#                 print(f"\nInvalid input. Please try again.")
#                 continue
#             yn = input(f"\nConfirm '{response}'? (y/n): ").lower()
#             if yn in {"y", "yes"}:
#                 confirmed = True
#                 return response.lower()

#     def input_attribute(self, attribute, points):
#         att = ""
#         valid_att = False
#         while not valid_att:
#             att = input(f"{attribute.capitalize()}: ")
#             if att.lower() in {"q", "quit"}:
#                 return "q"
#             elif att.lower() in {"r", "restart"}:
#                 return "r"
#             elif not att.isdigit() or not (1 <= int(att) <= 7):
#                 print("\nInvalid input. Please enter a number between 1 and 7.\n")
#                 continue
#             elif int(att) > points + 1:
#                 print(f"\nInvalid input. You only have {points} points remaining.\n")
#                 continue
#             valid_att = True
#         return int(att)

#     def input_attributes(self):
#         att_confirmed = False
#         body, eyes, mind, heart = "", "", "", ""
#         restart = False
#         while not att_confirmed:
#             points = 10
#             print("\nPlease enter your scores for body, eyes, mind, and heart between 1 and 7." \
#                     "\nEach score starts at 1 and you have 10 points to distribute." \
#                     "\nType r or restart to start over.")

#             for att in ["body", "eyes", "mind", "heart"]:
#                 value = self.input_attribute(att, points)
#                 if value == "q":
#                     return True
#                 elif value == "r":
#                     restart = True
#                     break
#                 else:
#                     if att == "body":
#                         body = value
#                     elif att == "eyes":
#                         eyes = value
#                     elif att == "mind":
#                         mind = value
#                     elif att == "heart":
#                         heart = value
#                 points -= (value-1)

#             if restart:
#                 restart = False
#                 continue

#             print(f"\nPlayer's scores:\n{'Body: ' + str(body):<10} {'Eyes: ' + str(eyes):<10} {'Mind: ' + str(mind):<10} {'Heart: ' + str(heart):<10}")
#             if points > 0:
#                 print(f"\nWarning! Not all points allocated! {points} points remaining!")
#             yn = input("\nConfirm these attributes? (y/n): ").lower()
#             if yn in {"y", "yes"}:
#                 att_confirmed = True
#                 self.ply.att["body"] = int(body)
#                 self.ply.att["eyes"] = int(eyes)
#                 self.ply.att["mind"] = int(mind)
#                 self.ply.att["heart"] = int(heart)
#                 self.ply.init_skills()
#         return False

#     def input_schedule(self):
#         print("\nPlease enter your Program of Study.")

#         print("\nSelect your core curriculum:")
#         print(f"Science (s)".ljust(20) + f"Humanities (h)".ljust(20) + f"Commercial Skills (c)")
#         core = self.input_confirm("\nCurriculum (s/h/c): ", "com_skills", (static.courses["sciences"]["alts"] | static.courses["humanities"]["alts"] | static.courses["com_skills"]["alts"]))
#         if core in static.courses["sciences"]["alts"]:
#             core = "sciences"
#         elif core in static.courses["humanities"]["alts"]:
#             core = "humanities"
#         elif core in static.courses["com_skills"]["alts"]:
#             core = "com_skills"
#         self.ply.curriculum = core

#         print("\nSelect your Fine Art elective:")
#         print(f"Visual Arts (va)".ljust(20) + f"Music (mu)".ljust(20) + f"Performing Arts (pa)".ljust(20) + f"Poetry (po)")
#         arts = self.input_confirm("\nFine Art (va,mu,pa,po): ", "visual_art", (static.courses["visual_art"]["alts"] | static.courses["music"]["alts"] | static.courses["perform"]["alts"] | static.courses["poetry"]["alts"]))
#         if arts in static.courses["visual_art"]["alts"]:
#             arts = "visual_art"
#         elif arts in static.courses["music"]["alts"]:
#             arts = "music"
#         elif arts in static.courses["perform"]["alts"]:
#             arts = "perform"
#         elif arts in static.courses["poetry"]["alts"]:
#             arts = "poetry"
#         self.ply.art_elective = arts

#         print("\nSelect your Life Skills elective:")
#         print(f"Health and Fitness (hf)".ljust(20) + f"Food and Nutrition (fn)".ljust(20) + f"Mechanics and Crafting (mc)".ljust(20) + f"Oral Communication (oc)")
#         life = self.input_confirm("\nLife Skills (hf,fn,mc,oc): ", "health", (static.courses["health"]["alts"] | static.courses["cooking"]["alts"] | static.courses["mechanics"]["alts"] | static.courses["oral_com"]["alts"]))
#         if life in static.courses["health"]["alts"]:
#             life = "health"
#         elif life in static.courses["cooking"]["alts"]:
#             life = "cooking"
#         elif life in static.courses["mechanics"]["alts"]:
#             life = "mechanics"
#         elif life in static.courses["oral_com"]["alts"]:
#             life = "oral_com"
#         self.ply.life_elective = life

#         print("\nSelect your extracurricular activities:")

#     def save(self, filename="last_save.txt"):
#         new_filename = input("\nEnter filename, or press ENTER to quicksave: ")
#         if new_filename and (new_filename != ""):
#             filename = new_filename
#         with open(filename, "w") as f:
#             json.dump({
#                 "time": self.glob.time,
#                 "ply_name": self.ply.name,
#                 "ply_att": self.ply.att,
#                 "ply_skills": self.ply.skills,
#                 "ply_curriculum": self.ply.curriculum,
#                 "ply_art_elective": self.ply.art_elective,
#                 "ply_life_elective": self.ply.life_elective,
#                 "ply_extracurriculars": self.ply.extracurriculars,
#                 "ply_class_scores": self.ply.class_scores,
#                 "ply_class_scores_quarter": self.ply.class_scores_quarter,
#                 "ply_class_grades": self.ply.class_grades,
#                 "ply_club_ranks": self.ply.club_ranks,
#                 "ply_rapport": self.ply.rapport
#             }, f)

#     def load(self, filename):
#         try:
#             with open(filename, "r") as f:
#                 data = json.load(f)
#                 self.glob.time = data["time"]
#                 self.ply.name = data["ply_name"]
#                 self.ply.att = data["ply_att"]
#                 self.ply.skills = data["ply_skills"]
#                 self.ply.curriculum = data["ply_curriculum"]
#                 self.ply.art_elective = data["ply_art_elective"]
#                 self.ply.life_elective = data["ply_life_elective"]
#                 self.ply.extracurriculars = data["ply_extracurriculars"]
#                 self.ply.class_scores = data["ply_class_scores"]
#                 self.ply.class_scores_quarter = data["ply_class_scores_quarter"]
#                 self.ply.class_grades = data["ply_class_grades"]
#                 self.ply.club_ranks = data["ply_club_ranks"]
#                 self.ply.rapport = data["ply_rapport"]
#         except FileNotFoundError:
#             print(f"Save file '{filename}' not found.")

#     def input_cycle(self):
#         confirm_quit = False
#         user_input = ""
#         while not confirm_quit:
#             user_input = input("c[_] >> ")
#             if user_input.lower() in {"quit", "q", "exit", "stop", "close"}:
#                 yn = input("\nAre you sure you want to quit? (y/n): ")
#                 if yn.lower() in {"y", "yes", "q", "quit"}:
#                     confirm_quit = True
#             elif user_input.lower() in {"help", "h"}:
#                 print("\nAvailable commands: quit, help, menu, focus\n")
#             elif user_input.lower() in {"menu", "m"}:
#                 menu_choice = "0"
#                 while menu_choice not in {"7", "exit", "e", "q", "quit"}:
#                     print("\nMenu Options:")
#                     print("\n1. View Calendar")
#                     print("2. View Skills")
#                     print("3. View Rapport")
#                     print("4. View Enrollment")
#                     print("5. View Focus Codes")
#                     print("6. Save Game")
#                     print("7. Exit Menu\n")
#                     menu_choice = input("c[MENU] >> ")
#                     if menu_choice in {"1", "cal", "calendar"}:
#                         self.print_time()
#                     elif menu_choice in {"2", "skill", "skills"}:
#                         self.print_skills()
#                     elif menu_choice in {"3", "rap","rapport"}:
#                         self.print_rapport()
#                     elif menu_choice in {"4", "enroll", "enrollment"}:
#                         self.print_enrollment()
#                     elif menu_choice in {"5", "f", "focus"}:
#                         self.print_focuses()
#                     elif menu_choice in {"6", "s","save"}:
#                         self.save()
#             elif user_input.lower() in {"focus", "f"}:
#                 confirm_focus = False
#                 while not confirm_focus:
#                     focus1 = input("FOCUS 1 >> ")
#                     while focus1 not in static.focus_codes:
#                         print("\nInvalid focus code. Please try again.\n")
#                         focus1 = input("FOCUS 1 >> ")
#                     focus2 = input("FOCUS 2 >> ")
#                     while focus2 not in static.focus_codes:
#                         print("\nInvalid focus code. Please try again.\n")
#                         focus2 = input("FOCUS 2 >> ")
#                     focus3 = input("FOCUS 3 >> ")
#                     while focus3 not in static.focus_codes:
#                         print("\nInvalid focus code. Please try again.\n")
#                         focus3 = input("FOCUS 3 >> ")
#                     print (f"Focuses: {static.focus_codes[focus1]}, {static.focus_codes[focus2]}, {static.focus_codes[focus3]}")
#                     yn = input("Are you sure you want to set these focuses? (y/n): ")
#                     if yn.lower() in {"y", "yes"}:
#                         confirm_focus = True
#                 weekly_focus = {focus1, focus2, focus3}
#                 self.advance(weekly_focus)

#     def advance(self, weekly_focus):
#         for focus in weekly_focus:
#             ftype = focus.split("-")[0]
#             findex = static.focus_codes[focus]
#             if ftype == "ed":
#                 course = dict()
#                 if findex == "fine_arts":
#                     course = static.courses[self.ply.art_elective]
#                 elif findex == "life_skills":
#                     course = static.courses[self.ply.life_elective]
#                 else:
#                     course = static.courses[findex]
#                 print(f"Education focus selected: {course['name']}")
#                 self.advance_course(course)
#             elif ftype == "ex":
#                 exc = static.extracurriculars[findex]
#                 print(f"Extracurricular focus selected: {exc['name']}")
#                 self.advance_extracurricular(exc)
#             elif ftype == "so":
#                 soc = static.social[findex]
#                 print(f"Social focus selected: {soc['name']}")
#                 self.advance_social(soc)
#             elif ftype == "pr":
#                 per = static.personal[findex]
#                 print(f"Personal focus selected: {per['name']}")
#                 self.advance_personal(per)
#         for person in self.ply.rapport:
#             if person in self.glob.students:
#                 old_rap = self.glob.students[person].rapport
#                 new_rap = self.ply.rapport[person]
#                 if new_rap > 200:
#                     new_rap = 200
#                 if old_rap < new_rap:
#                     self.glob.students[person].rapport = new_rap
#                     self.glob.students[person].rapport_rank = math.floor(new_rap / 10)
#         self.glob.advance_time()

#     def advance_course(self, course):
#         for character in self.glob.course_enroll[course["index"]]:
#             self.ply.rapport[character] += 1
#         for skill in course["skills"]:
#             self.ply.skills[skill] += 1
#         if course["index"] in ("sciences", "humanities", "com_skills"):
#             if self.ply.curriculum == course["index"]:
#                 self.ply.class_scores[course["index"]] += 3
#                 self.ply.class_scores_quarter[course["index"]] += 3
#             else:
#                 self.ply.class_scores[course["index"]] += 2
#                 self.ply.class_scores_quarter[course["index"]] += 2
#         elif course["index"] in ("visual_art", "music", "perform", "poetry"):
#             self.ply.class_scores["fine_arts"] += 4
#             self.ply.class_scores_quarter["fine_arts"] += 4
#         elif course["index"] in ("health", "cooking", "mechanics", "oral_com"):
#             self.ply.class_scores["life_skills"] += 4
#             self.ply.class_scores_quarter["life_skills"] += 4
#         for course in self.ply.class_scores:
#             sc_index = self.glob.time["sc_index"]
#             if static.calendar["school"][sc_index]["quarter"] in {"midterms", "finals", "exams"}:
#                 self.ply.class_grades[course] = min(self.ply.class_scores_quarter[course], 5)
#             elif static.calendar["school"][sc_index-1]["quarter"] in {"midterms", "finals", "exams"}:
#                 self.ply.class_scores_quarter[course] = 0

#     def advance_extracurricular(self, extracurricular):
#         for character in self.glob.ec_enroll[extracurricular["index"]]:
#             self.ply.rapport[character] += 1
#         skill_count = 0
#         for skill in extracurricular["skills"]:
#             if skill_count < 2:
#                 self.ply.skills[skill] += 2
#                 skill_count += 1
#             else:
#                 self.ply.skills[skill] += 1

#     def advance_social(self, social):
#         print("Social not yet implemented! Time wasted! SAD!")
#         # print(f"Advancing social activity: {social['name']}")
#         # for character in self.glob.social_enroll[social["index"]]:
#         #     self.ply.rapport[character] += 1
#         # for skill in social["skills"]:
#         #     self.ply.skills[skill] += 1
#         # self.glob.advance_time()

#     def advance_personal(self, personal):
#         print("Personal not yet implemented! Time wasted! SAD!")
#         # print(f"Advancing personal focus: {personal['name']}")
#         # for skill in personal["skills"]:
#         #     self.ply.skills[skill] += 1
#         # self.glob.advance_time()

#     def print_time(self):
#         print(f"\nMonday, {static.calendar['month_names'][self.glob.time['month']]} {self.glob.time['day']}, {self.glob.time['year']}\nYear {static.calendar['school'][self.glob.time['sc_index']]['school_year']}, {static.calendar['school'][self.glob.time['sc_index']]['semester'].capitalize()} Semester, {static.calendar['school'][self.glob.time['sc_index']]['quarter'].capitalize()} Quarter\nTotal Week: {self.glob.time['total_week']}\n")

#     def print_skills(self):
#         print("\nStats and Skills:\n")
#         print(f"Attributes:\n{'Body: ' + str(self.ply.att['body']):<10} {'Eyes: ' + str(self.ply.att['eyes']):<10} {'Mind: ' + str(self.ply.att['mind']):<10} {'Heart: ' + str(self.ply.att['heart']):<10}\n")
#         print("Skills:\n")
#         skill_string = ""
#         skill_number = 0
#         for skill, value in self.ply.skill.items():
#             if skill_number % 4 == 0 and skill_number != 0:
#                 skill_string += "\n"
#             skill_string += f"{skill}: {math.floor(value/10)}".ljust(20)
#             skill_number += 1
#         print(skill_string)

#     def print_rapport(self):
#         ply = self.ply
#         print("\nRapport:\n")
#         character_string = ""
#         character_number = 0
#         for character, value in ply.rapport.items():
#             if character_number % 4 == 0 and character_number != 0:
#                 character_string += "\n"
#             character_string += f"{character}: {math.floor(value/10)}".ljust(20)
#             character_number += 1
#         print(character_string)

#     def print_enrollment(self):
#         print("\nEnrollment:\n")
#         print(f"Curriculum Track: {self.ply.curriculum}")
#         print(f"Fine Art Elective: {self.ply.art_elective}")
#         print(f"Life Skills Elective: {self.ply.life_elective}")
#         print(f"Class Scores: {self.ply.class_scores}")
#         # print(f"Class Scores This Quarter: {self.ply.class_scores_quarter}")
#         print(f"Class Grades: {self.ply.class_grades}")
#         for event in self.ply.extracurriculars:
#             print(f"Extracurricular: {event}")

#     def print_focuses(self):
#         print("\nFocuses:")
#         print(f"\nEDUCATION:".ljust(30) + "EXTRACURRICULAR:".ljust(30) + "SOCIAL:".ljust(30))
#         print(f"Sciences: ed-s".ljust(30) + "Animal Science Club: ex-asc".ljust(30) + "Lunch: so-l".ljust(30))
#         print(f"Humanities: ed-h".ljust(30) + "Football / Soccer: ex-f".ljust(30) + "Walking Home: so-w".ljust(30))
#         print(f"Commercial Skills: ed-c".ljust(30) + "Staff Arts: ex-s".ljust(30) + "After School: so-a".ljust(30))
#         print(f"Arts: ed-a".ljust(30) + "Debate Club: ex-d".ljust(30) + "Weekend: so-we".ljust(30))
#         print(f"Life Skills: ed-l".ljust(30) + "Marching Band: ex-b".ljust(30) + "Group Activity: so-g".ljust(30))
#         print(f"".ljust(30) + "Mancala Club: ex-m".ljust(30) + "Holiday: so-h".ljust(30))
#         print(f"".ljust(30) + "Theater: ex-t")
#         print(f"".ljust(30) + "Art Club: ex-a")
#         print(f"".ljust(30) + "Volunteer Service Club: ex-v")
#         print(f"".ljust(30) + "Student Newspaper: ex-n\n")


# def main():
#     game_instance = Game()
#     game_instance.main_menu()


# if __name__ == "__main__":
#     main()



# print("\n\nFocuses:")
# print("\nEDUCATION:\n")
# print("Sciences: ed-s")
# print("Humanities: ed-h")
# print("Commercial Skills: ed-c")
# print("Arts: ed-a")
# print("Life Skills: ed-l")
# print("\nEXTRACURRICULAR:\n")
# print("Animal Science Club: ex-asc")
# print("Football / Soccer: ex-f")
# print("Staff Arts: ex-s")
# print("Debate Club: ex-d")
# print("Marching Band: ex-b")
# print("Mancala Club: ex-m")
# print("Theater: ex-t")
# print("Art Club: ex-a")
# print("Volunteer Service Club: ex-v")
# print("Student Newspaper: ex-n")
# print("\nSOCIAL:\n")
# print("Lunch: so-l")
# print("Walking Home: so-w")
# print("After School: so-a")
# print("Weekend: so-we")
# print("Group Activity: so-g")
# print("Holiday: so-h")

