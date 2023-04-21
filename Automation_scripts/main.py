def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
#the function of above
#hours, minutes, remaining_seconds = convert_second(5000)
#print(hours, minutes, remaining_seconds)

def lucky_number(name):
    number = len(name) * 9
    print(f"hello, {name}. Your lucky number is {number}")

#lucky_number("shamir")
#lucky_number("Uzair")

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km


def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

email = "uzairarifjokhio@gmail.com" \
        "shamirarif@gmail.com" \
        "rimssh@gmail.com"
old_domain1 = "gmail.com"
new_domain1 = "yahoo.com"

print(replace_domain(email,old_domain1,new_domain1))


