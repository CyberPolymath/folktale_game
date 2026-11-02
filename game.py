POINTS_CORRECT = 2
POINTS_WRONG = -1


class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

python_questions = [
    {
        "question": "What does print(type(5.0)) display?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'double'>"],
        "answer": "<class 'float'>",
    },
    {
        "question": "Which keyword is used to define a function in python?",
        "options": ["func", "function", "def", "define"],
        "answer": "def",
    },
    {
        "question": "what is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "23"],
        "answer": "8",
    },
    {
        "question": "Which of these data types is immutable?",
        "options": ["list", "dictionary", "set", "tuple"],
        "answer": "tuple",
    },
    {
        "question": "What does 'Hello'[1] return?",
        "options": ["H", "e", "l", "Error"],
        "asnwer": "e",
    },
]

maths_questions = [
    {
        "question": "What is 15 x 12?",
        "options": ["170", "180", "190", "200"],
        "answer": "180",
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        "answer": "12",
    },
    {
        "question": "What is 25% of 200?",
        "options": ["25", "40", "50", "75"],
        "answer": "50",
    },
    {
        "question": "What is the value of 7 + 3 x 2?",
        "options": ["20", "13", "16", "10"],
        "answer": "13",
    },
    {
        "question": "Which of these is a prime number?",
        "options": ["15", "21", "17", "27"],
        "answer": "17",
    },
]



categories = {
    "1": Category("Python Language", python_questions),
    "2": Category("Basic Maths", maths_questions),
}


def show_welcome():
    print("=" * 30)
    print("    Welcome to KBC(Kaun Banega Champion)")
    print("="*30)


def choose_category():
    print("\nChoose your Category:")
    for key, category in categories.items():
        print(f"{key}. {category.name}")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice in categories:
            return categories[choice]
        print("Invalid choice. Please enter 1 or 2.")


def show_rules(category):
    total = len(category.questions)
    max_score = total * POINTS_CORRECT

    print("\n" + "=" * 40)
    print("              GAME RULES")
    print("=" * 40)
    print(f"1. You will be asked {total} multiple-choice questions.")
    print("2. Each question has 4 options. Enter the option number (1-4).")
    print(f"3. Correct answer: +{POINTS_CORRECT} points.")
    print(f"4. Wrong answer: {POINTS_WRONG} point.")
    print("5. Every question must be answered. There is no skipping.")
    print("6. There is no timer, but think before you answer.")
    print("   Once you submit an answer, it cannot be changed.")
    print(f"7. Maximum possible score: {max_score}.")
    print("   Your score can go negative if you answer wrongly often.")
    print("8. Play honestly. No AI tools, no internet search,")
    print("   and no help from other people. Play only for yourself.")
    print("=" * 40)

def ask_question(number, total, q):
    print(f"\nQuestion {number}/{total}: {q['question']}")
    for i, option in enumerate(q["options"], start=1):
        print(f" {i}. {option}")

    while True:
        choice = input ("your answer (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return q["options"][int(choice) - 1]
        print("Invalid input. Please enter a number from 1 to 4.")

def play(category):
    score = 0
    correct_count = 0
    total = len(category.questions)

    for number, q in enumerate(category.questions, start =1):
        user_answer = ask_question(number, total, q)

        if user_answer == q["answer"]:
            score += POINTS_CORRECT
            correct_count +=1
            print(f"Correct! + {POINTS_CORRECT} points")
        else:
            score += POINTS_WRONG
            print(f"Wrong! {POINTS_WRONG} point. Correct answer: {q['answer']}")

        print(f"Current score: {score}")

    return score, correct_count, total


def show_results(score, correct_count, total):
    print("\n" + "="*30)
    print("         Game Over")
    print("="*30)
    print(f"Correct answers : {correct_count}/{total}")
    print(f"Final score     : {score} (max possible): {total * POINTS_CORRECT})")

def main():
    show_welcome()
    category = choose_category()
    print(f"\nYou hvae chosen: {category.name}")
    show_rules(category)
    input("\nPress Enter to start...")
    score, correct_count, total = play(category)
    show_result(score, correct_count,total)


main()
