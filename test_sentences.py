from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
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

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(4):

        noun = get_noun(1)

        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        noun = get_noun(2)

        assert noun in plural_nouns

def test_get_verb():

    past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):

        verb = get_verb(1 or 2, "past")

        assert verb in past_tense

    single_present_tense = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):

        verb = get_verb(1, "present")

        assert verb in single_present_tense

    plural_present_tense = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):

        verb = get_verb(2, "present")

        assert verb in plural_present_tense

    future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):

        verb = get_verb(1 or 2, "future")

        assert verb in future_tense

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along", 
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]

    for _ in range(4):

        preposition = get_preposition()

        assert preposition in prepositions

def test_get_prepositional_phrase(): 
    
    # prepositions
    prepositions = ["about", "above", "across", "after", "along", 
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]

    for _ in range(4):

        prepositional_phrase = get_prepositional_phrase(1 or 2).split()
        assert len(prepositional_phrase) == 3
        preposition = prepositional_phrase[0]
        assert preposition in prepositions

    # determiners
    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        prepositional_phrase = get_prepositional_phrase(1).split()
        assert len(prepositional_phrase) == 3
        determiner = prepositional_phrase[1]
        assert determiner in single_determiners

    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):

        prepositional_phrase = get_prepositional_phrase(2).split()
        assert len(prepositional_phrase) == 3
        determiner = prepositional_phrase[1]
        assert determiner in plural_determiners

    # nouns
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):

        prepositional_phrase = get_prepositional_phrase(1).split()
        assert len(prepositional_phrase) == 3
        noun = prepositional_phrase[2]
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        prepositional_phrase = get_prepositional_phrase(2).split()
        assert len(prepositional_phrase) == 3
        noun = prepositional_phrase[2]
        assert noun in plural_nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])