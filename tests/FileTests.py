from unittest import TestCase
from unittest.mock import MagicMock as Mock
from src.File import File

class FileTests(TestCase):

    def test_returns_file_content(self):

        file_mock = Mock(readlines=Mock() , close=Mock())
        open_mock = Mock(return_value=file_mock)

        File().read('some file name' , open_function=open_mock)
        
        open_mock.assert_called_once_with('some file name' , 'r')
        file_mock.readlines.assert_called_once_with()
        file_mock.close.assert_called_once_with()

    def test_processes_input(self):
        list = ['ABC' , 'ABC\n' , 'A B C\n\r']
        
        self.assertEqual(File().process_input(list) , ['abc' , 'abc' , 'a b c'])
