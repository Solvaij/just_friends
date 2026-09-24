focus_codes = {
            "ed-s": "sciences",
            "ed-h": "humanities",
            "ed-c": "com_skills",
            "ed-a": "fine_arts",
            "ed-l": "life_skills",
            "ex-asc": "animal_science",
            "ex-f": "soccer",
            "ex-s": "staff",
            "ex-d": "debate",
            "ex-b": "band",
            "ex-m": "mancala",
            "ex-t": "theater",
            "ex-a": "art_club",
            "ex-v": "service",
            "ex-n": "newspaper",
            "so-sc": "school",
            "so-oo": "one_only",
            "so-ga": "group",
            "pr-r": "resting",
            "pr-b": "reading",
            "pr-p": "practice",
            "pr-e": "eating",
            "pr-t": "traveling"
}

courses = {
    "sciences": {"name": "Sciences", "skills": ["logic"], "alts": {"s", "sc", "sci", "science", "sciences"}, "index": "sciences"},
    "humanities": {"name": "Humanities", "skills": ["recall"], "alts": {"h", "hum", "hummanitiy", "humanities"}, "index": "humanities"},
    "com_skills": {"name": "Commercial Skills", "skills": ["perception"], "alts": {"c", "com", "com_skills", "com skills", "commerical", "commercial_skills", "commercial skills"}, "index": "com_skills"},
    "visual_art": {"name": "Visual Arts", "skills": ["arts", "willpower"], "alts": {"va", "art", "visual_art", "visual art", "visual arts"}, "index": "visual_art"},
    "music": {"name": "Music", "skills": ["motor_skill", "reaction"], "alts": {"mu", "music"}, "index": "music"},
    "perform": {"name": "Performing Arts", "skills": ["presence", "acrobatics"], "alts": {"pa", "perform", "theater", "perform", "performance", "performing_arts", "performing arts"}, "index": "perform"},
    "poetry": {"name": "Poetry", "skills": ["communication", "empathy"], "alts": {"po", "poetry"}, "index": "poetry"},
    "health": {"name": "Health and Fitness", "skills": ["body_mech", "vigor"], "alts": {"hf", "health", "fitness", "health_and_fitness", "health and fitness"}, "index": "health"},
    "cooking": {"name": "Food and Nutrition", "skills": ["cooking", "comfort"], "alts": {"ck", "cooking", "fn", "food", "nutrition", "food_and_nutrition"}, "index": "cooking"},
    "mechanics": {"name": "Crafting and Mechanics", "skills": ["making", "instinct"], "alts": {"mc", "mech", "craft", "autos", "mechanics", "crafting_mechanics", "crafting mechanics", "craft_mech", "crafting_and_mechanics"}, "index": "mechanics"},
    "oral_com": {"name": "Oral Communication", "skills": ["persuasion", "composure"], "alts": {"oc", "oral_com", "oral com", "com", "communication", "oral_communication", "oral communication"}, "index": "oral_com"},
    "fine_arts": {"name": "Fine Arts"},
    "life_skills": {"name": "Life Skills"}
}

extracurriculars = {
    "soccer": {"name": "Football / Soccer", "skills": ["strength", "vigor", "acrobatics", "presence"], "index": "soccer"},
    "staff": {"name": "Staff Fencing", "skills": ["acrobatics", "reaction", "instinct", "body_mech"], "index": "staff"},
    "debate": {"name": "Debate Team", "skills": ["persuasion", "composure", "communication", "logic"], "index": "debate"},
    "band": {"name": "Marching Band", "skills": ["motor_skill", "body_mech", "arts", "vigor"], "index": "band"},
    "mancala": {"name": "Mancala Club", "skills": ["logic", "instinct", "recall", "willpower"], "index": "mancala"},
    "theater": {"name": "Theater", "skills": ["willpower", "presence", "composure", "making"], "index": "theater"},
    "art_club": {"name": "Art Club", "skills": ["arts", "making", "motor_skill", "empathy"], "index": "art_club"},
    "animal_science": {"name": "Animal Science Club", "skills": ["cooking", "recall", "perception", "comfort"], "index": "animal_science"},
    "service": {"name": "Volunteer Service Club", "skills": ["comfort", "empathy", "cooking", "strength"], "index": "service"},
    "newspaper": {"name": "School Newspaper", "skills": ["perception", "communication", "persuasion", "reaction"], "index": "newspaper"}
}

