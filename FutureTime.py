#FutureTime.py
#Name:Macy Dubes
#Date:9/8/25
#Assignment:LAB 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour + 19) % 24
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  #Ask user for minutes
  question1 = input("How many hours?   ")
  question2 = input("How many minutes   ")
  moreHours = int(question1)
  moreMins = int(question2)
  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  
  futureHour = (extraHour + currentHour + moreHours) % 24

  print(f"{futureHour:02d} : {futureMins:02d}")
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
