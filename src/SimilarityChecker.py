from Levenshtein import distance
from collections import OrderedDict as Map

class SimilarityChecker:

    @staticmethod
    def distance(string_one , string_two):
        return distance(string_one , string_two)

    @staticmethod
    def closest_match(wordlist , word):
        
        if not len(word) or not len(wordlist):
            raise ValueError
        
        closest_word = word
        closest_distance = len(word)
        
        for element in wordlist:
            if SimilarityChecker.distance(element , word) < closest_distance:
                closest_word = element
                closest_distance = SimilarityChecker.distance(element , word)

        return {'distance' : closest_distance , 'word' : closest_word}

    @staticmethod
    def process_sentance(wordlist , sentance):

        if not len(sentance) or not len(wordlist):
            raise ValueError

        closest_sentance = []
        total_distance = 0

        for word in sentance.split(' '):
            match = SimilarityChecker.closest_match(wordlist , word)
            closest_sentance.append(match['word'])
            total_distance += match['distance']

        return {'sentance' : ' '.join(closest_sentance) , 'distance' : total_distance}
