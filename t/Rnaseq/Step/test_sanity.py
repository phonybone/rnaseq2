import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir,'lib'))


from Rnaseq.Step.Bowtie import *
from Rnaseq.Step.Link import *
from Rnaseq.Step.Header import *

class TestSanity(unittest.TestCase):
    def test_link_outputs(self):
        btstep=Bowtie.Bowtie()
        self.assertEqual(btstep.__class__.__name__, 'Bowtie')

        lstep=Link.Link()
        self.assertEqual(lstep.__class__.__name__, 'Link')

        hstep=Header()
        self.assertEqual(hstep.__class__.__name__, 'Header')


suite = unittest.TestLoader().loadTestsFromTestCase(TestSanity)
unittest.TextTestRunner(verbosity=2).run(suite)
