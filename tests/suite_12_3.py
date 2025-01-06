#  TestSuit

import unittest
import tests_12_1
import tests_12_2

run_tour_ST = unittest.TestSuite()
run_tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
run_tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_ST)
