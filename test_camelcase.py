import CamelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', CamelCase.camelcase('Hello World'))
        self.assertEqual('helloWorld', CamelCase.camelcase('Hello World'))
        self.assertEqual('', CamelCase.camelcase(''))
        self.assertEqual('hello', CamelCase.camelcase('Hello'))

        self.assertNotEqual('helloWorld', CamelCase.camelcase('h3ll0W0rld'))
        self.assertNotEqual('helloWorld', CamelCase.camelcase(''))
        self.assertNotEqual('helloWorld', CamelCase.camelcase('😀😁😂🤣😃'))
        self.assertNotEqual('helloWorld', CamelCase.camelcase('#hello-World#'))
        self.assertNotEqual('helloWorld', CamelCase.camelcase('\n Hello World \n'))
        

    
        


    
    
