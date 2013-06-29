import sys
import unittest
import tempfile

from nose.tools import eq_
from solidpy.utils.stack import get_lines_from_file


class TestStack(unittest.TestCase):		

	def test_no_exceptions_raised(self):
		temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
		temp.writelines(["oh hello there\n", ])
		temp.seek(0)

		self.assertTrue(get_lines_from_file(temp.name, culprit_lineno=10))
		temp.close()


	def test_context(self):
		temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
		temp.writelines(["line 1\n", "line 2\n", "line 3\n", "line 4\n" ,"line 5\n" ])
		temp.seek(0)

		result =  get_lines_from_file(temp.name, culprit_lineno=4)

		eq_(result['context_line'], (4 ,"line 4\n"))
		eq_(result['pre_context'], [(1, 'line 1\n'), (2, 'line 2\n'), (3, 'line 3\n')])
		eq_(result['post_context'], [(5, 'line 5\n')])


		temp.close()


