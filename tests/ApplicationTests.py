from unittest import TestCase
from unittest.mock import MagicMock as Mock
from src.Application import Application


class ApplicationTests(TestCase):

    def test_inits(self):
    
        input_file = 'some input file'
        wordlist_file = 'some wordlist file'
        mock_file = Mock(read=Mock(return_value=['some word']))
        mock_similarity_checker=Mock(process_sentance=Mock(return_value={'sentance' : 'test sentance' , 'distance' : 100}))
        print_function = Mock()

        Application(input_file , wordlist_file , file=mock_file , similarity_checker=mock_similarity_checker , print_function=print_function)
        
        mock_file.read.assert_called__with('some input file')
        mock_file.read.assert_called__with('some wordlist file')
        mock_similarity_checker.process_sentance.assert_called_with(['some word'] , 'some word')
        print_function.assert_called_with('Total number of changes that had to be made: 100')
