import java.util.Scanner;
 
class Question {            // objects - maoy mo store or mo save sa mga details sa pangutana (text, choices, sakto nga answer, points, difficulty)
    String question;        // string sa question (store)
    String[] choices;       // list sa mga choices A-D
    String answer;          // string sa correct answer
    int points;             // percent deduction kung mali ang answer
    String difficulty;      // string sa difficulty level


    // Constructor — method mag set/assign ug initial values na mo auto run 
    public Question( String question, String[] choices, String answer, int points, String difficulty) {  // public para ma access sa uban classes
        this.question = question;        // set ang qustions (this.''' kay ang variable(kadtong object na gi create), ang ''' value)
        this.choices = choices;          // set ang choices
        this.answer = answer;            // gi set ang sakto nga answer
        this.points = points;            // gi set ang points para deduction
        this.difficulty = difficulty;    // set ang difficulty
    }

    // Method - function inside a class nga mo display sa QUESTIONS ug uban info (difficulty, points, choices)
    public void display() {                                     // void (non-return) dili mobalik ang value mag display ra
        System.out.println("\n╔════════════════════════════════════════════════════════════════════════════════════════════╗");                     
        System.out.println("║ Difficulty: " + difficulty);      // display difficulty level
        System.out.println("║ For " + points + " points");      // display kung pila ka points
        System.out.println("╠════════════════════════════════════════════════════════════════════════════════════════════╣");
        System.out.println("║ Question: " + question);          // display question
        System.out.println("║");

        // for each loop para i-display ang each choices (A-D)
        for (String c : choices) {                              //temporary na e call ang choices ug 'c'   
            System.out.println("║" + c);                        // display each choice 
        }
        System.out.println("╚════════════════════════════════════════════════════════════════════════════════════════════╝");
    }
}


public class Main {

    //Method mo deduct sa money (deductMoney())
    //calculates pila ang kwarta ma deduct kung ma mali ug answer

        public static double deductMoney(double money, int points) {      //static - ma access without object
            return (points / 100.0) * money;                              // formula for deduction - need double para decimal ang result
        }

    // nag handle sa process sa mga questions (askQuestion) 
    public static boolean askQuestion(Question q, Scanner scan) {     
        int chances = 3;                                              // 3 attempts or chances sa user
        boolean correct = false;                                      // ilhanan kung sakto or mali ang answer

        q.display();                                                  // e display ang question 

       
        while (chances > 0) {                                         // loop hangtod mahurot ang chances - loop as long condition is met
            System.out.print("\nEnter your answer ( A /B /C /D ): ");
            String ans = scan.next().toUpperCase();                   // covert ang answer or 'ans' to uppercase para limpyo ang input

            if (ans.equals(q.answer)) {                               // if sakto ang answer (if ang answer sa user = sa correct na answer)
                System.out.println("╔══════════╗");
                System.out.println("║ Correct!");
                System.out.println("╚══════════╝");
                correct = true;                                       // mark as correct
                break;                                                // exit sa loop 

            } else {
                chances = chances -1;                                 // wrong answer = kuhaan ug chance

                if (chances > 0) {                                    // if naa pay chances 
                    System.out.println("╔════════╗");
                    System.out.println("║ Wrong!");
                    System.out.println("╚════════╝");
                    System.out.println("Try again. Chances left: " + chances);

                } else {
                    System.out.println("╔════════╗");               // comdition if wala nay chances
                    System.out.println("║ Wrong!");
                    System.out.println("╚════════╝");
                    System.out.println("No more chances for this question.");
                }
            }
        }
        return correct;                                               // ibalik kung asa gi tawag kung true or false
    }

