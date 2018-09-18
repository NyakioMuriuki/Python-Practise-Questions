import unittest
import triple_check


class testTripleCheck(unittest.TestCase):
    def test_for_type(self):
        with self.assertRaises(TypeError):
            triple_check.triple_check(['a','b','b'])

    def test_for_correct_output(self):
        self.assertEqual(triple_check.triple_check([1,1,2,2,2,1,3]), (3,))
        self.assertEqual(triple_check.triple_check([5,3,4,3,5,5,3]), (4,))
        self.assertEqual(triple_check.triple_check([5,3,4,3,5,5,3,4]), (4,4))







if __name__ == '__main__':
    unittest.main()