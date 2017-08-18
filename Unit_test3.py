import unittest
from word_ladder import *
#start = hit
#end = cog

class TestWL(unittest.TestCase):

    def test_same(self):
        self.assertEqual(same('hide','seek'), 0)
        self.assertEqual(same('lead','gold'), 1)
        self.assertEqual(same('load','gold'), 2)
        self.assertEqual(same('site','side'), 3)
        self.assertEqual(same('hide','hide'), 4)


    def test_build(self):


        self.assertEqual(build('hide', words, {'hide': True}, []), [])
        self.assertNotEqual(build('hide', words, {'ride': True}, ['size']), ['size'])
        self.assertNotEqual(build('hide', words, {'ride': True}, ['size']), [])
        self.assertEqual(build('hide', words, {'ride': True}, ['size']), ['hide'])
        self.assertEqual(build('aaaaaaaaaaaaaaaaaaaaaaa', words, {'ride': True}, ['size']), [])
        self.assertEqual(build('hide', [], {'ride': True}, ['size']), [])


    def test_find(self):
        self.assertFalse(find('hide', [], seen, target, path))
        self.assertTrue(find (start, words, seen, target, path))




if __name__ == '__main__':
    unittest.main()
