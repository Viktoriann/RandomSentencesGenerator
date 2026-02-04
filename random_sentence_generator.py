import random

def get_random_word(words):
    return random.choice(words)


names = ["Angela", "David", "Peter", "Jane", "Steve", "Carmen", "Michell", "Lucy"]
places = ["London", "New York", "Paris", "Tokyo", "Sofia", "Rome", "Madrid", "Sydney"]
verbs = ["eats", "play with", "holds", "sees", "brings"]
nouns = ["stones", "cake", "phone", "ball", "bikes", "chair", "umbrella", "window"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "in the bar", "outside", "at work"]

print(f"Hello, this is your first random sentence:")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print("*******************************************")
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
    print("*******************************************")
    print("\n")
    should_continue = input("Would you like to generate a new random sentence? (y/n) ").lower()

    if should_continue == "n":
        print("Goodbye!")
        break
    elif should_continue != "y":
        print("Invalid output. Try again.")
        should_continue = input("Would you like to generate a new random sentence? (y/n) ").lower()

