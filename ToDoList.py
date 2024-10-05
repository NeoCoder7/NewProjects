# To Do List
ToDoList=[]
while True:
    print("Welcome to your To Do List")
    print("""Type 1 to Add something
Type 2 to Cross-Off Something
Type 3 to View your list
Type 4 to Exit """)
    CommandofUser=int(input())
    if CommandofUser==1:
            Adding=input("What do you want to add:\n")
            ToDoList.append(Adding)
    elif CommandofUser==2:
           if not ToDoList:
            print("Your list is empty")
           else:
            WhattoCross=int(input("What would you like to Checkoff\n"))    
            ItemtoCheckOff=ToDoList[WhattoCross-1]
            MaskedItem = ItemtoCheckOff[0] + '-' * (len(ItemtoCheckOff) - 2) + ItemtoCheckOff[-1]
            print(MaskedItem)
    elif CommandofUser==3:
            for item in range(len(ToDoList)):
                  print(f'{item+1}.{ToDoList[item]}')
    elif CommandofUser==4:
            print("GoodBye")
            exit()
    else:
           print("Wrong Input")


