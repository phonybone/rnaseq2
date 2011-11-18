import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

import Rnaseq.Globals

class TestInit(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Rnaseq.Globals.get('rnaseq_dir'), dir)

suite = unittest.TestLoader().loadTestsFromTestCase(TestInit)
unittest.TextTestRunner(verbosity=2).run(suite)