social = {
    "school": {"name": "Social at School", "capacity": 9},
    "solo": {"name": "One-on-One", "capacity": 1},
    "group": {"name": "Group Activity", "capacity": 3}
}

personal = {
    "rest": {"name": "Resting"},
    "read": {"name": "Reading"},
    "practice": {"name": "Practicing Skills"},
    "eat": {"name": "Eating Out"},
    "travel": {"name": "Traveling"}
}

calendar = {
    "month_days": {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31},
    "month_names": {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"},
    "school": [
        {"school_year": 1, "semester": "fall", "quarter": "harvest", "year": 1983, "start_date": "8-8", "end_date": "10-2"},
        {"school_year": 1, "semester": "fall", "quarter": "midterms", "year": 1983, "start_date": "10-3", "end_date": "10-7"},
        {"school_year": 1, "semester": "fall", "quarter": "break", "year": 1983, "start_date": "10-8", "end_date": "10-16"},
        {"school_year": 1, "semester": "fall", "quarter": "autumn", "year": 1983, "start_date": "10-17", "end_date": "12-11"},
        {"school_year": 1, "semester": "fall", "quarter": "finals", "year": 1983, "start_date": "12-12", "end_date": "12-16"},
        {"school_year": 1, "semester": "winter", "quarter": "break", "year": 1983, "start_date": "12-17", "end_date": "1-22"},
        {"school_year": 1, "semester": "spring", "quarter": "thawing", "year": 1984, "start_date": "1-23", "end_date": "3-18"},
        {"school_year": 1, "semester": "spring", "quarter": "midterms", "year": 1984, "start_date": "3-19", "end_date": "3-23"},
        {"school_year": 1, "semester": "spring", "quarter": "break", "year": 1984, "start_date": "3-24", "end_date": "4-1"},
        {"school_year": 1, "semester": "spring", "quarter": "planting", "year": 1984, "start_date": "4-2", "end_date": "5-27"},
        {"school_year": 1, "semester": "spring", "quarter": "finals", "year": 1984, "start_date": "5-28", "end_date": "6-1"},
        {"school_year": 1, "semester": "national", "quarter": "exams", "year": 1984, "start_date": "6-2", "end_date": "6-15"},
        {"school_year": 1, "semester": "summer", "quarter": "break", "year": 1984, "start_date": "6-16", "end_date": "8-5"},
        {"school_year": 2, "semester": "fall", "quarter": "harvest", "year": 1984, "start_date": "8-6", "end_date": "9-30"},
        {"school_year": 2, "semester": "fall", "quarter": "midterms", "year": 1984, "start_date": "10-1", "end_date": "10-5"},
        {"school_year": 2, "semester": "fall", "quarter": "break", "year": 1984, "start_date": "10-6", "end_date": "10-14"},
        {"school_year": 2, "semester": "fall", "quarter": "autumn", "year": 1984, "start_date": "10-15", "end_date": "12-9"},
        {"school_year": 2, "semester": "fall", "quarter": "finals", "year": 1984, "start_date": "12-10", "end_date": "12-14"},
        {"school_year": 2, "semester": "winter", "quarter": "break", "year": 1984, "start_date": "12-15", "end_date": "1-20"},
        {"school_year": 2, "semester": "spring", "quarter": "thawing", "year": 1985, "start_date": "1-21", "end_date": "3-17"},
        {"school_year": 2, "semester": "spring", "quarter": "midterms", "year": 1985, "start_date": "3-18", "end_date": "3-22"},
        {"school_year": 2, "semester": "spring", "quarter": "break", "year": 1985, "start_date": "3-23", "end_date": "3-31"},
        {"school_year": 2, "semester": "spring", "quarter": "planting", "year": 1985, "start_date": "4-1", "end_date": "5-26"},
        {"school_year": 2, "semester": "spring", "quarter": "finals", "year": 1985, "start_date": "5-27", "end_date": "5-31"},
        {"school_year": 2, "semester": "national", "quarter": "exams", "year": 1985, "start_date": "6-1", "end_date": "6-14"},
        {"school_year": 2, "semester": "summer", "quarter": "break", "year": 1985, "start_date": "6-15", "end_date": "8-4"}
    ],
    "holidays": [
        (1,1,"New Year"), 
        (2,10,"Lunar New Year"), 
        (2,21,"Founding Day"),
        (3,12,"Hero Day"),
        (4,4,"Easter"),
        (5,9,"Nature Day"),
        (6,15,"Dragon Boat Festival"),
        (7,28,"Fire Festival"),
        (8,19,"Labor Day"),
        (9,1,"Mancala Day"),
        (9,17,"Children's Day"),
        (10,6,"Harvest Festival"),
        (10,29,"Saint Day"),
        (11,20,"Rememberance Day"),
        (12,3,"Big Battle Day"),
        (12,25,"Christmas"),
        (12,26,"Boxing Day")
    ],
    "lunar": [
        (1983,1,5,"Third"),
        (1983,1,14,"New"),
        (1983,1,22,"First"),
        (1983,1,28,"Full"),
        (1983,2,4,"Third"),
        (1983,2,12,"New"),
        (1983,2,20,"First"),
        (1983,2,27,"Full"),
        (1983,3,6,"Third"),
        (1983,3,14,"New"),
        (1983,3,22,"First"),
        (1983,3,28,"Full"),
        (1983,4,5,"Third"),
        (1983,4,13,"New"),
        (1983,4,20,"First"),
        (1983,4,27,"Full"),
        (1983,5,4,"Third"),
        (1983,5,12,"New"),
        (1983,5,19,"First"),
        (1983,5,26,"Full"),
        (1983,6,3,"Third"),
        (1983,6,11,"New"),
        (1983,6,17,"First"),
        (1983,6,25,"Full"),
        (1983,7,3,"Third"),
        (1983,7,10,"New"),
        (1983,7,16,"First"),
        (1983,7,24,"Full"),
        (1983,8,1,"Third"),
        (1983,8,8,"New"),
        (1983,8,15,"First"),
        (1983,8,23,"Full"),
        (1983,8,31,"Third"),
        (1983,9,6,"New"),
        (1983,9,13,"First"),
        (1983,9,22,"Full"),
        (1983,9,29,"Third"),
        (1983,10,6,"New"),
        (1983,10,13,"First"),
        (1983,10,21,"Full"),
        (1983,10,28,"Third"),
        (1983,11,4,"New"),
        (1983,11,12,"First"),
        (1983,11,20,"Full"),
        (1983,11,27,"Third"),
        (1983,12,4,"New"),
        (1983,12,12,"First"),
        (1983,12,19,"Full"),
        (1983,12,26,"Third"),
        (1984,1,3,"New"),
        (1984,1,11,"First"),
        (1984,1,18,"Full"),
        (1984,1,24,"Third"),
        (1984,2,1,"New"),
        (1984,2,9,"First"),
        (1984,2,16,"Full"),
        (1984,2,23,"Third"),
        (1984,3,2,"New"),
        (1984,3,10,"First"),
        (1984,3,17,"Full"),
        (1984,3,24,"Third"),
        (1984,4,1,"New"),
        (1984,4,8,"First"),
        (1984,4,15,"Full"),
        (1984,4,22,"Third"),
        (1984,4,30,"New"),
        (1984,5,8,"First"),
        (1984,5,15,"Full"),
        (1984,5,22,"Third"),
        (1984,5,30,"New"),
        (1984,6,6,"First"),
        (1984,6,13,"Full"),
        (1984,6,21,"Third"),
        (1984,6,28,"New"),
        (1984,7,5,"First"),
        (1984,7,12,"Full"),
        (1984,7,21,"Third"),
        (1984,7,28,"New"),
        (1984,8,3,"First"),
        (1984,8,11,"Full"),
        (1984,8,19,"Third"),
        (1984,8,26,"New"),
        (1984,9,2,"First"),
        (1984,9,10,"Full"),
        (1984,9,18,"Third"),
        (1984,9,24,"New"),
        (1984,10,1,"First"),
        (1984,10,9,"Full"),
        (1984,10,17,"Third"),
        (1984,10,24,"New"),
        (1984,10,31,"First"),
        (1984,11,8,"Full"),
        (1984,11,16,"Third"),
        (1984,11,22,"New"),
        (1984,11,30,"First"),
        (1984,12,8,"Full"),
        (1984,12,15,"Third"),
        (1984,12,22,"New"),
        (1984,12,30,"First"),
        (1985,1,6,"Full"),
        (1985,1,13,"Third"),
        (1985,1,20,"New"),
        (1985,1,28,"First"),
        (1985,2,5,"Full"),
        (1985,2,12,"Third"),
        (1985,2,19,"New"),
        (1985,2,27,"First"),
        (1985,3,6,"Full"),
        (1985,3,13,"Third"),
        (1985,3,21,"New"),
        (1985,3,29,"First"),
        (1985,4,5,"Full"),
        (1985,4,11,"Third"),
        (1985,4,20,"New"),
        (1985,4,27,"First"),
        (1985,5,4,"Full"),
        (1985,5,11,"Third"),
        (1985,5,19,"New"),
        (1985,5,27,"First"),
        (1985,6,2,"Full"),
        (1985,6,10,"Third"),
        (1985,6,18,"New"),
        (1985,6,25,"First"),
        (1985,7,2,"Full"),
        (1985,7,9,"Third"),
        (1985,7,17,"New"),
        (1985,7,24,"First"),
        (1985,7,31,"Full"),
        (1985,8,8,"Third"),
        (1985,8,16,"New"),
        (1985,8,23,"First"),
        (1985,8,30,"Full"),
        (1985,9,7,"Third"),
        (1985,9,14,"New"),
        (1985,9,21,"First"),
        (1985,9,28,"Full"),
        (1985,10,7,"Third"),
        (1985,10,14,"New"),
        (1985,10,20,"First"),
        (1985,10,28,"Full"),
        (1985,11,5,"Third"),
        (1985,11,12,"New"),
        (1985,11,19,"First"),
        (1985,11,27,"Full"),
        (1985,12,5,"Third"),
        (1985,12,11,"New"),
        (1985,12,18,"First"),
        (1985,12,27,"Full")
    ]
}

encode = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
          10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',
          20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',
          30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z',36:'a',37:'b',38:'c',39:'d',
          40:'e',41:'f',42:'g',43:'h',44:'i',45:'j',46:'k',47:'l',48:'m',49:'n',
          50:'o',60:'p',70:'q',80:'r',90:'s',100:'t',110:'u',120:'v',130:'w',140:'x',
          150:'y',160:'z',170:'!',180:"@",190:"#",200:"$",210:"%",220:"^",230:"&",240:"*",
          250:"(",260:")",270:"-",280:"_",290:"=",300:"+"}

