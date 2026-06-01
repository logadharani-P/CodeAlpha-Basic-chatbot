while True:
    user=input().lower()

    if user=="hi":
        print("Hello,how can i help you?")
    elif user=="how are you?":
        print("I am glad to hear that i'm pretty well,how about you?")
    elif user=="i am fine":
        print("That's great to hear!")
    elif user=="what is the scientific name of cockroach?":
        print("The scientific name of cockroach is Blattodea while there are over 4,600 species of cockroach")
    elif user=="who is the chiefminister of tamilnadu?":
        print("the current chief minister of tamilnadu is c.joseph vijay")
    elif user=="Who am i?":
        print("I don't have any personal information about you,pleae tell me about yourself")
    elif user=="bye":
        print("goodbye!have a nice day")
        break
    else:
        print("sorry,i can't understand please try again")
