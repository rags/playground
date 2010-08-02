from composite import *

class TestCompositeCounter:    

    def words(self):
        return ["fooblahboobar","blahfoobar","foo","bar","blah","fooboobar",
                "boo","fooblah","barfoo","foobar","xfooybar","blahfo","blahblah","foobarfo",
                "nonfoobar","fooblahbar","fooblah","boobar","blabar","bl","b","barrr"]

    def test_simple(self):
        assert 1 == CompositeCounter(["foobar","foo","bar"],2).count()
        assert 0 == CompositeCounter(["foobar","foo","bar"],3).count()
        
    def test_count(self):
        assert 10 == CompositeCounter(self.words(),2).count()
        assert 4 == CompositeCounter(self.words(),3).count()
        assert 1 == CompositeCounter(self.words(),4).count()
        assert 0 == CompositeCounter(self.words(),5).count()
        assert 0 == CompositeCounter(self.words(),6).count()

    def test_file_read(self):
        file_words = read1("../sample.txt")
        print file_words
        assert 3561 == len(file_words)
        assert "a" == file_words[0]
        assert "aardvark" == file_words[1]
        assert "azures" == file_words[3560]
    
    def test_acceptance_file(self):
        assert 106 == count_composites(["../sample.txt",2])
        assert 3 == count_composites(["../sample.txt",3])
        assert 0 == count_composites(["../sample.txt",4])