decode = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
          'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,
          'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,
          'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,'a':36,'b':37,'c':38,'d':39,
          'e':40,'f':41,'g':42,'h':43,'i':44,'j':45,'k':46,'l':47,'m':48,'n':49,
          'o':50,'p':60,'q':70,'r':80,'s':90,'t':100,'u':110,'v':120,'w':130,'x':140,
          'y':150,'z':160,'!':170,"@":180,"#":190,"$":200,"%":210,"^":220,"&":230,"*":240,
          "(":250,")":260,"-":270,"_":280,"=":290,"+":300}

# encode = ['0','1','2','3','4','5','6','7','8','9',
#           'A','B','C','D','E','F','G','H','I','J',
#           'K','L','M','N','O','P','Q','R','S','T',
#           'U','V','W','X','Y','Z','a','b','c','d',
#           'e','f','g','h','i','j','k','l','m','n',
#           'o','p','q','r','s','t','u','v','w','x',
#           'y','z','!',"@","#","$","%","^","&","*",
#           "(",")","-","_","=","+","[","]","{","}",
#           "|",";",":","'",'"',",","<",">","/","?",
#           "~","`","\\","\"","'"]

# decode = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
#           'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,
#           'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,
#           'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,'a':36,'b':37,'c':38,'d':39,
#           'e':40,'f':41,'g':42,'h':43,'i':44,'j':45,'k':46,'l':47,'m':48,'n':49,
#           'o':50,'p':51,'q':52,'r':53,'s':54,'t':55,'u':56,'v':57,'w':58,'x':59,
#           'y':60,'z':61,'!':62,"@":63,"#":64,"$":65,"%":66,"^":67,"&":68,"*":69,
#           "(":70,")":71,"-":72,"_":73,"=":74,"+":75,"[":76,"]":77,"{":78,"}":79,
#           "|":80,";":81,":":82,"'":83,'"':84,",":85,"<":86,">":87,"/":88,"?":89,
#           "~":90,"`":91,"\\":92,"\"":93,"'":94}

