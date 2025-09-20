student_data = {
	'id1': {'name': ['sara'], 'class': 'v', 'subject_integation': ['english', 'math', 'science']},
	'id2': {'name': ['david'], 'class': 'v', 'subject_integation': ['english', 'math', 'science']},
	'id3': {'name': ['sara'], 'class': 'v', 'subject_integation': ['english', 'math', 'science']},
	'id4': {'name': ['surya'], 'class': 'v', 'subject_integation': ['english', 'math', 'science']}
}
reasult = {}
for key,value in student_data.items():
	if value not in reasult.values():
		reasult[key] = value
print(reasult)