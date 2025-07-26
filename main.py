# Recalled foods list from file
with open("recalled_items.txt", "r") as file:
    recalled_items = [line.strip() for line in file.readlines()]

# Print welcome message
print("\n============================================")
print("🧼 Welcome to the Listeria Recall Checker 🧼")
print("❌Check if a food has been recalled❌")
print("============================================")

while True:
    user_input = input("👉🏼 Type here ( or 'exit' to quit): ").lower()

    if user_input == "exit":
        print("👋🏼 Stay safe! Goodbye.")
        break

    print("\n🔍 Checking product...")

    # Check for matches
    matches = [item for item in recalled_items if user_input in item.lower()]

    if matches:
        print("⚠️ WARNING: We found the following recalled item(s) matching your search:")
        for match in matches:
            print(f" - {match}")
    else: 
        print("✅ No recalled items match your search.")

    print()  # Add blank line for better readability