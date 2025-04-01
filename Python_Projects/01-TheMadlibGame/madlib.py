
'''------------------------------------ Mad Libs Game ---------------------------------------------'''

#Library
import random

def mad_libs():
    print("\n🎉 Welcome To MADLIB: THE GAME! 🎉\n")   
    
    # User interface
    name = input("Enter a name: ").strip()
    adjective = input("Enter an adjective: ").strip()
    noun = input("Enter a noun: ").strip()
    verb = input("Enter a verb ending in -ing: ").strip()
    place = input("Enter a place: ").strip()
    animal = input("Enter an animal: ").strip()
    emotion = input("Enter an emotion: ").strip()
    food = input("Enter a type of food: ").strip()
    past_tense_verb = input("Enter a verb in past tense: ").strip()

    # Random story templates
    stories = [
        f"One day, {name} was walking through {place} when they saw a {adjective} {animal}. "
        f"The {animal} was {verb} near a {noun}. {name} felt {emotion} and decided to join in. "
        f"After some time, they got hungry and ate some {food}. What a {adjective} day!",

        f"In a faraway land, {name} found a {adjective} {noun}. As soon as they touched it, they were transported to {place}. "
        f"Suddenly, a {animal} appeared, {verb} loudly! {name} was so {emotion} that they {past_tense_verb} away as fast as they could. "
        f"Luckily, they found a delicious {food} waiting for them. A magical adventure indeed!",

        f"While exploring {place}, {name} discovered a {adjective} {noun}. It was unlike anything they had ever seen before. "
        f"Just as they were about to touch it, a {animal} came running towards them, {verb} like crazy. "
        f"{name} felt {emotion} but then realized the {animal} just wanted some {food}. "
        f"With a smile, {name} {past_tense_verb} and shared their meal."
    ]

    # Select and print a random story
    print("\n📝 Your Mad Libs Story:")
    print(random.choice(stories))

    # Replay option
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        mad_libs()
    else:
        print("\nThanks for playing! 🎭")


mad_libs()
