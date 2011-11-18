import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

from Rnaseq.Inputs import *
from Rnaseq.Pipeline import *

class TestSh(unittest.TestCase):
    def test_basic(self):
        pipeline_file=os.path.join(dir, 't', 'fixtures', 'pipelines', 'simple_bowtie_p.yml')
        pipeline=Pipeline(pipeline_file)
        inputs_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        paired1=Inputs.load(inputs_file)[0]

        sh=pipeline.sh_script(paired1)
        print sh
        
        
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestSh)
unittest.TextTestRunner(verbosity=2).run(suite)
