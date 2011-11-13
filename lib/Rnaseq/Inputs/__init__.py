#-*-python-*-
import yaml, re

class Inputs(object):
    def __init__(self, **kwargs):
        if 'filename' in kwargs:
            # read file contents:
            f=open(kwargs['filename'])
            file_contents=f.read()
            f.close()

            if re.search('yml$', kwargs['filename']):
                yml=yaml.load(file_contents)
                self.files=re.split('[\s,]+',yml['input_files'])
                if 'paired_end' in yml: self.paired_end=yml['paired_end']
            else:
                raise Exception("unknown inputs file format")
            
