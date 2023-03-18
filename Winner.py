import random

player1=0
player2=0

for i in range(5):
    print(f"\nStep {i+1}:")
    while True:
        player1_dice = random.randint(1, 6)
        player2_dice = random.randint(1, 6)
        print(f"Player 1 dice number: {player1_dice}")
        print(f"Player 2 dice number: {player2_dice}")

        if player1_dice != player2_dice:
                if player1_dice > player2_dice:
                    print("Player 1 wins!")
                    player1 += 1
                    
                else:
                    print("Player 2 wins!")
                    player2 += 1
                break

        else:
            print("The same number -_- Rolling again...")

if player1 > player2:
    print("\nPlayer 1 is winner:)")
else:
    print("\nPlayer 2 is winner:)")
