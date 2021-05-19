import unittest
from car_fueling import compute_min_number_of_refills


class CarFueling(unittest.TestCase):
    def test(self):
        for (d, m, stops, answer) in [
            (950, 400, [200, 375, 550, 750], 2),
            (10, 3, [1, 2, 5, 9], -1),
            (200, 250, [100, 150], 0),
            (200, 250, [100, 199], 0),
            (500, 200, [100, 200, 300, 400], 2),
            (607, 210, [175, 345, 360, 511, 590, 606], 3)
        ]:
            self.assertEqual(compute_min_number_of_refills(d, m, stops), answer)


if __name__ == '__main__':
    unittest.main()
