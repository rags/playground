require 'runit/testcase'
require '../coordinate'
class TestCoordinate < Test::Unit::TestCase
def test_x
coord = Coordinate.new(2,3)
assert_equal(2,coord.x,"oops!")
end

def test_y
coord = Coordinate.new(2,3)
assert_equal(3,coord.y,"oops!")
end

def test_y=
coord = Coordinate.new()
assert_equal(0,coord.y,"oops!")
end


end

if $0 == __FILE__
  require 'runit/cui/testrunner'  
  RUNIT::CUI::TestRunner.run(TestCoordinate.suite)
end