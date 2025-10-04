import random

def hangman():
    # Predefined words list
    words = ["python", "coding", "program", "hangman", "developer"]
    word = random.choice(words)  
    guessed_letters = set()     
    attempts = 6                 
    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.\n")
    print("_ " * len(word)) 

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(display_word)
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)
if __name__ == "__main__":
    hangman()
