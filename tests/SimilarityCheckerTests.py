from unittest import TestCase
from collections import OrderedDict as Map
from src.SimilarityChecker import SimilarityChecker

class SimilarityCheckerTests(TestCase):

    def test_levenshtein_matching(self):

        # No changes
        self.assertEqual(0 , SimilarityChecker.distance('cog' , 'cog'))

        # Single changes
        self.assertEqual(1 , SimilarityChecker.distance('quick' , 'quivk'))
        self.assertEqual(1 , SimilarityChecker.distance('quick' , 'quik'))
        self.assertEqual(1 , SimilarityChecker.distance('quick' , 'quicck'))

        # Paired changes
        self.assertEqual(2 , SimilarityChecker.distance('jumps' , 'jympss'))
        self.assertEqual(2 , SimilarityChecker.distance('jumps' , 'jmpss'))
        self.assertEqual(2 , SimilarityChecker.distance('jumps' , 'jymp'))

        # Combination change
        self.assertEqual(3 , SimilarityChecker.distance('over' , 'oobe'))

    def test_closest_match(self):

        wordlist = ['one' , 'two' , 'three' , 'four' , 'five']

        word = 'one'
        self.assertEqual(
            {'distance' : 0 , 'word' : 'one'} , 
            SimilarityChecker.closest_match(wordlist , word)
        )

        word = 'ttwo'
        self.assertEqual(
            {'distance' : 1 , 'word' : 'two'} ,
            SimilarityChecker.closest_match(wordlist , word)
        )

        word = 'thrrr'
        self.assertEqual(
            {'distance' : 2 , 'word' : 'three'} , 
            SimilarityChecker.closest_match(wordlist , word)
        )

    def test_closes_match_raises_error(self):

        with self.assertRaises(ValueError):
            SimilarityChecker.closest_match(['wordlist'] , '')

        with self.assertRaises(ValueError):
            SimilarityChecker.closest_match([] , 'word')

    def test_proccess_sentance(self):
        sentance = 'the quivk browb fpx jymps ober the lazy cog'
        wordlist = ['the' , 'quick' , 'brown' , 'fox' , 'jumps' , 'over' , 'the' , 'lazy' ,'cog']
        closest_sentance = SimilarityChecker.process_sentance(wordlist , sentance)
        self.assertEqual(closest_sentance , {'sentance' : 'the quick brown fox jumps over the lazy cog' , 'distance' : 5})

    def test_process_sentance_raises_error(self):

        with self.assertRaises(ValueError):
            SimilarityChecker.process_sentance(['wordlist'] , '')

        with self.assertRaises(ValueError):
            SimilarityChecker.process_sentance([] , ['sentance'])
