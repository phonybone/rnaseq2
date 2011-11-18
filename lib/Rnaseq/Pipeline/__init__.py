#-*-python-*-

import yaml, re
from Rnaseq.Context import *
from Rnaseq.Step import *

class Pipeline(object):
    required=['name', 'description', 'stepnames']
    
    def __init__(self, filename):
        self.filename=filename
        self.steps=[]
        self.load()

    def verify_required(self):
        missing=[]
        for attr in self.required:
            try: a=getattr(self, attr)
            except AttributeError: missing.append(attr)

        if len(missing)>0:
            raise Exception("missing attributes: %s" % ", ".join(missing))
                


    def load(self):
        '''
        reads the yaml file defining the pipeline.
        sets self.steps and self[stepname] for each step, and all other attrs.
        '''
        
        f=open(self.filename)
        yml=yaml.load(f)
        f.close()

        for (k,v) in yml.items():
            setattr(self, k, v)
        self.verify_required()

        for stepname in re.split('[\s,]+',self.stepnames):
            self.steps.append(Step.factory(stepname, yml[stepname]))


    def step_named(self, stepname):
        for s in self.steps:
            if s.name == stepname: return s
        return None


    def sh_script(self, inputs):
        context=self.make_context(inputs)
        sh=''
        for step in self.steps:
            sh+=step.sh_script(context)
        return sh


    def make_context(self, inputs):
        context=Context()
        for step in self.steps:
            pass
        return context
