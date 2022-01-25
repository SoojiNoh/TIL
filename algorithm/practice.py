def dict_list_sum(_dicts):
	return reduce(lambda acc, _next: acc['age']+_next['age'], _dicts)

_dicts = [{'name': 'kim', 'age': 12}, { 'name': 'lee', 'age': 4}]
print(dict_list_sum(_dicts))