from Rnaseq.Step import *

class Footer(Step):
    '''Footer step'''
    
    def sh_script(self, context):
        input=context.inputs(self.name)
        return "footer.sh_script nyi"

    def outputs(self, inputs):
        return inputs

#print "%s checking in" % __file__
