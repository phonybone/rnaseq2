import unittest, sys, os
dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
sys.path.append(os.path.join(dir+'/lib'))


from Rnaseq.Inputs import *
from Rnaseq.Step.link import *
from Rnaseq.Context import *
import Rnaseq.Globals

class TestSh(unittest.TestCase):

    def test_basic(self):
        input_file=os.path.join(dir, 't', 'fixtures', 'data', 'paired1.yml')
        input=Inputs.load(input_file)[0]
        step=Link()
        s=step.sh_script(Context(input=input))

        lines=re.split(r'\n',s)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], ('ln -fs %s %s' % (input.files[0], input.working_dir)))
        self.assertEqual(lines[1], ('ln -fs %s %s' % (input.files[1], input.working_dir)))

suite = unittest.TestLoader().loadTestsFromTestCase(TestSh)
unittest.TextTestRunner(verbosity=2).run(suite)
