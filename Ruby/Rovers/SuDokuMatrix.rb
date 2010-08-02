class SuDoKuMatrix
		
	def initialize(block_size=3)
		@blockSize = block_size
		@matrixSize = block_size * block_size
		@cells={}		
	end
	
	def [](x,y)
		@cells[[x,y]]
	end
	
	def []=(x,y,value)
		@cells[[x,y]]=value
	end
end

x=SuDoKuMatrix.new(5)
x[0,0] = "boo"
print x[0,0]