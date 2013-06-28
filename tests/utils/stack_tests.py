import sys
sys.path.insert(0, '/home/martin/solid-python')

from nose.tools import eq_
import tempfile

from solidpy.utils.stack import get_lines_from_file

temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
temp.writelines(["oh hello there\n", ])
temp.seek(0)

eq_(get_lines_from_file(temp.name, culprit_lineno=4), 1)

