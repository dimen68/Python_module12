# Задача "Логирование бегунов"

import unittest
import logging
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                            format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_1 = Runner('Men1', -1)
            for i in range(10): Runner.walk(test_1)
            self.assertEqual(test_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc_1:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_2 = Runner(6, 10)
            for i in range(10): Runner.run(test_2)
            self.assertEqual(test_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc_2:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_3 = Runner('Men3')
        test_4 = Runner('Men4')
        for i in range(10): Runner.run(test_3)
        for i in range(10): Runner.walk(test_4)
        self.assertNotEqual(test_3.distance, test_4.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')
    unittest.main()
