
# CAR GAME
command=""
started=False

while command !="quit":
    command=input(">").lower()
    if command =="start":
        if started:
            print("Car is already Started")
        else:
            started=True
            print("Car started.")

    elif command =="stop":
        if not started:
            print("Car is already stoped")
        else:
            started=False
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

