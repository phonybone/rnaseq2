import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))

from Rnaseq.Inputs import *
from Rnaseq.Pipeline import *

class TestLoad(unittest.TestCase):
    def test_load(self):
        pipeline_file=os.path.join(dir, 't', 'fixtures', 'pipelines', 'simple_bowtie_p.yml')
        pipeline=Pipeline(pipeline_file) # calls pipeline.load

        self.assertEqual(pipeline.name, 'simple_bowtie_t')
        self.assertEqual(pipeline.description, 'do alignments on paired end data using bowtie')
        self.assertEqual(pipeline.stepnames, 'Header Link Bowtie Footer')

        self.assertEqual(pipeline.Header, {'inputs' : 'inputs'})
        self.assertEqual(pipeline.Link, {'inputs': 'Header'})
        self.assertEqual(pipeline.Bowtie, {  'inputs' : 'Link',
                                             'index' : '/proj/hoodlab/share/programs/bowtie-indexes/hg19',
                                             'max_mismatches' : 1,
                                             'output_format' : 'sam',
                                             'args' : '-n -k 1'
                                             })
        self.assertEqual(pipeline.Footer, {'inputs': 'Bowtie'})


        steps=pipeline.steps
        self.assertEqual(type(steps), type([]))
        self.assertEqual(len(steps), 4)
        
        
        
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestLoad)
unittest.TextTestRunner(verbosity=2).run(suite)
