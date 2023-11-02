from english_words import english_words_lower_alpha_set
from random import choice


def hangman():
  play = "yes"
  while play != "no":
    howManyGuesses = 0
    word = choice(list(english_words_lower_alpha_set))
    letters = []
    board = []
    for x in word:
      letters+= [x]
      board+= [""]
    guesses = []
    while guesses[0:] != letters[0:]:
      guess = input("Guess: ").lower()
      if guess == "":
        print("Not a letter.")
      elif len(guess) > 1:
        print("One letter")
      elif guess in guesses and letters.count(guess) == guesses.count(guess):
        print("Already guessed.")
      elif guess not in letters:
        print("No")
        howManyGuesses+=1
      elif guess in letters and letters.count(guess) > 1:
        print("Yes")
        howManyGuesses+=1
        print("There were",letters.count(guess),"of the letter",guess,"in the word")
        counted = letters.count(guess)
        a = counted
        pos = -1
        while a != 0:
          guesses += [guess]
          index = letters.index(guess, pos+1, len(letters))
          pos = index
          board[index] = guess
          a-=1
        print("Board:",('_'.join(board)))
      else:
        howManyGuesses+=1
        print("Yes")
        guesses += [guess]
        index = letters.index(guess)
        board[index] = guess
        print("Board:",('_'.join(board)))
      if sorted(guesses[0:]) == sorted(letters[0:]):
        print("You got that in",howManyGuesses,"guesses.")
        print("Well done!")
        play = input("Do you want to play again? Press enter to continue and no to stop. ")