from src.File import File
from src.SimilarityChecker import SimilarityChecker

class Application:

    def __init__(self , input_file , wordlist_file , file=File() , 
                similarity_checker=SimilarityChecker , print_function=print):
        sentance = file.read(input_file)[0]
        wordlist = file.read(wordlist_file)
        closest_sentance = similarity_checker.process_sentance(wordlist , sentance)
        print_function('Closest sentance: ' + closest_sentance['sentance'])
        print_function('Total number of changes that had to be made: ' + str(closest_sentance['distance']))
