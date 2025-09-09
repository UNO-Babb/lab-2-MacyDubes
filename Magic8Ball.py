#Magic8Ball.py
#Name:Macy Dubes
#Date:9/8/25
#Assignment:LAB2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ["For sure.", "Yes.", "Without a doubt.", "It is certain", "Signs point to yes.", "Definitely.", "Most likely.", "You can rely on it", 
           "You betcha!", "Ask again later.", "Better not tell you now.", "Don't count on it.", "Cannot predict now.", "Very doubtful.", 
           "My sources say no.", "My reply is no", "No.", "Nope.", "Probably not", "Absolutely not."]
  #Prompt the user for their question.
  question = input("What do you want to know?  ")

  length = len(answers)
  r = random.random() * length
  #Answer question randomly with one of the options from your earlier list.
  r = int(r)
  
  response = answers[r]
  print(response)
if __name__ == '__main__':
  main()
