import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

from Rnaseq.Inputs import *

class TestBasic(unittest.TestCase):

    def test_paired1(self):
        filename=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        paired1_a=Inputs.load(filename)
        self.assertEqual(len(paired1_a), 1)
        paired1=paired1_a[0]
        self.assertEqual(paired1.label, 'paired1')
        self.assertEqual(paired1.files, ['s_1_1.fq','s_1_2.fq'])
        self.assertTrue(paired1.paired_end)
                    
    def test_pairedN(self):
        filename=os.path.join(dir, 't', 'fixtures', 'data', 'paired_multi.yml')
        pairedN=Inputs.load(filename)
        self.assertTrue(len(pairedN), 2)

        p1=pairedN[0]
        self.assertEqual(p1.label, 's_1')
        self.assertEqual(p1.files, ['s_1_1.fq','s_1_2.fq'])
        self.assertTrue(p1.paired_end)
        
        p2=pairedN[0]
        self.assertEqual(p2.label, 's_1')
        self.assertEqual(p2.files, ['s_1_1.fq','s_1_2.fq'])
        self.assertTrue(p2.paired_end)
        

    def test_missing_fields(self):
        print "test_missing_fields NYI"
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestBasic)
unittest.TextTestRunner(verbosity=2).run(suite)
