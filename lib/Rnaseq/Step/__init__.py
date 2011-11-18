#-*-python-*-

class Step(object):

    def inputs(self):
        raise Exception("%s: inputs() not implemented" % type(self))
    
    def sh_script(self):
        raise Exception("%s: sh_script() not implemented" % type(self))

    @classmethod
    def factory(self, stepname, args):
        
        try:
            modname='Rnaseq.Step.%s' % stepname
            mod=__import__(modname)
        except ImportError as ie:
            raise Exception("error loading step '%s': %s" % (modname, str(ie)))

        mod=getattr(mod, 'Step')        # get Rnaseq.Step module
        mod=getattr(mod, stepname)      # get Rnaseq.Step.stepname
        kls=getattr(mod, stepname)      # get class
        
        step=kls()
        return step
        

#print "%s checking in" % __file__
