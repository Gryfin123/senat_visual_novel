# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Block user's rollback
    $ renpy.block_rollback()
    
    $ restartCharacterScoresAndFlags()

    # Get users name
    call ama_finds_users_name

    # Day 1
    call d1_intro

    call d1_evening

    # Day 2
    call d2_intro

    # This ends the game.
    jump ending_script
    
    return

    