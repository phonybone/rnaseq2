import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))
#print "sys.path is %s" % "\n".join(sys.path)

from Rnaseq.Inputs import *

class TestBasic(unittest.TestCase):
    def test_basic(self):
        paired1=Inputs(filename='paired1.yml')
        self.assertEqual(paired1.files, ['s_1_1.fq','s_1_2.fq'])
        self.assertTrue(paired1.paired_end)
                        
suite = unittest.TestLoader().loadTestsFromTestCase(TestBasic)
unittest.TextTestRunner(verbosity=2).run(suite)
