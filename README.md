For this challenge you need to write a program that checks an input file for it's similarity to actual words.

You will be given a fixed word list and your program will recieve a single parameter - a path to a text file, it will output a single number equal to  the number of changes required to make that file contain only valid words. 

For example given the sentence:

the quivk browb fpx jymps ober the lazy cog

the program will output 

5 

this is because 5 changes are the minimum number of changes required to make the sentence valid.
the quivk browb fpx jymps ober the lazy cog
*** ***c* ****n *o* *u*** *v** *** **** ***

** it doesn't matter whether the corrected sentence makes sense or not, just that all of the changed words are in the supplied word list. Note that cog is not changed in this example as it is already a valid word.

For each word W in the file, you must find the word W' from the word list, so that the number of alterations from W to W' is minimised. It is valid that W is already W' and the number of changes required is nil. The definition of a change is either the replacement of a single letter with any other letter, inserting a letter in any position or deleting a letter from any position. The score for the provided file is the minimum number of changes required to make all words in the file the.

Input spec:

Your program will take a single parameter, the path to the file name containing some text to analyse. Your program will also open and read the valid word list from the following path location:

    /var/tmp/wordlist.txt

The input file will contain text entirely in lower case seperated by one or more space characters, there will be no other characters. The file might end with a new line character.

Example input file:

    the quivk browb fpx jymps ober the lazy cog

There will be no gotcha's - the input file will be as specified and the valid word list is exactly as the one included in the repository.

Output spec:
The score must be echo'd to stdout as an integer followed by a single new line, eg:

    5
