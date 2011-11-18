import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

from Rnaseq.Inputs import *
import Rnaseq.Globals

class TestBasic(unittest.TestCase):

    def test_templates(self):
        filename=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        inputs=Inputs.load(filename)
        i1=inputs[0]
        self.assertEqual(i1.working_dir, os.path.join(dir, 't', 'fixtures', 'working_dir'))
        self.assertEqual(i1.data_dir, os.path.join(dir, 't', 'fixtures', 'data'))


suite = unittest.TestLoader().loadTestsFromTestCase(TestBasic)
unittest.TextTestRunner(verbosity=2).run(suite)
