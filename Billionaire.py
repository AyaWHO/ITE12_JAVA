# CLASS
# Store/hold the details of each question (text, choices, correct answer, points, difficulty)

class Question:
    def __init__(self, question: str, choices: list, answer: str, points: int, difficulty: str):
        """   #multi-line comment 
        Constructor:
        question  -> string (the question text)
        choices   -> list of strings (choices A-D)
        answer    -> string (correct answer, e.g. 'A')
        points    -> integer (for deduction or score)
        difficulty -> string (difficulty level)
        """
        self.question = question
        self.choices = choices
        self.answer = answer.upper()
        self.points = points
        self.difficulty = difficulty

    # Function: display()
    # Display the question, difficulty, points, and choices
    def display(self):
        print("\n╔════════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"║ Difficulty: {self.difficulty}")
        print(f"║ For {self.points} points")
        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ Question: {self.question}")
        print("║")
        for c in self.choices:
            print("║ " + c)
        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")


# FUNCTION para sa pag deduct_money()
# Computes how much money will be deducted when the user gets a question wrong
def deduct_money(money: float, points: int) -> float:
    """    #multi-line comments
    money  -> float (current money)
    points -> int (percentage deduction)
    returns the deducted amount as float
    """
    return (points / 100.0) * money


# FUNCTION(def) para sa pag ask_question()
# Handles asking a single question, checking input, giving 3 chances
def ask_question(q: Question) -> bool:              #question object ug mag return ture or false
    chances = 3
    correct = False

    q.display()

    while chances > 0:
        ans = input("\nEnter your answer (A / B / C / D): ").strip().upper()  #Strip mag remove ug space to reduce error
                                                                              #upper mo covert siya ug Upper case
        if ans == q.answer:
            print("╔══════════╗")
            print("║ Correct!")
            print("╚══════════╝")
            correct = True
            break
        else:
            chances -= 1
            print("╔════════╗")
            print("║ Wrong!")
            print("╚════════╝")

            if chances > 0:
                print(f"Try again. Chances left: {chances}")
            else:
                print("No more chances for this question.")

    return correct


# FUNCTION para ma start_game()
# Controls the entire game process from intro to asking all questions
def start_game():
    money = 1_000_000_000.0        #Initial na mga values
    total_points = 0
    questions_answered = 0

    print("\n============================ WELCOME TO WHO WANTS TO BE A BILLIONAIRE ============================")
    print("       *=*=*=*=*=*=*=*=*=*=*=*=*=* Twisted Wonderland Edition *=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("\nDirections: Answer all questions correctly to win the Billion Money!")
    print("Each question has corresponding points (Easy-15, Average-30, Hard-55)")
    print("\nNote: Wrong answers deduct percentage from money!\n")

    agree = input("Enter Y(Yes) or N(No) to Proceed: ").strip().upper()
    if agree != "Y":
        print("You did not agree. Returning back to the menu...")
        return

    # List of questions
    questions = [
        Question(
            "What is the official name of the school that Yuu got transported to?",
            ["A. Royal Sword Academy", "B. Night Raven College", "C. Noble Bell College", "D. Sage's Island Academy"],
            "B", 15, "Easy"
        ),
        Question(
            "Who is the headmaster of Night Raven College?",
            ["A. Leona Kingscholar", "B. Crowley Dire", "C. Kalim Al-Asim", "D. Crewel Divus"],
            "B", 15, "Easy"
        ),
        Question(
            "Which dorm in Twisted Wonderland is inspired by Alice in Wonderland?",
            ["A. Heartslabyul", "B. Savanaclaw", "C. Octavinelle", "D. Diasomnia"],
            "A", 15, "Easy"
        ),
        Question(
            "Which character is heavily inspired by Maleficent?",
            ["A. Trein Mozus", "B. Sebek Zigvolt", "C. Epel Felmier", "D. Malleus Draconia"],
            "D", 30, "Average"
        ),
        Question(
            "What substance forms when negative emotions accumulate inside a mage, leading to Overblot?",
            ["A. Blot Crystals", "B. Phantom Ink", "C. Dark Ether", "D. Obsidian Tar"],
            "A", 30, "Average"
        ),
        Question(
            "Which dorm is known for training students in beauty, aesthetics, and strict self-discipline?",
            ["A. Ignihyde", "B. Diasomnia", "C. Pomefiore", "D. Savanaclaw"],
            "C", 30, "Average"
        ),
        Question(
            "What is the Dark Mirror’s main requirement for choosing new NRC students?",
            ["A. Strong lineage", "B. High magical ability", "C. Compatible magical signature", "D. Potential for power"],
            "C", 55, "Hard"
        ),
        Question(
            "Idia Shroud’s Overblot was caused by what deep-rooted issue?",
            ["A. Anger toward Ortho", "B. Isolation and guilt over Ortho’s death", "C. Forced social events", "D. Betrayal from Azul"],
            "B", 55, "Hard"
        ),
        Question(
            "What caused Azul Ashengrotto to Overblot?",
            ["A. A broken contract", "B. Losing Mostro Lounge", "C. Fear of losing the power he gained", "D. Betrayal by Jade and Floyd"],
            "C", 55, "Hard"
        ),
    ]

    # Loop through all questions
    for q in questions:
        print("\n< <<======================== QUESTION ========================>> >")
        print(f"Current Prize: PHP {money:,.0f}")

        correct = ask_question(q)
        questions_answered += 1

        if correct:
            total_points += q.points
            print(f"You earned {q.points} points!")
        else:
            loss = deduct_money(money, q.points)
            money -= loss
            print(f"You lost {q.points}% of your money!")

        nxt = input("\nProceed to the next question? (Y/N): ").strip().upper()
        if nxt != "Y":
            print("\n╔═════════════════════════════════════════════════════════════════════════╗")
            print(f"║ Thank you for playing! You answered {questions_answered} question(s).")
            print("╚═════════════════════════════════════════════════════════════════════════╝")
            break

    # Game Over
    print("\n================>>> GAME OVER <<<================")
    print(f"Remaining Money: PHP {money:,.0f}")
    print(f"Total Points Earned: {total_points}")
    print(f"You answered {questions_answered} question(s).")
    print("\n================>>>>>>>>><<<<<<<<<================\n")


# MAIN MENU
def main():
    while True:
        print("\n        _===============_      ")
        print("=========   MAIN MENU   =========")
        print("1. Start Game")
        print("2. Exit")
        print("________                ________")
        print("         ===============")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            print("\n╔════════════════════════╗")
            print("║ Thank you for playing!")
            print("╚════════════════════════╝\n")
            break
        else:
            print("\nInvalid choice. Try again.")


main()
