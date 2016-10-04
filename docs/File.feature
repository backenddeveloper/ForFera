Feature: The File class.
    This is designed to provide the functionality to support an answer to the Fera technical challange.
    This is built with the intention of being part of code review.
    This will open a given file and read its content into a list.

    Scenario: The file class opens a file.
    Given an instance of the File class,
    When we call the get content method with a given filename,
    Then it will open the file and return its content.
        
    Scenario: The File class processes input.
    Given we have an instance of the File class,
    And we have a list containing both uppercase, lowercase and non-alphabetic characters,
    When we give this list to the process input method,
    Then the uppercase charaters are turned to lowercase,
    And non-alphabetic characters baring spaces are removed,
    And the list is returned.
    
