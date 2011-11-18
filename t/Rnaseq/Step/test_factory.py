import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir,'lib'))

from Rnaseq.Step import *

class TestFactory(unittest.TestCase):
    def test_factory(self):

        btstep=Step.factory('Bowtie', {});
        self.assertEqual(btstep.__class__.__name__, 'Bowtie')

        lstep=Step.factory('Link', {})
        self.assertEqual(lstep.__class__.__name__, 'Link')

        hstep=Step.factory('Header', {})
        self.assertEqual(hstep.__class__.__name__, 'Header')



suite = unittest.TestLoader().loadTestsFromTestCase(TestFactory)
unittest.TextTestRunner(verbosity=2).run(suite)
