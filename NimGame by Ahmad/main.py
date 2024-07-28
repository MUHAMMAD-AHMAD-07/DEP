
while True:
    print("Welcome to the Nim Game :)")
    print("Please select the Game Mode: ")
    print("1. Play against another human")
    print("2. Play against the computer")
    mode = int(input())
    if mode == 1:
        import nimGame
        break
    elif mode == 2:
        import nimGameComp
        break
    else:
        print("Invalid choice. Please select 1 or 2.")

