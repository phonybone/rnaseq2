from Rnaseq.Step import *

class Header(Step):
    '''Header step'''
    
    def sh_script(self, context):
        input=context.inputs(self.name)
        return "header.sh_script nyi"

    def outputs(self, inputs):
        return inputs

#print "%s checking in" % __file__

