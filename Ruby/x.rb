square = proc { |i| i*i }

def meth1(&b)
  print b.call(9), "\n"
end

#meth1 { |i| i+i }

def meth2
  print yield(8), "\n"
end

meth2 { |i| i+i }
meth1 { |i| i+i }
meth2 &square

