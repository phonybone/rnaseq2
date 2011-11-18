#-*-python-*-
import yaml, re
import Rnaseq.Globals

# An Input is an object that describes the input to a step, and 
# as such it can consist of more than one file (eg paired read files).

class Inputs(object):

    # return an array of Input objects init'd from a yaml file:
    # yaml file must consist of a number of hash objects, one level
    # deep, with appropriate fields.
    @classmethod
    def load(self,filename):
        '''load input objects from a yaml file'''

        f=open(filename)
        file_contents=f.read()
        f.close()
        yml=yaml.load(file_contents)

        inputs=[]
        for (label,h) in yml.items():
            h['label']=label
            inputs.append(Inputs(h).verify())
        return inputs

    def __init__(self, h):
        for (k,v) in h.items():
            if (type(v)==type('')):
                v=re.sub(r'\\%', '%', v) # replace any '\\%' with '%', since yaml doesn't like '%'
                v=v % Rnaseq.Globals.globals # and then do the string formatting
            setattr(self,k,v)

        self.files=re.split('[\s,]+', self.files)
        if 'paired_end' not in h:
            self.paired_end=False


    def verify(self):
        assert(self.label != None)
        assert(type(self.files)==type([]))
        return self
