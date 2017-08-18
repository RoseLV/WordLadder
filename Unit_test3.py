import unittest
import word_ladder

class TestWL(unittest.TestCase):
    def test_samefun(self):
        self.assertEqual(same('hide','seek'), 0)
        self.assertEqual(same('lead','gold'), 1)
        self.assertEqual(same('load','gold'), 2)
        self.assertEqual(same('site','side'), 3)
        self.assertEqual(same('hide','hide'), 4)
    def test_buildfun(self):
        self.assertEqual(build('.oad', ['load','coad','hide'], {'load': False, 'coad': True, 'hide': False}, []),['load'] )
    def test_sfindfun(self):
        self.assert(sfind('lead', ['lead','coad','hide'], {'lead': False, 'coad': True, 'hide': False}, 'load', ['lead']), True)


if __name__ == '__main__':
    unittest.main()
