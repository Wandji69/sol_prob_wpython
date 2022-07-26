while True:
    try:
        number = int(input("please enter number"))
    except ValueError:
        print("You did enter a number")
    except:
        print("An unknow error occured")
    print("thank you for entering a number")
