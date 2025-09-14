#Get rid of the duplictaes!!

student_data = {'std1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'std2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'std3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'std4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)