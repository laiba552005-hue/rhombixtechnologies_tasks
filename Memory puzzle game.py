import random

cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
random.shuffle(cards)

print("Actual Cards:", cards)  # Testing ke liye

revealed = ['*'] * 8

while '*' in revealed:
    print("\nVisible Cards:", revealed)

    pos1 = int(input("First position: "))
    pos2 = int(input("Second position: "))

    print("Card 1 =", cards[pos1])
    print("Card 2 =", cards[pos2])

    if cards[pos1] == cards[pos2]:
        revealed[pos1] = cards[pos1]
        revealed[pos2] = cards[pos2]
        print("Match Found!")
    else:
        print("Not a Match!")