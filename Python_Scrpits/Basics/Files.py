guest = open("guest.txt","w")
guest_list = [ "uzair", "zain", "anas", "rimsha" ]

for i in guest_list:
    guest.write(i + "\n")

guest.close()

new_list = ["arif", "sainya", "ali"]

with open("guest.txt", "a") as guest:
    for i in new_list:
        guest.write(i + "\n")

guest.close()

with open("guest.txt") as guest:
    for line in guest:
        print(line.strip())

