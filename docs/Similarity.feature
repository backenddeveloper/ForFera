Feature: The Smiliarity checker class.
    This is designed to provide the functionality to support an answer to the Fera technical challange.
    This is built with the intention of being part of code review.
    This will calculate the number of single letter substitutions, additions or removals required to make 
    each word in a sentance a valid word within the constraints of a given wordlist.

    Scenario: The distance method uses Levenshtein string matching to calculate string difference.
    Given access to the SimilarityChecker class,
    When we call the distance method with two strings,
    Then it will return the Levenshtein distance between the two strings.
    
    Scenario: When given a (word) list and a single word it finds the smallest distance word in the list.
    Given access to the SimilarityChecker class,
    And a list containing different words,
    And a single word,
    When we call the closest match method,
    Then the closest matching word is returned,
    As is the Levenshtein distance.

    Scenario: The closest match method raises an Error when an empty word or an empty wordlist is given.
    Given access to the SimilarityChecker class,
    And a wordlist,
    And a single word,
    And either the wordlist or the single word is empty,
    When we call the closest match method,
    Then an Error is raised.
    
    Scenario: It processes a whole sentance and returns the nearest matches.
    Given access to the SimilarityChecker class,
    And a wordlist,
    And a sentance,
    When we call the process sentance method,
    Then a nearest matching sentance and the corresponding total Levenshtein distances is returned.

    Scenario: The process sentance method raises an Error when an empty word or an empty wordlist is given.
    Given access to the SimilarityChecker class,
    And a wordlist,
    And a sentance,
    And either the wordlist or the sentance is empty,
    When we call the process sentance method,
    Then an Error is raised.
