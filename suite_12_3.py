import unittest
import test_12_1
import test_12

my_test_suite = unittest.TestSuite()

my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_test_suite)