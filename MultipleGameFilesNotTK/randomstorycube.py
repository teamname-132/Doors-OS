def random_story_cube():
  woman = ["A scientist", "a queen", "a pirate", "a giant rabbit"]
  man = ["a police officer", "an artist", "Your grandfather", "a killer robot"]
  place = ["on Pluto ", "at the supermarket", "in a spooky, bat-filled cave"]
  shewore = ["scuba diving gear", "fairy wings", "paper bag"]
  hewore = ["a purple suit", "a shark costume", "beach towel"]
  womansays = [
    "let’s go to the beach", "let’s go to the moon", "let’s go to spain"
  ]
  mansays = ["ok", "no let’s go cycling", "yes let’s go"]
  consequence = [
    "there got squashed by a giant frog", "got lost", "met a creepy horse"
  ]
  worldsaid = [
    "run over by a car", "fell into a dich", " lost all of their money"
  ]
  while True:
    print(random.choice(woman), "met", random.choice(man),
          random.choice(place))
    print("she was wearing", random.choice(shewore))
    print("he was wearing", random.choice(hewore))
    print("she said", random.choice(womansays))
    print("he said", random.choice(mansays))
    print("On their travels", random.choice(consequence), "and",
          random.choice(worldsaid))
    print()
    print(
      "--------------------------------------------------------------------")
    print()
    hi = input("press enter to play again or to not type stop ").upper()
    if hi == "STOP":
      exit()
    print()
    print(
      "--------------------------------------------------------------------")
    print()