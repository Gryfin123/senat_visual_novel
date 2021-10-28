
# Define variables
define player_name = ""
define chinczyk_name = "???"


# Define characters
define player = Character("[player_name]", who_color="#990022", what_color="#DD6688", window_color="#660011" )
define ama = Character("Ama", who_color="#b8381b")
define gibek = Character("Gibek", who_color="#7b12a8")
define gryfin = Character("Gryfin", who_color="#34d32e")
define chinu = Character("[chinczyk_name]", who_color="#fca737")


# Define flags
define PLAYER_HAS_4TH_WALL = False
define PLAYER_HAS_THE_END_PROTECTOR = False

# Define Character's Score
define base_gibek_score = -5
define gibek_score = base_gibek_score
define base_gryfin_score = 0
define gryfin_score = base_gryfin_score

# Define transforms (used in positioning of characters on screen)
transform far_left:
    xalign 0
    yalign 1
transform slight_left:
    xalign 0.25
    yalign 1
transform center:
    xalign 0.50
    yalign 1
transform slight_right:
    xalign 0.75
    yalign 1
transform far_right:
    xalign 1.0
    yalign 1

# Define functions
init python:
    def restartCharacterScoresAndFlags():
        gibek_score = base_gibek_score
        gryfin_score = base_gryfin_score
        PLAYER_HAS_4TH_WALL = False
        PLAYER_HAS_THE_END_PROTECTOR = False



python:
    """
    player "Just testing imports."
    
    $ player_name = renpy.input("What is your name, Magical Boy?")

    $ player_name = player_name.strip()# The .strip() instruction removes any extra spaces the player may have typed by accident.

    player "That's what I have become."

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Shuji"
  
    ama "Pleased to meet you, %(player_name)s!"

    show ama standard at far_left
    with easeinleft

    ama "Ha."

    show ama evil at slight_left
    with easeinbottom

    ama "Ha ha."

    show gibek standard at far_right
    with zoomin
    
    gibek "Hi."

    show gibek concern at slight_right
    with ease
    
    gibek "Hi hi."
    
    show gibek cool at center
    with ease

    gibek "Hi hi hi."

    show gryfin standard at far_right
    with dissolve

    gryfin "He."
    
    show gryfin ready at far_left
    with fade

    gryfin "He he."

    show gryfin smile at slight_right
    with fade

    gryfin "He he he."

    gryfin "Just testing imports."
    """