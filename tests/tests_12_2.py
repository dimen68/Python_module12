# задание по теме "Методы Юнит-тестирования"
import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            form_result = {}
            for place, runner in result.items():
                form_result[place] = runner.name
            print(form_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournaments_1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        result1 = tournament1.start()
        self.all_results[1] = result1
        self.assertLessEqual(min(self.runner1.speed, self.runner3.speed), tournament1.full_distance,
                             'Дистанция слишком мала для замеров')
        self.assertTrue(result1[max(result1.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournaments_2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        result2 = tournament2.start()
        self.all_results[2] = result2
        self.assertLessEqual(min(self.runner2.speed, self.runner3.speed), tournament2.full_distance,
                             'Дистанция слишком мала для замеров')
        self.assertTrue(result2[max(result2.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournaments_3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = tournament3.start()
        self.all_results[3] = result3
        self.assertLessEqual(min(self.runner1.speed, self.runner2.speed, self.runner3.speed), tournament3.full_distance,
                             'Дистанция слишком мала для замеров')
        self.assertTrue(result3[max(result3.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
