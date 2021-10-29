label d1_evening:

    "Some time passed."

    "It's evening."

    scene bg home
    with dissolve

    "You are at home."

    "You think what to do today."

    "It is internet afterall. You sit down and start chatting with one of SenatRPG members."

    menu: 
        "Who is to going to be?"
        "Ama":
            call d1_chatting_with_ama
        
        "Gibek":
            call d1_chatting_with_gibek

        "Gryfin":
            call d1_chatting_with_gryfin

    "You finish chatting, say goodbyes and start to prepare yourself for sleep."

    if PLAYER_HAS_MET_CHINCZYK:
        jump d1_evening_hags_seed_of_doubt

    "You finish doing your bed."

    "Well, it's time to go to sleep."

    return

# Continuations
label d1_evening_hags_seed_of_doubt:

    "Suddenly..."

    "You remember [chinczyk_name] back when you were walking home."

    "The doubt starts growing in you."

    "Its root growing around your heart and grasping even tighter."

    "That sounded manecing. What will you do with it."

    menu:
        "Take it seriously and do not go to Senat tomorrow":
            call end_did_not_go_to_senat_next_day

        "Warn the Senat members about danger":
            call end_evacuate_senat

        "Ignore it, it's madman's talk":
            $ i = 1 # Do nothing in a nutshell

    return

label d1_chatting_with_ama:

    #$ ama_score += 5

    "You chat with Ama. It's pretty complicated."

    return
    
label d1_chatting_with_gibek:

    $ gibek_score += 5

    "You chat with Gibek. It's pretty epic."

    return

label d1_chatting_with_gryfin:

    $ gryfin_score += 5

    "You chat with Gryfin. It's pretty confusing."

    return