    // Nag-handle sa whole game
    public static void startGame(Scanner scan) {        //scanner ara ma read ang user input (static, function na pwede tawagon walay object)

        double money = 1000000000.0;                    // starting value/money kay 1 Billion
        int totalPoints = 0;                            // starting points kay 0
        int questionsAnswered = 0;                      // counter sa questions answered, starting sa 0 

        // Intro message 
        System.out.println("\n============================ WELCOME TO WHO WANTS TO BE A BILLIONAIRE ============================");
        System.out.println("       *=*=*=*=*=*=*=*=*=*=*=*=*=* Twisted Wonderland Edition *=*=*=*=*=*=*=*=*=*=*=*=*=*=");
        System.out.println("\nDirections: Answer all questions correctly to win the Billion Money! Each question has corresponding point value (Easy-20, Average-40, and Hard)-60, the more difficult the question the higher the points");
        System.out.println("\nNote: If you answer a question incorrectly, the points for that question will be deducted from your total prize. For example, if you miss a 20-point question, 20% will be deducted from your Billion Money.\n");
        
        // Terms & Conditions
        System.out.println("I Agree to the Terms and Conditions.");
        System.out.print("Enter Y(Yes) or N(No) to Proceed: ");
        String agree = scan.next().toUpperCase();

        // Condition if dili mo agree ang user sa Terms & Conditions
        if (!agree.equals("Y")) {                                  //!agree = not agree 
            System.out.println("You did not agree. Returning back to the menu...");
            return;                                                          // exit sa function ug balik sa menu
            
        }

        //Questions
        Question[] questions = {
            new Question(
               "What is the official name of the school that Yuu got transported to?", 
                new String[] {"A. Royal Sword Academy", "B. Night Raven College", "C. Noble Bell College", "D. Sage's Island Academy " }, 
                "B", 15, "Easy" ),

            new Question(
                "Who is the headmaster of Night Raven College?", 
                new String[] {"A. Leona Kingscholar", "B. Crowley Dire", "C. Kalim Al-Asim", "D. Crewel Divus" }, 
                "B", 15, "Easy" ),

            new Question(
                "Which dorm in Twisted Wonderland is inspired by Alice in Wonderland?",
                new String[]{"A. Heartslabyul", "B. Savanaclaw", "C. Octavinelle", "D. Diasomnia"},
                "A", 15, "Easy" ),

            new Question(
                "Which character is heavily inspired by Maleficent",
                new String[]{"A. Trein Mozus ", "B. Sebek Zigvolt", "C. Epel Felmier", "D. Malleus Draconia"},
                "D", 30, "Average"  ),
                
            new Question(
                "What substance forms when negative emotions accumulate inside a mage, leading to Overblot?",
                new String[] {"A. Blot Crystals", "B. Phantom Ink", "C. Dark Ether", "D. Obsidian Tar"},
                "A", 30, "Average"), 
            
            new Question(        
                "Which dorm is known for training students in beauty, aesthetics, and strict self-discipline?",
                new String[]{"A. Ignihyde", "B. Diasomnia", "C. Pomefiore", "D. Savanaclaw"},
                "B",30, "Average" ),  

            new Question(
                "What is the Dark Mirror’s main requirement for choosing new NRC students?",
                new String[]{"A. Strong and Noble lineage", "B. High magical ability", "C. A compatible magical signature", "D. Potential for growth and power"},
                "C",55, "Hard"),

            new Question(
                "Idia Shroud’s Overblot was caused by what deep-rooted issue?",
                new String[]{"A. Anger and fear toward Ortho", "B. Isolation and guilt over Ortho’s death", "C. Being forced into social events", "D. Pressure and Betrayal from Azul"},
                "B",55,"Hard" ),
            
            new Question(
                "What caused Azul Ashengrotto to Overblot?",
                new String[]{"A. A broken contract", "B. Losing his Mostro Lounge business at the NRC", "C. Fear of losing the power he worked hard to gain", "D. Jade and Floyd betraying him"},
                "C",55,"Hard" ),
    
        };

        // Loops sa questions
        for (int i=0; i < questions.length; i++) {              //variable 'i' start at 1, keep looping until mo equal sa length sa questions array--
            Question q = questions[i];                          //after kada loop mag add ug 1 sa 'i' --get question from array positioned at 'i'

            System.out.println("\n< <<======================== WELCOME TO WHO WANTS TO BE A BILLIONAIRE ========================>> >");
            System.out.println("\nPrize: PHP " + money);        // show current money

            boolean correct = askQuestion(q, scan);             // ask/present question
            questionsAnswered++;                                // increment sa questions answered (add one kada question na ma answeran)
            
            if (correct) {                                      // if correct answer then add points
                totalPoints += q.points;
                System.out.println("You earned " + q.points + " points!");
            } 
                                                          
            else {                                              // else then deduct money 
                double loss = deductMoney(money, q.points);
                money -= loss;
                System.out.println("You lost " + q.points + "% of your money!");
            }

            System.out.print("\nProceed to the next question? (Y/N): ");  // ask if mo proceed sa next question
            String next = scan.next().toUpperCase();    

            if (!next.equals("Y")) {                               // if not
                System.out.println("╔═════════════════════════════════════════════════════════════════════════╗");
                System.out.println("║ Thank you for playing! You answered " + questionsAnswered + " question(s).");
                System.out.println("╚═════════════════════════════════════════════════════════════════════════╝");

                break;                                                      // break sa question loop
            }
        }

        // Game Over Message
        System.out.println("\n================>>> GAME OVER <<<================");
        System.out.printf("Remaining Money: PHP %,.0f%n", money);  //print w/format ang float na naay comma, ug zero decimal places
        System.out.println("Total Points Earned: " + totalPoints);
        System.out.println("You answered " + questionsAnswered + " question(s).");
        System.out.println("\n================>>>>>>>>><<<<<<<<<================\n");
    
    }

    //Main menu 
        public static void main(String[] args) {        // Magstart sa java program
        Scanner scan = new Scanner(System.in);          // scanner for input

        while (true) {                                  // infinite loop for menu
            System.out.println("\n        _===============_      ");
            System.out.println("=========   MAIN MENU   =========");
            System.out.println("1. Start Game");
            System.out.println("2. Exit");
            System.out.println("________                ________");
            System.err.println("         ===============");
            System.out.print("\nEnter your choice: ");

            String choice = scan.next();

            if (choice.equals("1")) {
                startGame(scan);                         // start the game
            } 
            else if (choice.equals("2")) {
                System.out.println("\n╔════════════════════════╗");
                System.out.println("║ Thank you for playing!");
                System.out.println("╚════════════════════════╝\n");
                break;                                  // exit program
            } 
            else {
                System.out.println("\nInvalid choice. Try again.");
            }
        }

        scan.close();                                   // para dili magpadayon og gamit og memory scanner
    }
}