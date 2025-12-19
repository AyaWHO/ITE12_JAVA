class Question:                  # Store/hold the details of each question (text, choices, correct answer, points, difficulty)
    def __init__(self, question: str, choices: list, answer: str, points: int, difficulty: str):     #'_init_ method = constructor 
       
        self.question = question             #self. = this. sa java
        self.choices = choices
        self.answer = answer.upper()
        self.points = points
        self.difficulty = difficulty

    # Method for display(), (question, difficulty, points, and choices)
    def display(self):            
        print("\n╔════════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"║ Difficulty: {self.difficulty}")
        print(f"║ For {self.points} points")     #access info/variable using 'self.'
        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ Question: {self.question}")
        print("║")

        for c in self.choices:
            print("║ " + c)
        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

# Function para sa pag deduct_money(), Computes how much money will be deducted when the user gets a question wrong
def deduct_money(money, points):
    return (points / 100.0) * money

# Function, para sa pag ask_question(), check kung correct or dili
def ask_question(q):              #q kay ang question (question object)
    correct = False
    chances = 3 

    q.display()                   #tawagon ang display method ug e display

    while chances > 0:
        ans = input("\nEnter your answer (A / B / C / D): ").strip().upper()  #Strip mag remove ug space to reduce error,erase extra space, input ma covert siya ug Upper case                              
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

# Class 
class Player:
    def __init__(self, name, age, address):            
        self.name = name
        self.age = age
        self.address = address

    # Method display user info
    def display_info(self):
        print("\n╔════════════ PLAYER INFORMATION ════════════╗")
        print(f"║ Name    : {self.name}")
        print(f"║ Age     : {self.age}")
        print(f"║ Address : {self.address}")
        print("╚════════════════════════════════════════════╝")


# Function to start game (INTRO UG UBAN DETAILS)
def start_game():
    money = 1000000000.0        #Initial na mga values (float sa money)
    total_points = 0
    questions_answered = 0

    print("\n============================ WELCOME TO WHO WANTS TO BE A BILLIONAIRE ============================")
    print("       *=*=*=*=*=*=*=*=*=*=*=*=*=* Twisted Wonderland Edition *=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("\nDirections: Answer all questions correctly to win the Billion Money! Each question has corresponding point value (Easy-20, Average-40, and Hard-60), the more difficult the question the higher the points")
    print("\nNote: If you answer a question incorrectly, the points for that question will be deducted from your total prize. For example, if you miss a 20-point question, 20% will be deducted from your Billion Money.\n")

    agree = input("Enter Y(Yes) or N(No) to Proceed: ").strip().upper()
    if agree != "Y":
        print("You did not agree. Returning back to the menu...")
        return
    
    # Player Information Input
    print("\n===== Enter the following =====")
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")

    player = Player(name, age, address)    #player object (ug mag tawag constructor)
    player.display_info()                  #Calls and display method 'display_info' sa class Player

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
        Question(
            "Who is the housewarden of Savanaclaw?", ["A. Leona", "B. Ruggie", "C. Rook", "D. Jack"],
            "A", 55, "Hard"
        )
    ]

    # Loop through all questions (isa-isa)
    for q in questions:
        print("\n< <<======================== QUESTION ========================>> >")
        print(f"Current Prize: PHP {money:,.0f}")

        correct = ask_question(q)   #tawagon ang function na 'ask_question' 
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

    # Game Over Display
    print("\n================>>> GAME OVER <<<================")
    print(f"Remaining Money: PHP {money:,.0f}")
    print(f"Total Points Earned: {total_points}")
    print(f"You answered {questions_answered} question(s).")
    print("\n================>>>>>>>>><<<<<<<<<================\n")


# Function Main Menu 
def main():
    while True:                            #repeat forever until exit(2) is chosen by the user
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
            print("\n╔══════════════════════════════════╗")
            print("║ Thank you for playing! (or not)")
            print("╚══════════════════════════════════╝\n")
            break
        else:
            print("\nInvalid choice. Try again.")

main()     #diri mag start since na define naman ang 'main'

