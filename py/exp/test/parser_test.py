from exp import *
from antlrparser.parser import *
from handcoded.parser import *

class BaseParserTest:

    def test_simple_minus__accpetance_test_1(self): 
        assert ['PUSH 3', 
                'PUSH 2', 
                'SUB'] == instructions_for("3-2",self.parser)
    
    def test_simple_div__accpetance_test_2(self):
        assert ['PUSH 1', 
                'PUSH 5', 
                'DIV'] == instructions_for("1/5",self.parser)
    
    def test_braces_precedence__accpetance_test_3(self):
        assert ['PUSH 5',
		'PUSH 2',
		'SUB',
		'PUSH 3',
		'MUL',
		'PUSH 7',
		'ADD',
		'PUSH 4',
		'MUL'] == instructions_for("((5-2)*3+7)*4",self.parser)
    
    def test_braces_precedence1__accpetance_test_4(self):
        assert ['PUSH 1',
		'PUSH 2',
		'PUSH 3',
		'SUB',
		'PUSH 9',
		'MUL',
		'SUB',
		'PUSH 2',
		'DIV'] == instructions_for("(1-(2-3)*9)/2",self.parser)

    def test_braces_with_same_operator__accpetance_test_5(self):
        assert ['PUSH 9',
		'PUSH 8',
		'PUSH 7',
		'PUSH 6',
		'PUSH 5',
		'SUB',
		'SUB',
		'SUB',
		'SUB'] == instructions_for("(9-(8-(7-(6-5))))",self.parser)
        
    
    def test_instrction_set_add_mult_braced_single_digits(self):
        assert '\n'.join(['PUSH 3',
			  'PUSH 4',
                          'ADD',
			  'PUSH 5',		
			  'MUL']) == instructions_str_for("(3+4)*5",self.parser)
	        
            
    

class TestAntlrParser (BaseParserTest):
    def setup_method(self,method):
        self.parser = AntlrParser()
    
    def test_instrction_set_add_mult(self):
        assert '\n'.join(['PUSH 23',
			  'PUSH 24',
			  'PUSH 25',		
			  'MUL',
			  'ADD']) == instructions_str_for("23+24*25",self.parser)
	        
    def test_instrction_set_add_mult_braced(self):
        assert '\n'.join(['PUSH 23',
			  'PUSH 24',
                          'ADD',
			  'PUSH 25',		
			  'MUL']) == instructions_str_for("(23+24)*25",self.parser)
    
    def test_instrction_set_div_sub(self):
        assert '\n'.join(['PUSH 23',
			  'PUSH 24',
                          'DIV',
			  'PUSH 25',		
			  'SUB']) == instructions_str_for("23/24-25",self.parser)
	        
    def test_instrction_set_div_sub_braced(self):
        assert '\n'.join(['PUSH 23',
			  'PUSH 24',                          
			  'PUSH 25',		
			  'SUB',
                          'DIV']) == instructions_str_for("23/(24-25)",self.parser)
	    
class TestHandCodedParser (BaseParserTest):
     def setup_method(self,method):
         self.parser = ShuntingYardParser()
