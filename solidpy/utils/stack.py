def get_lines_from_file(filepath=None, culprit_lineno=0):

	file_contents = open(filepath).readlines()

	# The index starts from 0, so the actual lineno is -1
	actual_culprit_lineno = culprit_lineno-1
	actual_culprit_lineno = 0 if actual_culprit_lineno < 0 else actual_culprit_lineno


	pre_culprit_lines = actual_culprit_lineno-5
	pre_culprit_lines = 0 if pre_culprit_lines < 0 else pre_culprit_lines

	post_culprit_lines = actual_culprit_lineno+5


	pre_context, post_context, context_line = {}, {}, {}

	# for i in range(pre_culprit_lines, actual_culprit_lineno):
	# 	print i
	# 	print file_contents

	pre_context = file_contents[pre_culprit_lines:actual_culprit_lineno]
	post_context = file_contents[actual_culprit_lineno+1:post_culprit_lines]
	context_line = file_contents[actual_culprit_lineno]

	context_dict = {
		'culprit_lineno': culprit_lineno,
		'filepath': filepath,
		'pre_context': pre_context,
		'context_line': context_line,
		'post_context': post_context,
	}


	return context_dict
 	