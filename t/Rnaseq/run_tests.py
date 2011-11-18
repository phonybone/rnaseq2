import unittest, sys, os

dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../..")
sys.path.append(os.path.join(dir+'/lib'))

suite=unittest.TestLoader().discover('.',pattern='test*.py')
unittest.TextTestRunner(verbosity=2).run(suite)
