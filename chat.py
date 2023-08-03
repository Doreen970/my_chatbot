# a function to get user input as argument
def get_answer(user_input):
    user_input = user_input.lower()

    if user_input == "1":
        return "Tech Women is an organisation that is geared towards helping women in marginalised groups pursue tech careers"

    elif user_input == "2":
        return "Women in Africa between the age of 16 and 40 are eligible to pursue this course"
    elif user_input == "3":
        return "We offer the following programs:\n1. Software engineering\n2. Data Science\n3. Networking fundamentals"
    elif user_input == "4":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that option. Please choose a valid number."

def main():
    print("Hi! I'm Tech Women chatbot. How can I help you today?")
    while True:
        print("\nPress [enter] to continue.")
        input()

        print("1. Tell me about Tech Women")
        print("2. What is the eligibility criteria / Who can join?")
        print("3. What programs do you offer?")
        print("4. Exit")

        user_input = input("Choose a number: ")

        if user_input.lower() == "4":
            print("Chatbot: Goodbye! Have a great day!")
            break

        answer = get_answer(user_input)
        print("Chatbot:", answer)

if __name__ == "__main__":
    main()
