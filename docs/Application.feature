Feature: The Application class.
    This is designed to provide the core answers to the Fera technical challange.
    This is built with the intention of being part of code review.
    This will open a given wordlist and a given input file adn output the closest 
    matching sentance, with the corresponding total Levenshtein distance.

    Scenario: The Application class runs the application
    Given an instance of the File class,
    And a reference to the SimilarityChecker,
    And an input file name,
    And a wordlist file name,
    When we instanciate the application,
    Then it will read both files,
    And it will call the process sentance method on the Similarity checker,
    And it will output the sentance and distance of that sentance.
        
