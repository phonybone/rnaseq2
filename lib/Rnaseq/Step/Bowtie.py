import os, re
from Rnaseq.Step import *

class Bowtie(Step):
    '''bowtie'''


    def sh_script(self, context):
        input=context.inputs(self.name)
        if input.paired_end:
            ins="-1 %s -2 %s" % (input.files[0], input.files[1])
        else:
            ins=input.files[0]
    

        # set input format flag based on .ext of first input file
        ext=re.split('\.',input.files[0])[-1] # take the item after the last '.'
        try:
            iff={'fq'   :'-q',  # hash/dict literal...
                 'fastq':'-q',
                 'fa'   :'-f',
                 'fasta':'-f',
                 }[ext]         # ...indexed here
        except KeyError as e:
            iff='-r'            # raw format


        output=self.outputs(input)[0]

        try: off=self.output_format
        except AttributeError: off=''

        try: off=self.args
        except AttributeError: args=''

        cmd="bowtie %(ins)s %(iff)s %(off)s %(args)s > %(out)s" \
            % {'ins': ins, 'out': output, 'iff': iff, 'off': off, 'args': args}

        return cmd
        

    def outputs(self, input):
        i0=input.files[0]
        if input.paired_end:
            # remove _1 or _2, and change .ext to '.bowtie'
            mg=re.search('(.*)_[12](.*)', i0)
            i0='%s.bowtie' % (mg.group(1))
        else:
            i0=re.sub('\.\w+$', '.bowtie')
        return [os.path.join(input.working_dir, i0)]

#print "%s checking in" % __file__
