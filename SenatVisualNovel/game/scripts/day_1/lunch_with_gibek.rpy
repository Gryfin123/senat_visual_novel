label d1_lunch_with_gibek:

    "And so you follow Gibek..."

    "His beautiful shining locks of hair..."

    "His muscular trained pizza-dough-rolling-arms..."

    "His perfect, thicc, a..."

    "He turns to you"

    scene bg eating_area

    show gibek cool at center
    with dissolve

    gibek "We are here."

    player "Well, that's not far at all."

    gibek "I didn't say it was far."

    "And so you sit down, have some talky-talky with Gibek."

    "We could probably go into details once we get more writers."

    "And then the air thickens."

    show gibek concern
    with dissolve

    player "{i}Gibek looks somewhat different. The air is also weirdly chill...{/i}"

    player "Hey Gibek, does it always get that chilly here around noon?"

    gibek "..."

    "You turn around and see her."

    show ama standard at slight_right
    with fade

    ama "Hi, you wouldn't mind me to sit with you?"

    gibek "..."

    "Ama sits next to Gibek and starts talking."

    player "{i}Gibek seems unconfortable being in her vicinity.{/i}"

    if PLAYER_HAS_4TH_WALL:
        menu:
            "Should I do anything about it?"
            "I'm new here, let's see how this plays out":
                call d1_let_it_play_out

            "Flip the table and start screaming \"The Racoons are back!!!\"":
                call d1_tableflip

            "Redirect the talk to your person, to distract Ama.":
                call d1_distract_her

            "You have some rubble from before, this can be used somehow." if PLAYER_HAS_4TH_WALL:
                call d1_build_wall

    return

# Continuations
label d1_let_it_play_out:

    "Gibek and Ama keep on talking."

    "But to be honest its less of a dialogue and more like a monolog."

    "At some point Ama drops spork on the ground."

    ama "Woops..."

    "She dives under the table to pick it up."

    "But she's no match for your speed."

    scene bg under_the_table
    hide gibek
    show ama standard at center
    with fade

    "You dive there to and race her for the spork."

    "You drift your hand between badgers to reach for the spork."

    "Your eyes meet under the table just for split second"

    "You see something in them..."

    "It's difficult to describe..."

    show ama evil
    with dissolve

    "Then you both go back up."

    scene bg eating_area
    show ama standard
    with fade

    "When you are back up, Gibek is gone."

    "No long after that, both of you depart seperate ways too."

    return

label d1_tableflip:

    "You flip tha table and start screaming:"

    player "RACOONS!!!"

    player "They are bakc!"

    player "{i}Wait, what is that screeching...{/i}"

    player "There acutally were racoons under this table"

    gibek "Actually, these are badgers."

    "Gibek picks one up and starts comforting it."

    ama "Wait... what? Why?"

    gibek "There was no better place for their winter sleep."

    "Gibek starts picking up all the badgers and taking them somewhere safe."

    hide gibek
    with easeoutright

    $ gibek_score -= 5

    "You remember that {a=call:d1_random_fact_of_the_day}some animals woken from winter sleep die."

    "You feel like a duche."

    "Ama starts desinfecting her hands."

    "That was a buzzkill."

    "No long after you leave home, showered in shame."

    return

label d1_distract_her:

    "You take a tichue..."

    "Tihuu..."

    "Tischiu...?"

    "..."

    "You take a piece of paper."

    "You scribble random lines on it."

    player "Jeez, I wonder how may I solve this complicated math equation."

    ama "What equation?"

    "You have no idea how she teleported behind you."

    player "Well, I had some difficulites with it yesterday. From what I heard Einstain could not solve it himself so it is no wonder I failed too."

    "Oh boy, it's on... You should see the look on her face."

    ama "That's bullshit, give me that."

    "She gets into it and starts solving you scribbles."

    # If you'd ever want to use this variable somewhere, move it to default_defines-file.
    $ not_important_yet_value = renpy.input("She is actually doing it. What did you write there?")

    "Huh."

    $ gibek_score += 10

    show gibek cool
    with dissolve

    "Anyway, a spark of understanding flashes in Gibeks eyes."

    gibek "You sacrifice will not be forgotten friend."

    "He whispers to you, nods and leaves undisturbed."

    hide gibek
    with easeoutbottom

    "You left with Ama."

    "She solves the thing and gives it back to you."

    "Well that is just impressive."

    "You have some small talk with her and then leave"

    return

label d1_build_wall:

    "You pull out rubble you have collected earlier."

    "You nod to gibek."

    "He nods to you."

    "You throw rubble at Ama."

    "There is few seconds of absolute silence. Like the sound itself has been vaccumed out of this room."

    "Gibek nods ut you like \"That's not what I had in mind.\""

    "You nod at him with \"Well what was it then?\""

    show ama evil
    with fade

    "\"We need to do something, that's not save\" nods Gibek."
    
    "But you got it."

    "You build a 4th wall around Ama before she can do anything."

    "New fastest fingers in SenatRPG."

    "You and Gibek then evacuate as fast as you can."

    $ PLAYER_BUILD_WALL_AROUND_AMA = True
    $ PLAYER_HAS_4TH_WALL = False

    hide gibek
    with easeoutright

    scene bg outside
    with fade


    "After that Gibek escorts you home, to make sure you are safe."

    show gibek cool
    with easeinbottom

    gibek "That was some majestic brick improvisation."

    gibek "It is difficult to say more then..."

    gibek "I'm impressed."

    player "Thank you."

    "You go home leaving a adrenaline-indulged-smile on Gibek's face"

    $ gibek_score += 50

    return


#Side notes

label d1_random_fact_of_the_day:

    "And that's the random fact of the day kids."

    "Do not disturb animals' winter sleep or thay die and in process probably hurt you too."

    return