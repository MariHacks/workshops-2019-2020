import random

user_input = ""
joke_list = ["I ate a clock yesterday, it was very time-consuming.",
"Did you hear about the crook who stole a calendar? He got twelve months.",
"I own the world’s worst thesaurus. Not only is it awful, it’s awful.",
"I’ve just written a song about tortillas; actually, it’s more of a rap."]

class ChatBot:
    def __init__(self):
        self.user_name = ''

    def set_user_name(self, user_name):
        self.user_name = user_name


jeff = ChatBot()

while not user_input == "goodbye":

  user_input = input("Hello " +jeff.user_name+": ").lower() # user input

  if user_input == "hello":
    print("hello back")

  elif "my name is" in user_input:
    jeff.set_user_name(user_name)
    print("Nice to meet you "+jeff.user_name)

  elif user_input == "how are you?":
    print("I'm doing well.")

  elif user_input == "goodbye":
    print("Bye fellow human!")

  else:
    print(random.choice(joke_list))

