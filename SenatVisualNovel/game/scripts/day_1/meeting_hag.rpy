label d1_meeting_hag:

    scene bg outside
    with fade

    "Some time later..."

    "While you are coming back home, minding your own buisness while someone approches you."

    show hag standard at far_left
    with easeinleft

    chinu "Chi..."

    show hag standard at slight_left
    with ease

    chinu "Chi chi..."

    show hag standard at center
    with ease

    chinu "Chi chi chi..."

    chinu "{a=call:d1_chinczyk_pocket_info}Chinczyk{/a} has find you my deahahahahr."

    chinu "What are you doing here, alone, leaving SenatRPG?"

    player "I'm heading back home actually."

    chinu "Well don't go yet. I have new interesting game system we could check out together."

    menu:
        "Let [chinczyk_name] introduce you to he's new game system":
            call d1_chinczyk_game_system
        "Run before he grabs you":
            call d1_run_from_chinczyk

    "When you start leaving you hear [chinczyk_name] shout behind you."

    chinu "Do not come to SenatRPG tomorrow little [player_name], mark my words!"



    show hag standard at slight_right
    with ease

    chinu "Chi chi chi..."

    show hag standard at far_right
    with ease

    chinu "Chi chi..."

    hide hag standard
    with easeoutright

    chinu "Chi..."

    return


# Continuations

label d1_chinczyk_game_system:

    "You stop with [chinczyk_name] for a moment"

    show hag laugh

    "He pulls out some random stickers, dice, tiles..."

    "... some paper, pencils, gum..."

    "... actual ceramic tiles, branches, leafes..."

    "... dynamit, gas mask, brick..."

    "... something labeled {a=call:d1_the_end_protector}\"The End Protector\"{/a}, metal pipe, restraining order..."

    "... pills... and then he starts putting everything together in seemingly, reasonalbe manner."

    "Then he proceeds to explain to you how the game works and plays one game with you."

    "It's an actual miracle that passersby did not call the police."

    "At the end of it all, you did not get a thing about his system."

    "During the game, sometimes he was sad, sometimes he was laughing, sometimes he was mad..."

    "At the end [chinczyk_name] won."

    "You could not care less at this point."

    "You take your opening and leave before he pulls out another game."

    return

label d1_run_from_chinczyk:

    "You start running away."

    "[chinczyk_name] grabs your hand."

    chinu "Ah... just one game, come one. It's fun."

    "You don't take any of that."

    "You grab random passerby and tell [chinczyk_name] he is a fan of Warhemmer 2nd edition."

    chinu "..."
    
    chinu "He..."
    
    chinu "What..."

    "Oh boy, the air around actually got pretty danse. The grip on your arm loosend though."

    "You take your chance and do not turn around to witness what horrific fate may meet that random person."

    return

# Side notes
label d1_chinczyk_pocket_info:

    player "{i}This name sound... almost familiar.{/i}"

    player "{i}He's one of the final person that left the server!{/i}"

    $ chinczyk_name = "Chinczyk"
    
    player "{i}The Erased one!{/i}"

    player "{i}The Ever Hungry Beast!{/i}"

    player "{i}The Commy!{/i}"

    player "{i}I... what should I...{/i}"

label d1_the_end_protector:

    "It looks strange, almost like it would be relevant for the plot later."

    "You snatch it, so that [chinczyk_name] does not see a thing."

    "He is too involved in pulling stuff out of his bag."

    "Dear God... he is not even half way through."





