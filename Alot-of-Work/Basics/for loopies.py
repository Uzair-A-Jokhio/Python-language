def sumization():
    values = [21, 955, 3526, 21, 13, 98 ]
    sum = 0
    length = 0
    for value in values:
        sum += value
        length += 1

    print(f"The length of characters: {length}")
    print(f"The sum: {sum}")

print("-----------------------------------------------------------------------------------------------------------")

def to_celcius(x):
    return (x - 32) * 5/9

for x in range(0,101,10): # 1st is the start # 2nd is the end # 3rd is the gap left between 1st and 2nd
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))

print("-----------------------------------------------------------------------------------------------------------")

def matches():
    teams = ["kings", "Qalanders", "sultans", "zalmis", "galadiators", "united"]
    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                print("{:>6} VS {:<9}".format(home_team, away_team))

matches()
print("-----------------------------------------------------------------------------------------------------------")

def eum():
    winners = ["uzair","shamir","zain","rimsha","anas"]
    for index, person in enumerate(winners):
        print(f"{index +1} - {person}")

print("-----------------------------------------------------------------------------------------------------------")

def full_emails(people):
    results = []
    for email, names in people:
        results.append(f"{names} <{email}> ")
    return results

print(full_emails([("uzairarifjokhio@gmail.com", "Uzair arif jokhio"),("shamirari8@gmail.com", "Shamir arif jokhio")]))

print("-----------------------------------------------------------------------------------------------------------")

def skip_elements(elements):
    # code goes here
    results = []
    for index, even in enumerate(elements):
        if index % 2 == 0:
            results.append(even)

    return results


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

print("-----------------------------------------------------------------------------------------------------------")

def guest_list(guests):
	for index,(name, age, profesion) in enumerate(guests):    # we can only add two values in enumerate if more than 2 value doo thiss
		print("{} is {} years old and works as {}".format(name,age,profesion))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


print("-----------------------------------------------------------------------------------------------------------")
