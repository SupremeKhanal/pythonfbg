command=""
while command !="quit":
    command=input(">").lower()
    if command =="start":
        print("Car started....")
    elif command =="stop":
        print("car stoped")
    elif command=="help":
    print("""
          start-to start the car
          stop -to stop the car
          quit-to qui
          """)
    elif command=="quit":
    break
    else:
        print("Sorry i don't understand that")
