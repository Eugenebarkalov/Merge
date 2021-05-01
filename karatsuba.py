 def multiply(self, other):


  # helper function
    def split(largeInt, n):
     least = largeInt._least_significant_digits(n/2)
     most = largeInt._right_shift(n/2)
     if debug: assert least.to_int() + (most.to_int() << (LargeInt.base_bits*(n/2))) == largeInt.to_int()
     return least, most
  n = max(len(str(self)),len(str(other)))
  if (n==1):
     return self.to_int() * other.to_int()
  else:
     aR, aL = split(self,n)
     bR , bL = split(other, n)
     x1 = aL.multiply(bL)
     x2 =aR.multiply(bR)
     a = aL.add(bL)
     b = aR.add(bR)
     x3=a.multiply(b)
  # code for recursive step here
  #return 1 # change this line with your implementation
  return  x1 * 10**n + (x3-x1-x2) * 10**(n/2) + x2
