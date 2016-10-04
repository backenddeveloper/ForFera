import re

class File:

    def read(self , filename , open_function=open):
        try:
            file =  open_function(filename , 'r')
            return self.process_input(file.readlines())
        finally:
            file.close()

    def process_input(self , list):
        for index , word in enumerate(list):
            list[index] = re.sub(r'\W+$' , '' , word.lower())
        return list
