def magic():

  import random

  print("What would you like to ask the magic 8 ball?")
  reply = input()
  answers = ("Go to Wendy\'s, you\'ll find your answer written on the window!", "I wish I knew the answer to that too.", "Ask your mom, she\'ll know.", "Read a book you'll find your answer.", "How am I supposed to know that?", "you\'ll find your answer in a bottle two days from now.","You don't want to know the answer to that.", "Let me think about that.")

  print(random.choices(answers))
  print ("Do you have another question for me?")
  answer = 0

  while answer != "no":

    answer = input()
    if answer == "yes":
      print("What else do you want to know?")
      input()
      print(random.choices(answers), "Type yes if you have more questions.Type no if you\'re done discovering answers to life.")
    elif "answer":
      print ("I was feeling a bit sleepy anyways.'")
    return