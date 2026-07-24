import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("-" * 30)
    
    length = int(input("Enter password length (default 12): ") or 12)
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")
    
    strength = 'Strong' if length >= 12 and use_symbols else 'Medium' if length >= 8 else 'Weak'
    print(f"Password Strength: {strength}")

main()
