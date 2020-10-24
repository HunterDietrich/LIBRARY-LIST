print("*** WELCOME TO THE LIBRARY***")

catalogue = [
    "The Lord of the Rings",
 "Harry Potter",
  "Hunger Games", "The Lion, the Witch, and the Wardrobe",
   "Becoming", 
   "I am Malala",
    "Cooking for Dummies", 
    "The Joy of Cooking"
]


fantasy = [
"The Lord of the Rings",
 "Harry Potter",
  "Hunger Games",
   "The Lion, the Witch, and the Wardrobe"

]

non_fiction = [
    "Becoming", 
   "I am Malala"
]

cooking = [
     "Cooking for Dummies", 
    "The Joy of Cooking"
]

genres = ["FANTASY", "NON-FICTION", "COOKING"]

user_activity = input("What would you like to do? \n [A]Browse [B] Checkout book \n")

if user_activity == "A":
    print("Here are all of our book genres: ")
    for i in genres:
        print(i)
    def read_checkout_options()
genre_select = input("Great. What genre would you like to see?").upper()

while genre_select not in genres:
    genre_select = input("Not a genre. what genre would you like to see in our catalogue \n").upper()

if genre_select == "FANTASY":
        for i in fantasy:
            print(i)
    input("What would you like to do? [A] Read a book from this list in the library or [B] Borrow this book before you leave?")
        while selected_action not in actions:
            selected_action = input("What would you like to do? \n[A] Read a book from this list in the library or \n[B] Borrow this book before you leave?: \n")
        
elif genre_select == "NON-FICTION":
        for i in non_fiction:
            print(i)
        def read_checkout_options()
elif genre_select == "COOKING":
        for i in cooking:
            print(i)
        def read_checkout_options()