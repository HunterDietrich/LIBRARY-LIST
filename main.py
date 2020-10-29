print("*** WELCOME TO THE LIBRARY ***")

catalogue = [
    "The Lord of the Rings", 
    "Harry Potter", 
    "Hunger Games", 
    "The Lion, the Witch, and the Wardrobe", 
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

def read_checkout_options():
    actions = ["A", "B"]
    selected_action = input("What would you like to do? [A] Read a book from this list in the library? or [B] Borrow this book before you leave").upper()
    while selected_action not in actions:
        selected_action = input("Not valid. What would you like to do? \n[A] Read a book from this list in the library? or \n[B] Borrow this book before you leave?: \n")

        if selected_action == "A":
            # call read function (HOMEWORK)
        elif selected_action == "B":
            # call checkout/borrow function (HOMEWORK)

user_activity = input("What would you like to do? \n [A]Browse [B]Checkout a book \n").upper()

if user_activity == "A":
    print("Here are all of our book genres: ")
    for i in genres:
        print(i)
    
    genre_select = input("What genre would you like to see? \n").upper()
    # input validation
    while genre_select not in genres:
        genre_select = input("Not a genre we have. What genre would you like to see in our catalogue? \n").upper()

    if genre_select == "FANTASY":
        for i in fantasy:
            print(i)
        read_checkout_options()
        
    elif genre_select == "NON-FICTION":
        for i in non_fiction:
            print(i)
        read_checkout_options()

    elif genre_select == "COOKING":
        for i in cooking:
            print(i)
        read_checkout_options()