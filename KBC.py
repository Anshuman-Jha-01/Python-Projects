quiz = {
    "1": {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "paris",
        "prize": 1000
    },
    "2": {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "mars",
        "prize": 2000
    },
    "3": {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Mark Twain"],
        "answer": "william shakespeare",
        "prize": 3000
    },
    "4": {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "pacific ocean",
        "prize": 4000
    },
    "5": {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Osmium", "Iron"],
        "answer": "oxygen",
        "prize": 5000
    },
    "6": {
        "question": "In computing, what does 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Power Utility", "Control Program Unit", "Central Program Utility"],
        "answer": "central processing unit",
        "prize": 6000
    },
    "7": {
        "question": "Which language is primarily spoken in Brazil?",
        "options": ["Spanish", "Portuguese", "French", "English"],
        "answer": "portuguese",
        "prize": 7000
    }
}

totalPrize = 0
print("\n" + "="*40)
print("        🎉 WELCOME TO KBC 🎉")
print("="*40 + "\n")

for key in quiz:
    print(f"💡 Question {key}: {quiz[key]['question']}")
    print("Options:")
    for i, option in enumerate(quiz[key]['options'], start=1):
        print(f"   {i}. {option}")
    
    ans = input("\n👉 Enter your answer: ").strip().lower()
    print()
    
    if ans == quiz[key]['answer']:
        totalPrize += quiz[key]['prize']
        print("✅ Correct! 🎯")
        print(f"💰 You have won ${totalPrize} so far.\n")
        print("-"*40 + "\n")
    else:
        print("❌ Oops! Wrong answer.")
        print(f"✔️ The correct answer was: {quiz[key]['answer'].title()}")
        print("\n" + "-"*40)
        print(f"🎉 Congratulations! You take home ${totalPrize}.")
        print("-"*40 + "\n")
        break
else:
    print("\n" + "-"*40)
    print("🏆 Horray! You answered all questions correctly!")
    print("🎉 Congratulations on becoming a MILLIONAIRE! 🎉")
    print("-"*40 + "\n")