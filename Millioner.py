import sys  # Used to exit the program on wrong answer

print("*** Who becomes a Millioner ***")
print("Choose an answer between (a, b, c, d)\n")

prize = 0  # Initial prize

# Function to ask a question with its specific prize
def ask_question(question_text, correct_option, correctAns, question_prize):
    global prize  # Access global prize variable
    answer = input(question_text).strip().lower()
    
    if answer == correct_option:
        print("Correct answer!")
        prize += question_prize
        print(f"You won: {prize} Rs.\n")
    else:
        print("Wrong answer!")
        print("Correct answer is ",correctAns)
        print(f"You won a total of {prize} Rs. in 'Kon Banega Crorepati!!!'")
        sys.exit()

# Question 1
ask_question("Q1. Who was the first Prime Minister of India?\n"
             "a) Mahatma Gandhi\tb) Sardar Patel\nc) Jawaharlal Nehru\td) Dr. Abdul Kalam\n>>> ", 
             "c","Jawaharlal Nehru", 100000)

# Question 2
ask_question("Q2. Which is the largest river in the world?\n"
             "a) Amazon River\tb) Nile River\nc) Yangtze River\td) Ganga\n>>> ", 
             "b","Nile River",300000)

# Question 3
ask_question("Q3. Which planet is known as the 'Red Planet'?\n"
             "a) Jupiter\tb) Venus\nc) Mars\td) Neptune\n>>> ", 
             "c","Mars", 400000)

# Question 4
ask_question("Q4. Which country gifted the Statue of Liberty to the United States?\n"
             "a) Germany\tb) France\nc) Italy\td) Canada\n>>> ", 
             "b"," France", 500000)

# Question 5
ask_question("Q5. Which is the largest ocean in the world?\n"
             "a) Atlantic Ocean\tb) Indian Ocean\nc) Arctic Ocean\td) Pacific Ocean\n>>> ", 
             "d"," Pacific Ocean", 700000)

# Question 6
ask_question("Q6. Which country is known as the Land of the Rising Sun?\n"
             "a) China\tb) South Korea\nc) Japan\td) Thailand\n>>> ", 
             "c","Japan",3000000)

# Question 7
ask_question("Q7. Who was the first woman to win a Nobel Prize?\n"
             "a) Marie Curie\tb) Malala Yousafzai\nc) Mother Teresa\td) Rosalind Franklin\n>>> ", 
             "a","Marie Curie", 5000000)

# Final prize message
print(f"Congratulations! You won a total of {prize} Rs. in 'Who becomes a Millioner'")
