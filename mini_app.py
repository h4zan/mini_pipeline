def main():
    print("Welcome 👋 ")
    print("What is your name?\n")

    while True:
        user_input = input("Enter: ") 
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        else:
            print(f"Hi,{user_input}")

if __name__ == "__main__":
    main()
