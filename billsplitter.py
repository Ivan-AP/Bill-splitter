import random


def gathering_friends():
    num_of_friends = int(input("Enter the number of friends joining (including you):"))
    print()
    if num_of_friends <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        guests = [input() for _ in range(num_of_friends)]
        print()
        total_bill = int(input("Enter the total bill value:"))
        party = {guest: round(total_bill / num_of_friends, 2) for guest in guests}
        print()
        lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        print()
        if lucky_feature == "Yes":
            lucky = guests[random.randint(0, len(guests) - 1)]
            print(f'{lucky} is the lucky one!')
            print()
            party = {guest: round(total_bill / (num_of_friends - 1), 2) for guest in guests}
            party[lucky] = 0
            print(party)
        else:
            print('No one is going to be lucky')
            print()
            print(party)


gathering_friends()
