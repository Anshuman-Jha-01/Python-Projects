import random

# Available moves
moves = ("snake", "water", "gun")

print("\n🎮 Welcome to Snake–Water–Gun Game 🎮")
print("Rules:")
print(" - Snake drinks Water 🐍💧 → Snake wins")
print(" - Water douses Gun 💧🔫 → Water wins")
print(" - Gun kills Snake 🔫🐍 → Gun wins")
print(" - Same move → It's a Draw!\n")

while True:
    f = open("game.txt", "r")
    txt = f.read()
    li = txt.split(",")
    wins = int(li[0])
    losses = int(li[1])
    f.close()

    user_score = 0
    comp_score = 0
    turns = 1

    # Play 3 turns per round
    while turns <= 3:
        print(f"\n--- Turn {turns} ---")
        user_move = input("Choose [Snake / Water / Gun]: ").strip().lower()
        comp_move = random.choice(moves)

        print(f"👉 You chose: {user_move.capitalize()}")
        print(f"🤖 Computer chose: {comp_move.capitalize()}")

        # User chooses snake
        if user_move == "snake":
            if comp_move == "snake":
                user_score += 1
                comp_score += 1
                print("⚖️ It's a Draw!")
            elif comp_move == "water":
                user_score += 1
                print("🎉 Hooray! You scored a point.")
            else:
                comp_score += 1
                print("💻 Dang! The computer scored a point.")
            turns += 1

        # User chooses water
        elif user_move == "water":
            if comp_move == "snake":
                comp_score += 1
                print("💻 Dang! The computer scored a point.")
            elif comp_move == "water":
                user_score += 1
                comp_score += 1
                print("⚖️ It's a Draw!")
            else:
                user_score += 1
                print("🎉 Hooray! You scored a point.")
            turns += 1

        # User chooses gun
        elif user_move == "gun":
            if comp_move == "snake":
                user_score += 1
                print("🎉 Hooray! You scored a point.")
            elif comp_move == "water":
                comp_score += 1
                print("💻 Dang! The computer scored a point.")
            else:
                user_score += 1
                comp_score += 1
                print("⚖️ It's a Draw!")
            turns += 1

        # Invalid input
        else:
            print("❌ Invalid choice! Please select Snake, Water, or Gun.")

    # Check winner after 3 turns
    print("\n===== Round Result =====")
    if user_score == comp_score:
        print(f"🤝 The game is a draw! Final Score: {user_score} : {comp_score}")
    elif user_score > comp_score:
        print(f"🏆 Congratulations! You won the game {user_score} : {comp_score}")
        with open("game.txt", "w") as f:
            wins+=1
            f.write(f"{wins},{losses}") 
    else:
        print(f"😔 Sorry! You lost the game {user_score} : {comp_score}")
        with open("game.txt", "w") as f:
            losses+=1
            f.write(f"{wins},{losses}") 

    # Ask to continue
    cont = input("\nDo you want to play another round? (Y/N): ").strip().lower()
    if cont == "n":
        print("\n👋 Thanks for playing! Goodbye!")
        break
    else:
        user_score = 0
        comp_score = 0
        turns = 1



# Display final stats
with open("game.txt", "r") as f:
    txt = f.read()
    li = txt.split(",")
    wins = int(li[0])
    losses = int(li[1])

print("\n===== 📊 Final Game Stats 📊 =====")
print(f"✨ Total Wins: {wins}")
print(f"💔 Total Losses: {losses}")
print("=================================")

           

