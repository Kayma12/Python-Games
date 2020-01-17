import random

def ran_number():
    num = random.randint(1, 100)
    return num


def guess_game():
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("To stop early write STOP")
    print("LET'S PLAY!")

    num = ran_number()
    guess_times = 0
    diff = []
    temperature = ''

    while True:

        your_guess = (input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

        if (str(your_guess)).lower() == 'stop':

            print('You have ended the game')
            break
        your_guess = int(your_guess)
        if your_guess < 1 or your_guess > 100:
            print('OUT OF BOUNDS! Please try again: ')
            continue
        int(your_guess)
        diff.append(abs(num - your_guess))
        if your_guess == num:
            print('You have guessed Correctly you took ' + str(guess_times) + ' attempts')
            break
        if your_guess < 1 or your_guess > 100:
            temperature = 'OUT OF BOUNDS'
        if guess_times < 1:
            guess_times += 1
            if diff[0] <= (10):
                temperature = 'WARM!'
            else:
                temperature = 'COLD!'
        else:
            guess_times += 1
            if abs(diff[guess_times - 1] < diff[guess_times - 2]):
                temperature = 'WARMER!'
            else:
                temperature = 'COLDER!'
        print(temperature)