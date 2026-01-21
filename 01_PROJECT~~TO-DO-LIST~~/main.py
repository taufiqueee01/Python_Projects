def welcome():
    return "Hello there! Welcome to taufi TO-DO-LIST"
Lists=[]
welcome()


while True:
    if not Lists:
        print(f"Chose your command\n1.Add task--> '1'\n2.Remove task--> '2'\n3. Exit--> '3'")
    else:
        print(f"{Lists} \nChose your command\n1.Add task--> '1'\n2.Remove task--> '2'\n3. Exit--> '3'")
    user=str(input("Enter your command: "))

    if "1" in user:

        def add_task():
            add_user=str(input("Enter your Task Name!!: "))
            Lists.append(add_user)
            print(f"         ~~List is updated~~        \n\n")
        add_task()
            

    elif "2" in user:   

        def tick_task():
            mark_user=str(input("Enter your Task Name!!: "))
            if mark_user in Lists:
                Lists.remove(mark_user)
        tick_task()
        
    elif "3" in user:
        print("Good luck to user my program")
        break
    
    else:
        print("Something error!! Try again")



