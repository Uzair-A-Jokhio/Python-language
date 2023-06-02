print("Name of county which WON the 1992 CWC? ")
secret_word = "pakistan"
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ").lower()
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("OUT of guesses, YOU LOSE! ")
else:
    print("Correct!! You win!!")
