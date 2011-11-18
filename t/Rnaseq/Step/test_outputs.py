import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir,'lib'))


from Rnaseq.Step.link import *
from Rnaseq.Step.bowtie import *
from Rnaseq.Inputs import *

class TestOutputs(unittest.TestCase):

    def test_link_outputs(self):
        input_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        input=Inputs.load(input_file)[0]
        step=Link()
        
        outputs=step.outputs(input)
        self.assertEqual(len(outputs), 2)
        self.assertEqual(outputs[0], os.path.join(input.working_dir, input.files[0]))
        self.assertEqual(outputs[1], os.path.join(input.working_dir, input.files[1]))


    def test_paired_end_outputs(self):
        '''test removal of _[12] and change of extension'''
        input_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        input=Inputs.load(input_file)[0]
        step=Bowtie()

        outputs=step.outputs(input)
        self.assertEqual(len(outputs), 1)
        self.assertEqual(outputs[0], os.path.join(input.working_dir, 's_1.bowtie'))
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestOutputs)
unittest.TextTestRunner(verbosity=2).run(suite)
