import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import unittest

from foxai.tools import logger

class TestLoggingCreation(unittest.TestCase):

    def test_incorrect_name(self):
        empty_name = logger.create_logger('', 0)
        self.assertEqual(empty_name, None)

        none_name = logger.create_logger(None, 0)
        self.assertEqual(none_name, None)
    
    def test_incorrect_log_level(self):
        wrong_type_level = logger.create_logger(__name__, 'foo')
        self.assertEqual(wrong_type_level, None)

        impossible_level_negative = logger.create_logger(__name__, -4)
        self.assertEqual(impossible_level_negative, None)

        impossible_level_too_high = logger.create_logger(__name__, 51)
        self.assertEqual(impossible_level_too_high, None)

        impossible_level_in_between = logger.create_logger(__name__, 35)
        self.assertEqual(impossible_level_in_between, None)
    
    def test_correct_logger(self):
        correct_logger = logger.create_logger(__name__, 20)
        correct_logger.info('Looking good')
        self.assertEqual(isinstance(correct_logger, logger.logging.Logger), True)

if __name__ == '__main__':
    unittest.main()