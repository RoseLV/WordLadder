import unittest
from word_ladder import *
# start = hit
# end = cog

class TestWL(unittest.TestCase):

    def test_same(self):
        self.assertEqual(same('hit','cog'), 0)
        self.assertEqual(same('hit','lot'), 1)
        self.assertEqual(same('hit','hot'), 2)
        self.assertEqual(same('hit','hit'), 3)
        #self.assertEqual(same('hide','hide'), 4)


    def test_build(self):
        # words = [hit,hot,dot,dog,lot,log,dof,mit,sit,sat,mog,mig,seg,nax,nax,cog]
        self.assertEqual(build('hit', words, {'hid': True}, ["hid"]), ["hit"])
        self.assertNotEqual(build('hit', words, {'hit': True}, ["hid"]), ["hid"])
        self.assertEqual(build('hit', words, {'hit': True, 'hot': True, 'sit': True, 'mit': True, 'lot': True, 'dot': True}, ["hid"]), [])
        self.assertEqual(build('hit', words, {'hid': True}, ["hit"]), [])
        #self.assertNotEqual(build('hide', words, {'ride': True}, ['size']), [])
        #self.assertEqual(build('hide', words, {'ride': True}, ['size']), ['hide'])
        #self.assertEqual(build('aaaaaaaaaaaaaaaaaaaaaaa', words, {'ride': True}, ['size']), [])
        #self.assertEqual(build('hide', [], {'ride': True}, ['size']), [])

    def test_find(self):
        #words = [hit, hot, dot, dog, lot, log, dof, mit, sit, sat, mog, mig, seg, nax, nax, cog]
        self.assertTrue(find('hit', words, seen, 'cog', ["hit", "hot", "lot", "log", "cog"]))
        self.assertFalse(find('hit', words, seen, 'cog', ["hit", "hot", "dot", "dog", "cog"]))
        self.assertFalse(find("hit", words, seen, "nax", []))
        # find return true case: self.assertTrue(find("hit", words, seen, 'cog', path))


if __name__ == '__main__':
    unittest.main()
 # start:hit end:hit pass
#start:hit end:cog pass