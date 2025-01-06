# Задача "Проверка на выносливость"

import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_1 = runner.Runner('Men1')
        for i in range(10): runner.Runner.walk(test_1)
        self.assertEqual(test_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_2 = runner.Runner('Men2')
        for i in range(10): runner.Runner.run(test_2)
        self.assertEqual(test_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_3 = runner.Runner('Men3')
        test_4 = runner.Runner('Men4')
        for i in range(10): runner.Runner.run(test_3)
        for i in range(10): runner.Runner.walk(test_4)
        self.assertNotEqual(test_3.distance, test_4.distance)


if __name__ == '__main__':
    unittest.main()
