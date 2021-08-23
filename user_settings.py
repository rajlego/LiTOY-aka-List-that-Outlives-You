# lifebar arguments :
disable_lifebar     = "no"
useless_first_years = 15
user_age            = 24
user_life_expected  = 90
useless_last_years  = 20

# save very often a copy of the whole database as a json file:
json_auto_save = True

# number of session of review, each session is composed of n_to_review reviews
# so total number of reviews is n_session*n_to_review
n_session = 5

# number of entries to pick for review at each launch (default=5):
n_to_review = 3

# for reading time estimation:
wpm = 200
average_word_length = 6

# absolute path for autocompletion of local files:
default_dir = "/home/"

# used when reviewing:
questions = {
        "importance": "What steps will make you likely to achieve your goals?",
#        "importance": "What steps will make you likely to achieve your goals?\
#\n* Which is more important?\n* If you had one hour to spend,\
#which would bring you more in your life?",
        "time": "Which task takes the less time to complete?",
        }

shortcuts = {"skip_review"      : ["s", "-"],
             "answer_level"     : ["1", "2", "3", "4", "5",
                                   "a", "z", "e", "r", "t"],
             "edit_left"        : ["el"],
             "edit_right"       : ["er"],
             "reload_media"     : ["reload"],
             "undo"             : ["undo"],
             "show_few_fields"  : ["less"],
             "show_all_fields"  : ["more"],
             "star_left"        : ["xl"],
             "star_right"       : ["xr"],
             "disable_left"     : ["dl"],
             "disable_right"    : ["dr"],
             "open_media"       : ["o"],
             "repick"           : ["repick"],
             "show_help"        : ["h", "H", "?", "help"],
             "open debugger"    : ["debug"],
             "quit"             : ["quit", "q", "exit"] }

# ELO :
K_values           =  [100, 80, 60, 40, 25, 17, 15, 12, 10]
# if you decide to change the setting, be careful : each new term has to be
# different and lower than the last one
default_score      =  1000  # default 1000
global_weights     =  (2, 1)  # gELO = 1st number*iELO + 2nd*tELO

# to avoid getting flagged for abusive web scraping
headers = {"User-Agent": "Mozilla/5.0"}

# VT100 color code: from https://wiki.bash-hackers.org/scripting/terminalcodes
col_red = "\033[91m"
col_blu = "\033[94m"
col_yel = "\033[93m"
col_gre = "\033[92m"
col_cya = "\033[36m"
col_mgt_fg = "\033[45m"
col_blink = "\033[5m"
col_bold = "\033[1m"
col_uline = "\033[4m"
col_rst = "\033[0m"
spacer = "    "  # nicer print message

