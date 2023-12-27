def attempts(n):
    x = 1         # the value of x shall remain 1
    while x <= n:
        print(f"attempt no: {str(x)}")
        x += 1
    print("done")

def count_down(start_count):
    current = start_count
    while current >= 0:
        print(current)
        current += -1
    print("done")


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        n = n / 2
        if n == 0:
            return False
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False



def decade_counter(year):
	while year < 50:
		year += 10
	return year



