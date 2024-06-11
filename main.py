from MCmain import MoveComplete

print("SELECT Message Type:")
print("     1) Move Completes")
selection = input()

if selection == "1":
    mc = MoveComplete()
    mc.moveEm()