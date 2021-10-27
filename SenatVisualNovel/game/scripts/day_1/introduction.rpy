label d1_intro:
    
    scene bg outdoors

    player "{i}What a day.{/i}"

    player "{i}Who would think out of all of other candidates, I will be the one to join SenatRPG.{/i}"

    player "{i}I mean they are like The Elite of THE ELITE communities.{/i}"

    player "{i}Even though some may disagree, I think they rule of 69 members isn't that bad. It can reduce the number trolls and other {a=call:d1_weird_bunch}weird bunch{/a}.{/i}"

    "And from nowhere!"

    "{b}THUMP{/b}"

    player "Aww... What...?"

    "You hit something. There seems to be some invisible wall blocking your way. But only part of it. You can easily walk past it without much hustle."

    menu:

        "Avoid the wall and keep going to SenatRPG":
            call d1_gryfin_gibek_argument

        "Mark the wall, so that others can avoid it":
            call d1_mark_the_wall

        "Bruteforce your way through the wall":
            call d1_destroy_the_wall

    return


# Continuations

label d1_mark_the_wall:
    player "{i}That strange, good thing I left my bike at home or I could hurt myself.{/i}"
    
    player "{i}Better make sure nobody else hurts himself here.{/i}"

    "You take a can of conviniently lying nearby paint an mark the wall with big red cross."

    "Slish and Slosh later, there is big red cross hanging in mid-air. You are pretty sure nobody will crush into it. Probably stop to make foto though."

    player "Let us be on our way."
    
    call d1_gryfin_gibek_argument

    return



label d1_destroy_the_wall:
    "You stare the invisible wall straith into metaphorical face. It start methaporical staring competition."

    "You know what is not metaphorical though? The convinent jack hammer laying nearby. You pick it up and smash the wall to rubble."

    "You see some person sitting in front of a computer. Weird."

    "You put jackhammer back."

    player "Will I get something for that?"

    "Sure, have some 4th wall rubble. Now head to SenatRPG." 
    
    call d1_gryfin_gibek_argument

    return



# Side notes

label d1_weird_bunch:

    player "{i}I heard they had to shoot out some of their own members. Pretty metal.{/i}"

    player "{i}All that was released to press was they were \"No good and it had to be done for the greater good\".{/i}"

    player "At least now there is free spot for me."
    
    return

