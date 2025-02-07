# English-to-Hindi Dictionary
word_dict = {}

while True:
    print("\n🔹 Menu:")
    print("1️⃣ Add a new word")
    print("2️⃣ Look up a Hindi meaning")
    print("3️⃣ Display all words")
    print("4️⃣ Check if a word exists")
    print("5️⃣ Exit")
    
    choice = input("👉 Enter your choice (1-5): ").strip()

    if choice == "1":
        eng_word = input("📝 Enter an English word: ").strip().lower()
        
        if eng_word in word_dict:
            print(f"⚠️ '{eng_word}' already exists with meaning: '{word_dict[eng_word]}'")
        else:
            hindi_word = input("🎯 Enter its Hindi meaning: ").strip()
            word_dict[eng_word] = hindi_word
            print(f"✅ '{eng_word}' added with meaning '{hindi_word}'")

    elif choice == "2":
        search_word = input("🔎 Enter an English word to find its Hindi meaning: ").strip().lower()
        meaning = word_dict.get(search_word, "❌ Not found in dictionary.")
        print(f"📝 Hindi meaning: {meaning}")

    elif choice == "3":
        if word_dict:
            print("\n📚 English to Hindi Dictionary:")
            for eng, hin in word_dict.items():
                print(f"🔹 {eng} → {hin}")
        else:
            print("⚠️ The dictionary is empty!")

    elif choice == "4":
        check_word = input("🔍 Enter an English word to check if it exists: ").strip().lower()
        if check_word in word_dict:
            print(f"✅ Yes, '{check_word}' exists with meaning '{word_dict[check_word]}'")
        else:
            print(f"❌ No, '{check_word}' is not found in the dictionary.")

    elif choice == "5":
        print("👋 Exiting the program. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please enter a number between 1 and 5.")
