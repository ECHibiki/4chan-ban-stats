resp = input('Type 1 to view desc, 2 to view asc: ')
if resp == '1':
	file = open('stats.txt', 'r')
	file_text_arr = file.read().split('\n')
	file_text_arr_proc = []
	text_input = "Board	-- Total Bans / Posts per day DESC\n\n"
	for text in file_text_arr:
		text = text.strip().replace('\t', '').replace('\r', '').replace('\n', '')
		file_text_arr_proc.append(text.split('--'))
	for indexA, text_groupA in enumerate(file_text_arr_proc):
		for indexB, text_groupB in enumerate(file_text_arr_proc):
			if float(text_groupB[1]) < float(text_groupA[1]) and indexB < indexA:
				current_group =  file_text_arr_proc[indexA]
				file_text_arr_proc[indexA] = file_text_arr_proc[indexB]
				file_text_arr_proc[indexB] = current_group
	for text_group in file_text_arr_proc:
		text_input = text_input + text_group[0] + '\t--\t' + text_group[1] + '\n'
	asc_file = open('stats-desc-bans.txt', 'w')
	asc_file.write(text_input)
	input(text_input)
elif resp == '2':
	file = open('stats.txt', 'r')
	file_text_arr = file.read().split('\n')
	file_text_arr_proc = []
	text_input = "Board	-- Total Bans / Posts per day ASC\n\n"
	for text in file_text_arr:
		text = text.strip().replace('\t', '').replace('\r', '').replace('\n', '')
		file_text_arr_proc.append(text.split('--'))
	for indexA, text_groupA in enumerate(file_text_arr_proc):
		for indexB, text_groupB in enumerate(file_text_arr_proc):
			if float(text_groupB[1]) > float(text_groupA[1]) and indexB < indexA:
				current_group =  file_text_arr_proc[indexA]
				file_text_arr_proc[indexA] = file_text_arr_proc[indexB]
				file_text_arr_proc[indexB] = current_group
	for text_group in file_text_arr_proc:
		text_input = text_input + text_group[0] + '\t--\t' + text_group[1] + '\n'
	asc_file = open('stats-asc-bans.txt', 'w')
	asc_file.write(text_input)
	input(text_input)