'''
name:Nicole Nelson
a python program to play stick game
'''
def stick_game():
    print("Rules:")
total_sticks=int(input("Enter the no of sticks: "))
name1=input("Enter the First name:")
name2=input("Enter the Second Name: ")
while total_sticks>0:
    A = int(input(f"{name1}, pick 1,2 or 3 Sticks: "))
    total_sticks-=A
    print("Sticks remaining: ",total_sticks)
    B = int(input(f"{name2}, pick 1,2 or 3 Sticks: " ))
    total_sticks-=B
    print("Sticks remaining: ",total_sticks)
    print(f"there are {total_sticks} sticks left")
    if total_sticks==0:
        print(name2,"wins",name1,"loses")
        break
    print(name2,"your turn:")
    user1=int(input("enter 1,2 or 3 sticks:"))
    total_sticks=user1
    print("sticks remaining:",total_sticks)
    if total_sticks==0:
        print(name1,"wins",name2,"loses")
        break
stick_game()
