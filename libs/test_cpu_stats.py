#!/usr/bin/env python

import unittest

# from . import cpu_stats
#No relative imports in non-packages

import cpu_stats
class TestCPUStats(unittest.TestCase):
    def setUp(self):
        self.sample_duration = .1 #secs

    def test_cpu_times(self):
        values = cpu_stats.cpu_times()
        self.assertTrue(len(values) >=7, values)

    def test_cpu_info(self):
        values = cpu_stats.cpu_times()
        self.assertTrue(len(values) > 0, values)


if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCPUStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
