label ama_finds_users_name:

    ama "Hello there, before we begin I would like to know your name."

    $ attempt_count = 0
    
    while (player_name == ""):
        $ player_name = renpy.input("So what is it?")
        $ player_name = player_name.strip()# The .strip() instruction removes any extra spaces the player may have typed by accident.
        $ attempt_count += 1
        if attempt_count > 4:
            ama "Sure, I'll just choose something."
            ama "{i}Shuffle, shuffle, shuffle...{/i}"
            ama "Rubic, let's go with that."
            $ player_name = "Rubic"

    $ player_name = player_name.capitalize()

    if attempt_count <= 4:
        if player_name != "Rubic":
            ama "I swear I'm just taking it for safekeeping."
        else:
            ama "Pretty sure I have seen it somewhere..."

        ama "Pleased to meet you, [player_name]!"

    ama "No let's keep going."

    return