
def get_lines_from_file(filepath=None, culprit_lineno=0):

	file_contents = open(filepath).readlines()

	# The index starts from 0, so the actual lineno is -1
	actual_culprit_lineno = culprit_lineno-1

	pre_culprit_lines = actual_culprit_lineno-5
	post_culprit_lines = actual_culprit_lineno+5

	pre_context = file_contents[pre_culprit_lines:actual_culprit_lineno]
	post_context = file_contents[actual_culprit_lineno:post_culprit_lines]
	context_line = file_contents[actual_culprit_lineno]

	context_dict = {
		'pre_context': pre_context,
		'context_line': context_line,
		'post_context': post_context,
	}


	return context_dict
 	