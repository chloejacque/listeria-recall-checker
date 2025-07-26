# Recalled foods list from file
with open("recalled_items.txt", "r") as file:
    recalled_items = [line.strip() for line in file.readlines()]
    
# Print welcome message
print("\n============================================")
print("🧼 Welcome to the Listeria Recall Checker 🧼")
print("❌Check if a food has been recalled❌")
print("============================================")
    

while True:
    print("\n🔍 What product or shop are you checking?")
    user_input = input("👉🏼 Type here ( or 'exit' to quit): ").lower()
    
    if user_input == "exit":
        print ("👋🏼 Stay safe! Goodbye.")
        break

# Check for matches
    matches = [item for item in recalled_items if user_input in item.lower()]
    if matches:
        print(f"⚠️ {len(matches)} recalled item(s) found:")
        for match in matches:
            print(f" - {match}")
    else: 
        print ("✅ No recalled items match your search.")

# Convert user input to lowercase for case-insensitive comparison
user_input = user_input.lower()

# Convert all recalled items to lowercase for case-insensitive comparison
lower_recalled_items = [item.lower() for item in recalled_items]

# Now check if user input is a a partial match 
matches = [item for item in recalled_items if user_input in item.lower()]


