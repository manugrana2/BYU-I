from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun is a string.
        assert isinstance(word, str)

    # 2. Test the plural nouns.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun is a string.
        assert isinstance(word, str)

def test_get_verb():
    # 1. Test the past verbs.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a past verb.
        verb = get_verb(1, "past")

        # Verify that the verb returned from get_verb
        # is one of the verbs in the past_verbs list.
        assert verb in past_verbs

    # 2. Test the present verbs.

    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present verb for single nouns.
        verb = get_verb(1, "present")

        # Verify that the verb returned from get_verb
        # is one of the verbs in the present_single_verbs list.
        assert verb in present_single_verbs

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present verb for plural nouns.
        verb = get_verb(2, "present")

        # Verify that the verb returned from get_verb
        # is one of the verbs in the present_plural_verbs list.
        assert verb in present_plural_verbs

    # 3. Test the future verbs.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future verb.
        verb = get_verb(1, "future")

        # Verify that the verb returned from get_verb
        # is one of the verbs in the future_verbs list.
        assert verb in future_verbs

def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]

    for _ in range(4):
        preposition = get_preposition()

        assert preposition in prepositions

def test_get_prepositional_phrase():
    single_determiner = ["a", "one", "the"]
    plural_determiner = ["some", "many", "the"]
    single_nouns = [
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    ]
    plural_nouns = [
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    ]
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]

    #Test with quantity singular
    for _ in range(4):
        phrase = get_prepositional_phrase(1)
        phrase = phrase.split(" ")
        #return f"{preposition} {determiner} {noun}"
        assert phrase[0] in prepositions and phrase[1] in single_determiner and phrase[2] in single_nouns

    #Test with quantity plural
    for _ in range(4):
        phrase = get_prepositional_phrase(2)
        phrase = phrase.split(" ")
        #return f"{preposition} {determiner} {noun}"
        assert phrase[0] in prepositions and phrase[1] in plural_determiner and phrase[2] in plural_nouns


pytest.main(["-v", "--tb=line", "-rN", __file__])
