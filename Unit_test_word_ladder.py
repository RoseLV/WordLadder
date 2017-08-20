import unittest
from word_ladder import *

dict = ["hit", "hot", "dot", "dog", "lot", "log", "dof", "mit", "sit", "sat", "mog", "mig", "seg", "nax", "maz", "cog",  "abcd", "mnxyz"]

class TestWordLadder(unittest.TestCase):

    def setUp(self):
        pass

    def testSame(self):
        self.assertEqual(same('hit', 'cog'), 0)
        self.assertEqual(same('hit', 'lot'), 1)
        self.assertEqual(same('hit', 'hot'), 2)
        self.assertEqual(same('hit', 'hit'), 3)

    def testBuild(self):

        self.assertEqual(build('hit', dict, {'hid': True}, ["hid"]), ["hit"])
        self.assertEqual(build('hit', dict, {'ride': True}, ['size']), ['hit'])
        self.assertNotEqual(build('hit', dict, {'hit': True}, ["hid"]), ["hid"])
        self.assertEqual(build('hit', dict, {'hit': True, 'hot': True, 'sit': True, 'mit': True, 'lot': True, 'dot': True}, ["hid"]), [])
        self.assertEqual(build('hit', dict, {'hid': True}, ["hit"]), [])

    def testFind(self):

        self.assertTrue(find("hit", dict, {'hid': True}, "cog", ["hit", "hot", "lot", "log", "cog"]))
        self.assertTrue(find("hit", dict, {'hid': True}, "cog", ['hit', 'hot', 'dot', 'dog', 'cog']))
        self.assertTrue(find("hit", dict, {'hid': True}, "cog", ['hit', 'mit', 'mig', 'mog', 'cog']))
        self.assertFalse(find("hit", dict, {'hid': True}, "hit", ["hit", "hot", "lot"]))
        # find return true case: self.assertTrue(find("hit", words, seen, 'cog', path))

    def testStart(self):

        result = ["hit", "hot", "dot", "dog", "lot", "log", "dof", "mit", "sit", "sat", "mog", "mig", "seg","nax","maz", "cog"]
        self.assertEqual(start("hit", dict), ("hit", result))
        with self.assertRaises(ValueError):
            start("oval", dict)

    def test_target(self):

        self.assertEqual(target("cog", "hit", dict), "cog")
        with self.assertRaises(ValueError):
            target("job", "hit", dict)

    #def testFind_path(self):
        #self.assertEqual(find_path("hit","nax"), "No path found")


if __name__ == '__main__':
    unittest.main()