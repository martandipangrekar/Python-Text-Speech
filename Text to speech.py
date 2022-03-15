import  pyttsx3
friend=pyttsx3.init()
Say=input("Say Somthing: ")
friend.say(Say)
friend.runAndWait()

