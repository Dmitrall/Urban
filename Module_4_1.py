import fake_math as fake
import true_math as true
result1 = fake.fake_divide(69,3)
result2 = fake.fake_divide(3, 0)
result3 = true.true_divide(49, 7)
result4 = true.true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

# Во втором варианте код проще и короче
#from fake_math import *
#from true_math import *
#result1 = fake_divide(69, 3)
#result2 = fake_divide(3, 0)
#result3 = true_divide(49, 7)
#result4 = true_divide(15, 0)
#print(result1)
#print(result2)
#print(result3)
#print(result4)