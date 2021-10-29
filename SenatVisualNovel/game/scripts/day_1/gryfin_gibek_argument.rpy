label d1_gryfin_gibek_argument:

    "Some time later..."

    player "{i}And so I go. Just one more step and the I will join SenatRPG. All of the coolest people in the world, all will surround me with love and attention.{/i}"

    player "{i}One final push and...{/i}"

    scene bg senat
    with fade

    player "Huh, it is... pretty empty. It's probably because it half past 11:00."

    gibek "...ust like every time you do."

    player "{i}Did I hear something?{/i}"

    gryfin "... can happen, you just need to adapt. From all people I was ..."

    player "{i}Oh wait, someone's there.{/i}"

    "You follow the sounds of argument and eventually find its source."

    show gibek standard at slight_right
    with easeinleft

    show gryfin standard at slight_left
    with easeinright

    player "Oh my god, its {a=call:d1_gryfin_pocket_info}Gryfin{/a}!"
    
    player "{a=call:d1_gibek_pocket_info}Gibek{/a} is here as well."
    
    player "I always wanted to meet them, see them, touch them... smell them?"

    "..."

    gryfin "It was absolutly important!"

    gryfin "I have finally had this spark! I just had to get to the drawing board and note all I had in mind."

    gibek "And what was {a=call:d1_ama_pocket_info}Ama{/a} doing in all of this?"

    gryfin "She was providing me inspiration. You are playing on in my {a=call:d1_campaign_pocket_info}campaign{/a}."

    gibek "She is your player as well."

    gryfin "Ok listen, it was just one time, next time I'll talk to you. I promise I will not forget about our meeting because of getting into my passion."

    gibek "It's not about you missing our appointment."

    gibek "It's about not being kind of a cunt and letting me know, so that I will not waste my day waiting."

    "After that they both realise you are watching them."

    show gryfin smile
    show gibek cool

    "Almost like nothing happend."

    gibek "Welcome, you are our new recruit, I see you found your way here."

    gryfin "Hi, I'm Gryfin and you are [player_name] if I'm not mistaken."

    player "Well yes, I am ..."

    gryfin "It is perfect. You are perfect. An unbiased person who can give use his honest opinion and end our 25 minute long discussion."

    gibek "You are actually going to..."

    gryfin "See I was planning to meet Gibek yesterday, but {a=call:d1_some_things}some things{/a} got in the way..."

    gryfin "Now, Gibek is pretty sad about it."

    gibek "Angry, actually. You are even ignoring what I just said."

    gryfin "While I say that it happend just one time and he is blowing it out of proportions."

    gryfin "What do you think about it?"

    menu:
        
        player "Well, I think..."

        "That Gibek has all right reasons to be mad":
            call d1_go_for_gibek from _call_d1_go_for_gibek

        "That Gryfin is right and it is not a big deal":
            call d1_go_for_gryfin from _call_d1_go_for_gryfin

        "That you both are friends, and that you will solve it together":
            call d1_let_them_settle_this from _call_d1_let_them_settle_this

    return


# Continuations
label d1_go_for_gibek:

    $ gibek_score += 10;

    gibek "Hah, see. Your unbiased person has spoken. Is it the moment where we could end the discussion?"

    gryfin "Sure, here have your new friend. Who cares. It is not like you ever need me for anything so you might as well go with [player_name], despite the fact that you will forget his name once I'm gone."

    gibek "It's not true."

    hide gryfin smile
    with easeoutleft

    "After these word, Gryfin just rolled his eyes and left. Who knows where he went really. It seems like he will not show up tomorrow."

    "Gibek's eyes and yours interlock and then he says word you longed to hear for some time now."

    gibek "You want to eat lunch? I can show you where we usually do it."
    
    player "We'll, I could stop somewhere nice and eat something."

    call d1_lunch_with_gibek from _call_d1_lunch_with_gibek

    return


label d1_go_for_gryfin:

    $ gryfin_score += 10;

    gibek "Are you actually serious?"

    gibek "Communication is base of every human interaction there can be."

    gryfin "And here we have someone who will not cling to every little detail."

    gibek "For the love of God, I am starting to get headache."

    hide gibek cool
    with easeoutleft

    "Well, Gibek left. It seems like he will not show up tomorrow."

    player "{i}What...?{/i}"

    gryfin "Well, don't worry, he will get over it. He always does. He's the cuttest person you will meet here. Especially when he's mad."

    gryfin "I prefere when he is not mad at me though, but he's still cute."
    
    player "Should I be sorry. I feel like i may anger him."

    gryfin "Nah... don't worry. Now come, I am going shopping, hoping to find some inpiration for my ongoing campaign."

    player "Are you leaving Senat?"

    gryfin "Just temporarly"

    call d1_shopping_with_gryfin from _call_d1_shopping_with_gryfin

    return


label d1_let_them_settle_this:

    $ gibek_score += 5;
    $ gryfin_score += 5;

    gibek "..."

    gryfin "..."

    gibek "I sound pretty reasonable."

    gryfin "I didn't answer the question though."

    player "It's because you are the ones who need to answere this question."

    gryfin "But..."

    gibek "Here, Gryfin, let's eat something. You are way more tolerable when you have your mouth full."
    
    "Gryfin looks at you and it seems he wants to say {a=call:d1_he_want_to_say_something}something{/a}, but keeps his tongue."

    hide gibek
    with easeoutleft

    hide gryfin
    with easeoutleft

    "They then leave. You are left alone."

    "The rest of your day is pretty boring."

    "You learn that everyone on SenatRPG is an actual living human being with their own lifes and some day SenatRPG can be completly empty."

    player "{i}It is a little dissapointment, but that's fair. Maybe tomorrow I will meet some more of them.{/i}"

    call d1_meeting_hag from _call_d1_meeting_hag

    return




# Side notes

label d1_gryfin_pocket_info:

    player "{i}Gryfin pocket info{/i}"

    return
    
label d1_gibek_pocket_info:

    player "{i}Gibek pocket info{/i}"

    return
    
label d1_ama_pocket_info:

    player "{i}Ama pocket info{/i}"

    return
    
label d1_campaign_pocket_info:

    player "{i}Campaign pocket info{/i}"

    return
    
label d1_some_things:

    player "{i}Some thing got in the way...{/a}"

    return

label d1_he_want_to_say_something:

    player "Yes?"

    gryfin "No, it is just that you semi-solved our problem and we are leaving you behind."

    "Don't worry, it's not in script right now."

    "Best case scenarion it will throw an error."

    "Worst kind, crash computer and free {i}him{/i}."