import unittest
from test_GantryAngle import TestFunctions

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestFunctions("test_import"), TestFunctions("test_gantry_angle"),
             TestFunctions("test_SSD"), TestFunctions("test_wedge"),
             TestFunctions("test_collimator"),
             TestFunctions("test_prescription_dose")]
    suite.addTests(tests)

    # command line output
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # output to txtfile
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
