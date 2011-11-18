import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))


from Rnaseq.Inputs import *
from Rnaseq.Context import *
from Rnaseq.Step.bowtie import *
import Rnaseq.Globals

class TestBowtie(unittest.TestCase):
    def test_bowtie(self):
        input_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        input=Inputs.load(input_file)[0]
        step=Bowtie()
        s=step.sh_script(Context(input=input))

        bowtie_inputs='-1 %s -2 %s' % (input.files[0], input.files[1])
        self.assertTrue(s.index(bowtie_inputs) > 0)
        self.assertTrue(s.index(' -q ') > 0)

        bowtie_outputs='> %s' % step.outputs(input)[0]
        self.assertTrue(s.index(bowtie_outputs) > 0)



suite = unittest.TestLoader().loadTestsFromTestCase(TestBowtie)
unittest.TextTestRunner(verbosity=2).run(suite)
