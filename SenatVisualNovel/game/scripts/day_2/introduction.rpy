label d2_intro:

    scene bg home
    with fade

    "You {a=call:d2_next_morning_random_fact}wake up the next morning{/a}."

    "It's a beautiful day outside. Birds are singing, flower are blooming. On days like this... kids like you..."

    "Want nothing more then to go to SenatRPG."

    "You go there..."
    
    scene bg senat burning

    "Aaand everything is burning!"

    "There is fire everywhere!"

    "Holy crap, it is actually burning fire. Also some buildings are falling in the background. Ground shakes."

    "It actually shakes harder and harder."

    "You hear screaming behind you."

    show hag laugh at center
    with easeintop

    chinu "CHI CHI CHI CHI CHI!!!"

    "You turn, there is a Big F**king [the_end], now in front of you and [chinczyk_name] right on top of it."

    chinu "I'M {a=call:d1_chinczyk_pocket_info}THE BEST ROLEPLAYER{/a}. ME!"
    
    menu:
        "Wait for your impending doom like a bitch":
            call d2_waiting_like_a_bitch from _call_d2_waiting_like_a_bitch

        "Wait for your impending doom like a boss":
            call d2_waiting_like_a_badass from _call_d2_waiting_like_a_badass

        "Use \"The End Protector\"" if PLAYER_HAS_THE_END_PROTECTOR:
            jump d2_end_protector_used 

        "Use \"The 4th Wall Rubble\"" if PLAYER_HAS_4TH_WALL:
            jump d2_4th_wall_rubble_used


    player "{i}This is it. This is how I die...{/i}"

    if gibek_score > 0 and gryfin_score > 0:
        jump d2_duo_to_the_rescue

    elif gibek_score > 0 and gryfin_score <= 0:
        jump d2_gibek_to_the_rescue

    elif gibek_score <= 0 and gryfin_score > 0:
        jump d2_gryfin_to_the_rescue

    else:
        jump d2_fatal_ending

    return

# Continuations
label d2_waiting_like_a_bitch:

    "You curl-up into a tight ball and hope for the best."

    return

label d2_waiting_like_a_badass:

    "You cross your arms and look [the_end] stright into its face."

    return

label d2_end_protector_used:

    "You pull out you \"The End Protecter\"."

    "This crime seems to pay off. [the_end] seems to walk past you and go on killing pretty much everything else."

    "Nothing left to do, but take your chances and run."

    jump end_player_survives_the_end

    return
    
label d2_4th_wall_rubble_used:

    "You pull out you \"The 4th Wall Rubble\"."

    "You use throw it at [the_end]. It's not very effective."

    "You build a giantic wall to close it off from you."

    "Seems to work fine for now."

    "You run. You can hear it breaking through the wall in the background. You are save though."

    jump end_player_survives_the_end

    return

label d2_fatal_ending:

    scene black

    player "{i}And there, at this exact moment, while being crush under [the_end]'s giantic feet I realised...{/i}"

    player "{i}That if we die, we are actually dead.{/i}"

    jump general_ending_script

    return

label d2_gibek_to_the_rescue:

    gibek "No fear my Friend..."

    show gibek cool at slight_right

    gibek "For I am here."

    player "Gibek, what is going on!? What should I do?!"

    gibek "Run, save yourself, may the legacy of SenatRPG live in you..."

    player "But I'm only one day here. There is no legacy to be had."

    gibek "Are you kidding me?!"

    gibek "I recall the messages you've sent me."

    gibek "I recall the conversations we have had."

    gibek "I will not beterred from keeping it alive in you."

    gibek "I remeber lessons I passed on to you, my son."

    gibek "I am one of the Old Guard. I am Gibek and I am the A..."

    "[the_end] stomp on you, but Gibek stops it with one hand."

    gibek "Now go."

    "They start trading blows."

    "You can't even run away. You are to captured by the epicness of the fight in front of you."

    "The awesomness of this blows you away so hard you actually end up in your home. All safe and sound."

    jump end_player_survives_the_end

    return

label d2_gryfin_to_the_rescue:

    gryfin "Hey, that's dangerous to be!"

    show gryfin ready at slight_left
    with easeinright

    gryfin "It's not palce save for new recruits. Especially not in front of [the_end]."

    player "I had no idea stuff like this happens here."

    gryfin "Well... It does not."

    player "What should I do then?"

    gryfin "Run."

    "Gryfin pushes you aside. [the_end] stomps barely missing you. It is time to go."

    jump end_player_survives_the_end

    return
    
label d2_duo_to_the_rescue:

    gibek "Prepare for trouble..."

    gryfin "And make it double."

    show gibek cool at slight_right
    with easeinright

    gibek "Team Senat blasts off at the speed of light!"

    show gryfin ready at slight_left
    with easeinright

    gryfin "Surrender now or prepare to fight!"

    player "{i}The fuck just happend{/i}"

    gibek "[player_name], we need your help, we cannot defeat it all by ourselves."

    gryfin "We need you to help us."

    player "How I do it?!"

    "Gryfin takes you notebook."

    player "What?"

    gryfin "Take notes."

    gibek "We need to write it down for future generations."

    "The fight comences. They kick serious butt."

    "The fight took around 48 seconds. Pretty long as for them."

    "The get pretty roughed up, but before [the_end] can exploit that, [chinczyk_name] gives a command to retreat. [the_end] starts running away with [chinczyk_name] on his back."

    hide hag
    with easeoutleft

    "Gibek and Gryfin slam the greatest high-five you have ever seen."

    "Then they go give you high-five as well."

    if PLAYER_BUILD_WALL_AROUND_AMA:
        jump end_ama_wins

    "You hand them finished notes with details about every move they made and some little doodles attached."

    gryfin "What was your favorite part?"
    
    # To use this variable, move definition to default_defines
    $ favorite_moment = renpy.input("So what was it?")

    gibek "Yeah, me too."

    jump end_the_good_ending

    return

# Side-notes
label d2_next_morning_random_fact:

    "You know, some people may take it as a bad sign."

    "And that was the random fact of the day for you."

    "If you consider it a bad sign though, you probably should go and try to find some help."

    return



