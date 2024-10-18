#Solution to question 2 goes here

#Solution to question 2 goes heredef determine_mushroom():
    # First question: Does your mushroom have gills?
    gills = input("Does your mushroom have gills? (yes/no): ").lower()

    # Second question: Does your mushroom grow in a forest?
    forest = input("Does your mushroom grow in a forest? (yes/no): ").lower()

    # Third question: Does your mushroom have a ring?
    ring = input("Does your mushroom have a ring? (yes/no): ").lower()

    # Based on the answers, determine the mushroom
    if gills == "no":
        print("The mushroom you are thinking of is: Cepe de bordeaux.")
    elif forest == "no" and ring == "yes":
        print("The mushroom you are thinking of is: Coprin chevelu.")
    elif forest == "no" and ring == "no":
        print("The mushroom you are thinking of is: Agaric jaunissant.")
    elif ring == "yes":
        print("The mushroom you are thinking of is: Amanite tue-mouche.")
    elif ring == "no" and gills == "yes" and forest == "yes":
        convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").lower()
        if convex_cup == "yes":
            print("The mushroom you are thinking of is: Pied Bleu.")
        else:
            print("The mushroom you are thinking of is: Girolle.")
    else:
        print("Sorry, I couldn't determine the mushroom.")

# Run the program
determine_mushroom()
