import unittest
def num_balance(n: int) -> str:
    half_length = 0
    if n > 0: 
        if len(str(n)) % 2 == 0:
            half_length = int(len(str(n)) / 2)
            sum_first_path = sum(int(digit) for digit in str(n)[:half_length])
            sum_second_path = sum(int(digit) for digit in str(n)[half_length:])
            if sum_first_path == sum_second_path:
                return 'число сбалансировано'
            return 'число не сбалансировано'
        else:
            half_length = int((len(str(n))) / 2)
            sum_first_path = sum(int(digit) for digit in str(n)[:half_length+1])
            sum_second_path = sum(int(digit) for digit in str(n)[half_length:])
            if sum_first_path == sum_second_path:
                return 'число сбалансировано'
            return 'число не сбалансировано'
    

print(num_balance(12341234))
print(num_balance(3335333))
print(num_balance(4756447564))
print(num_balance(123456))

class Test(unittest.TestCase):
    def test_num_balance(self):
        self.assertEqual(num_balance(12341234), 'число сбалансировано')
        self.assertEqual(num_balance(33533), 'число сбалансировано')
        self.assertEqual(num_balance(4756447564), 'число сбалансировано')
    
    def test_num_not_balance(self):
        self.assertEqual(num_balance(123456), 'число не сбалансировано')
        self.assertEqual(num_balance(1231232), 'число не сбалансировано')

if __name__ == '__main__':
    unittest.main()