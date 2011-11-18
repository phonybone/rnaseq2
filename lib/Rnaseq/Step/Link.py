import os
from Rnaseq.Step import *

class Link(Step):
    '''link the inputs to the working directory'''

    def sh_script(self, context):
        input=context.step(self.name).inputs
        assert input.working_dir
        script=[]
        for f in input.files:
            script.append("ln -fs %s %s" % (f, input.working_dir))
        return "\n".join(script)

    def outputs(self, input):
        l=[os.path.join(input.working_dir, x) for x in input.files]
        return l


#print "%s checking in" % __file__
