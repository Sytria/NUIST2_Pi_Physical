def quiz():
        print("Welcome to the Animal Quiz!")
        print("Answer the following questions : ")

        questions = [
                "1. What is the largest animal on Earth? : a. Blue Whale, b. Mouse, c. Cat",
                "2. Which bied can fly backwards? : a. Cuckoo, b. Eagle, c. Hummingbird",
                "3. What is the only mammal capable of flight? : a. Bat, b. Squirrel, c. Dolphin"
        ]
        answers = [
                "Blue Whale",
                "Hummingbird",
                "Bat"
        ]
        score = 0

        for i in range(len(questions)):
                user_answer = input(questions[i]).strip().lower()
                if user_answer == answers[i]:
                        print("Correct!")
                        score += 1
                else:
                        print("Incorrect!")

        print("Quiz completed!")
        print(f"You got{score}/{len(questions)} questions correct.")

quiz()

