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
  
    call d1_intro

    # This ends the game.
    ama "That's it, the game ends here. Hope you had fun."
    
    return

    