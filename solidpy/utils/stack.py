def get_lines_from_file(filepath=None, culprit_lineno=0):

	pre_context, post_context, context_line = [], [], []
	file_contents = open(filepath).readlines()

	# The index starts from 0, so the actual lineno is -1
	actual_culprit_lineno = culprit_lineno-1
	actual_culprit_lineno = 0 if actual_culprit_lineno < 0 else actual_culprit_lineno


	pre_culprit_lines = actual_culprit_lineno-5
	pre_culprit_lines = 0 if pre_culprit_lines < 0 else pre_culprit_lines

	for i in range(pre_culprit_lines, actual_culprit_lineno):
		line = file_contents[i] if len(file_contents) > i else False
		if line is not False:
			pre_context.append((i+1, line))

	post_culprit_lines = actual_culprit_lineno+5
	post_culprit_index_start = actual_culprit_lineno+1

	for i in range(post_culprit_index_start, post_culprit_lines):
		line = file_contents[i] if len(file_contents) > i else False
		if line is not False:
			post_context.append((i+1, line))

	context_line_contents = file_contents[actual_culprit_lineno] if len(file_contents) > actual_culprit_lineno else False
	if context_line_contents is not False:
		context_line = (culprit_lineno, context_line_contents)
	
	context_dict = {
		'culprit_lineno': culprit_lineno,
		'filepath': filepath,
		'pre_context': pre_context,
		'context_line': context_line,
		'post_context': post_context,
	}


	return context_dict
 	