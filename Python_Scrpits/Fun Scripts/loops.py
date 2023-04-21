
def wall_loop():
    #the input of user!!
    num = int(input("Enter the height! "))

    #for loop 
    for _ in range(num):
        #will print '#' vertically and horizontally to creat an illusion of wall 
        print("#" * num , end="  ")


def even_thing():
    even1 = int(input("enter number: ")) #asking for the last digit for determing even 
    #a list is create 
    even_num = []

    for i in range(1, even1):
        #to check if the value in range is even
        if i % 3 == 0:
            even_num.append(i)

    print("Even number: " , even_num ) 
 



