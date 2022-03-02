import random

# Name Variable
name = "Akhil"

# Question
question = "Will I ever be a good programmer?"

# Answer
answer = ""




# Random Number Generation ---> Imported Random Module.
random_number = random.randint(1, 11)

# if, elif and else statements to assign and define the answer of the number.

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now.."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Okay Sure."
elif random_number == 11:
  answer = "Heck yeah!"
else:
  print("Error")

if len(question) == 0:
  print("question is not aksed, please ask a question")

elif len(name) == 0:
  print("Question: " + question)

else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)







