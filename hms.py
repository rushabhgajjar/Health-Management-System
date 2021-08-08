# Health Management system
# 3 clients - Rohit, Amit and Dinesh
# 3 files to log their food and 3 files to log their exercise
# write a function that when executed takes input as client name

def get_date():
    import datetime
    return str(datetime.datetime.now())

def retrieve_data():
    client_dic = {1: "Rohit", 2: "Amit", 3: "Dinesh"}
    retrieve = int(input("Enter the client number to retrieve data for:\n1 - Rohit\n2 - Amit\n3 - Dinesh\n"))
    if client_dic[retrieve] == "Rohit":
        with open("Rohit food.txt") as f:
            print("Food")
            print(f.read())
            print("Exercise")
        with open("Rohit exercise.txt") as f:
            print(f.read())
    elif client_dic[retrieve] == "Amit":
        with open("Amit food.txt") as f:
            print("Food")
            print(f.read())
            print("Exercise")
        with open("Amit exercise.txt") as f:
            print(f.read())
    else:
        with open("Dinesh food.txt") as f:
            print("Food")
            print(f.read())
            print("Exercise")
        with open("Dinesh exercise.txt") as f:
            print(f.read())

def client_name():
    client_dic = {1: "Rohit", 2: "Amit", 3: "Dinesh"}
    name_input = int(input("Enter the following number as per the particular client:\n1 - Rohit\n2 - Amit\n3 - Dinesh\n"))
    print("Thank you for selecting", client_dic[name_input])
    print()
    return client_dic, name_input

def select_log(client_dic, name_input):
    activity = {1: "Food", 2: "Exercise"}
    act_input = int(input("Enter the number as per the activity you wish to log for selected client:\n1 - Food\n2 - Exercise\n"))
    print("Thank you for selecting", activity[act_input], "for", client_dic[name_input])
    print()
    return activity, act_input

def data_entry(client_dic,name_input,activity,act_input):
    if client_dic[name_input] == "Rohit":
        if activity[act_input] == "Food":
            with open("Rohit food.txt", "a") as f:
                a = input("Enter food data:")
                print()
                b = get_date()
                f.write(str(b + "   " + a + "\n"))
                print("Entry Successful")
        else:
            with open("Rohit exercise.txt", "a") as f:
                a = input("Enter exercise data:")
                print()
                b = get_date()
                f.write(str(b + "   " + a + "\n"))
                print("Entry Successful")
    elif client_dic[name_input] == "Amit":
        if activity[act_input] == "Food":
            with open("Amit food.txt", "a") as f:
                a = input("Enter food data:")
                print()
                b = get_date()
                f.write(str(b + "   " + a + "\n"))
                print("Entry Successful")
        else:
            with open("Amit exercise.txt", "a") as f:
                a = input("Enter exercise data:")
                print()
                b = get_date()
                f.write(str(b + "   " + a + "\n"))
                print("Entry Successful")
    else:
        if client_dic[name_input] == "Dinesh":
            if activity[act_input] == "Food":
                with open("Dinesh food.txt", "a") as f:
                    a = input("Enter food data:")
                    print()
                    b = get_date()
                    f.write(str(b + "   " + a + "\n"))
                    print("Entry Successful")
            else:
                with open("Dinesh exercise.txt", "a") as f:
                    a = input("Enter exercise data:")
                    print()
                    b = get_date()
                    f.write(str(b + "   " + a + "\n"))
                    print("Entry Successful")

ask = int(input("Enter the following number as per function to be executed:\n1 - Retrieve data\n2 - Log data\n"))
if ask == 1:
    retrieve_data()
else:
    client_dic, name_input = client_name()
    activity, act_input = select_log(client_dic, name_input)
    data_entry(client_dic, name_input, activity, act_input)