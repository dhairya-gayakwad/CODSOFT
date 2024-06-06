
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
