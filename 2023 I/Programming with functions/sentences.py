import random
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    single_nouns = [
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    ]
    plural_nouns = [
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    ]
    if quantity == 1:
        return random.choice(single_nouns)
    else:
        return random.choice(plural_nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    past_verbs = [
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    ]
    present_single_verbs = [
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    ]
    present_plural_verbs = [
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    ]
    future_verbs = [
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    ]

    if tense == "past":
        return random.choice(past_verbs)
    elif tense == "present" and quantity == 1:
        return random.choice(present_single_verbs)
    elif tense == "present" and quantity != 1:
        return random.choice(present_plural_verbs)
    elif tense == "future":
        return random.choice(future_verbs)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    preposition = random.choice(prepositions)
    return preposition
    
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposition} {determiner} {noun}"

def main():
    """Generate and print six sentences with a determiner,
    a noun, a verb, and a prepositional phrase. Each sentence
    will have a different combination of quantity and verb tense.
    """

    # First sentence: single past
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prepositional_phrase = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

    # Second sentence: single present
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prepositional_phrase = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

    # Third sentence: single future
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prepositional_phrase = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

    # Fourth sentence: plural past
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "past")
    prepositional_phrase = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

    # Fifth sentence: plural present
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "present")
    prepositional_phrase = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

    # Sixth sentence: plural future
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "future")
    prepositional_phrase = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.".capitalize())

if __name__ == "__main__":
    main()