cdict = {'0': "sciences", '1': "humanities", '2': "com_skills", 
         '3': "visual_art", '4': "music", '5': "perform", '6': "poetry",
         '7': "health", '8': "cooking", '9': "mechanics", 'A': "oral_com",
         "sciences": '0', "humanities": '1', "com_skills": '2', 
         "visual_art": '3', "music": '4', "perform": '5', "poetry": '6', 
         "health": '7', "cooking": '8', "mechanics": '9', "oral_com": 'A'}

edict = {'0':"soccer", '1': "staff", '2': "debate", '3': "band", 
         '4': "mancala", '5': "theater", '6': "art_club", '7': "animal_science", 
         '8': "service", '9': "newspaper", "soccer": '0', "staff": '1', 
         "debate": '2', "band": '3', "mancala": '4', "theater": '5', 
         "art_club": '6', "animal_science": '7', "service": '8', "newspaper": '9'}

# time = {"total_week": 1, "year": 1983, "month": 8, "day": 1, "sc_index": 0}

# def advance():
#     time["total_week"] += 1
#     time["day"] += 7
#     days_this_month = calendar["month_days"][time["month"]]
#     if time["month"] == 2 and (time["year"] % 4 == 0 and (time["year"] % 100 != 0 or time["year"] % 400 == 0)):
#         days_this_month = 29
#     if time["day"] > days_this_month:
#         time["day"] -= days_this_month
#         time["month"] += 1
#         if time["month"] > 12:
#             time["month"] = 1
#             time["year"] += 1
#     sc_year = (calendar["school"][time["sc_index"]]["year"])
#     sc_end = calendar["school"][time["sc_index"]]["end_date"]
#     end_month, end_day = sc_end.split("-")
#     if int(end_month) == 1 and time["month"] == 12:
#         pass
#     elif (time["month"] > int(end_month)) or (time["month"] == int(end_month) and time["day"] > int(end_day)):
#         time["sc_index"] += 1
#     print_time()

