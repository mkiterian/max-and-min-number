def find_max_min(a_list):
  if min(a_list) == max(a_list):
  	return [len(a_list)]
  else:
    return [min(a_list), max(a_list)]
