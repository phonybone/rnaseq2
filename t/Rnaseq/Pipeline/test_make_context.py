import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

from Rnaseq.Inputs import *
from Rnaseq.Pipeline import *

# why even have a context?
# why not just alter all the steps inside the pipeline, ie
# assertEqual(pipeline.step_named('Header').inputs, paired1.files) or
# assertEqual(pipeline.step_named('Bowtie').inputs, ['/literal/filename/goes/here', '/second/filename/etc'])

class TestContext(unittest.TestCase):
    def test_context(self):
        pipeline_file=os.path.join(dir, 't', 'fixtures', 'pipelines', 'simple_bowtie_p.yml')
        pipeline=Pipeline(pipeline_file) # calls pipeline.load

        inputs_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        paired1=Inputs.load(inputs_file)[0]

        context=pipeline.make_context(paired1)
        self.assertEqual(context.step('Header').inputs, paired1.files)
        self.assertEqual(context.step('Link').inputs, pipeline.step_named('Header').outputs())
        self.assertEqual(context.step('Bowtie').inputs, pipeline.step_named('Link').outputs())
        self.assertEqual(context.step('Footer').inputs, pipeline.step_named('Bowtie').outputs())

        
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestContext)
unittest.TextTestRunner(verbosity=2).run(suite)