# def print_time():
#     print(f"Monday, {calendar['month_names'][time['month']]} {time['day']}, {time['year']}\nYear {calendar['school'][time['sc_index']]['school_year']}, {calendar['school'][time['sc_index']]['semester'].capitalize()} Semester, {calendar['school'][time['sc_index']]['quarter'].capitalize()} Quarter\nTotal Week: {time['total_week']}")





# classmates = {
#     "sciences": {"engineer", "nerd", "rich"},
#     "humanities": {"stuco", "art", "theater"},
#     "com_skills": {"jock", "dropout"},
#     "arts": {"art": {"art"},
#             "music": {"nerd"},
#             "perform": {"theater"},
#             "poetry": {"stuco"}
#             },
#     "life_skills": {"health": {"jock"},
#                     "cooking": {"rich"},
#                     "craft": {"dropout"},
#                     "oral_com": {"engineer"}
#                     },
#     "extracurricular": {"animal_science": {"dropout"},
#                         "football": {"jock"},
#                         "staff_arts": {"rich"},
#                         "debate": {"stuco"},
#                         "marching_band": {"nerd"},
#                         "mancala": {"engineer"},
#                         "theater": {"theater"},
#                         "art_club": {"art"},
#                         "volunteer": {"rival"},
#                         "newspaper": {}
#                         }
# }
