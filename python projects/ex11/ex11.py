import itertools


class Node:
	def __init__(self, data, positive_child=None, negative_child=None):
		self.data = data
		self.positive_child = positive_child
		self.negative_child = negative_child


class Record:
	def __init__(self, illness, symptoms):
		self.illness = illness
		self.symptoms = symptoms
	
			
def parse_data(filepath):
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.strip().split()
			records.append(Record(words[0], words[1:]))
		return records
		
		
class Diagnoser:
	def __init__(self, root: Node):
		self.root = root

	def _diagnose_helper(self, symptoms, cur_node):
		if not cur_node.negative_child and not cur_node.positive_child:
			return cur_node.data
		if cur_node.data in symptoms and cur_node.positive_child:
			return self._diagnose_helper(symptoms, cur_node.positive_child)
		elif cur_node.data not in symptoms and cur_node.negative_child:
			return self._diagnose_helper(symptoms, cur_node.negative_child)

	def diagnose(self, symptoms):
		return self._diagnose_helper(symptoms, self.root)
		
	def calculate_success_rate(self, records):
		if len(records) == 0:
			raise ValueError("records list is empty")
		success_counter = 0
		for record in records:
			if self.diagnose(record.symptoms) == record.illness:
				success_counter += 1
		return success_counter / len(records)

	def _all_illnesses_helper(self, cur_node, lst):
		if not cur_node.negative_child and not cur_node.positive_child:
			if cur_node.data is not None:
				lst.append(cur_node.data)
			return
		if cur_node.positive_child:
			self._all_illnesses_helper(cur_node.positive_child, lst)
		if cur_node.negative_child:
			self._all_illnesses_helper(cur_node.negative_child, lst)
		return lst

	def all_illnesses(self):
		non_sorted_illnesses = self._all_illnesses_helper(self.root, [])
		illnesses_dict = {}
		for illness in set(non_sorted_illnesses):
			key = non_sorted_illnesses.count(illness)
			if key in illnesses_dict.keys():
				illnesses_dict[key].append(illness)
			else:
				illnesses_dict[key] = [illness]
		sorted_illness = []
		for num in sorted(illnesses_dict, reverse=True):
			sorted_illness += illnesses_dict[num]
		return sorted_illness

	def _paths_to_illness_helper(self, cur_node, illness, true_false_lst,
	                             paths_lst):
		if not cur_node.negative_child and not cur_node.positive_child:
			if cur_node.data == illness:
				paths_lst.append(true_false_lst[:])
			return
		if cur_node.positive_child:
			true_false_lst.append(True)
			self._paths_to_illness_helper(cur_node.positive_child, illness,
				true_false_lst, paths_lst)
			true_false_lst.pop()
		if cur_node.negative_child:
			true_false_lst.append(False)
			self._paths_to_illness_helper(cur_node.negative_child, illness,
				true_false_lst, paths_lst)
			true_false_lst.pop()
		return paths_lst

	def paths_to_illness(self, illness):
		if illness in self.all_illnesses():
			self._paths_to_illness_helper(illness, self.root, [], [])
		else:
			return []

	def _minimize_helper_false(self, cur_node):
		negative_leaf, positive_leaf = None, None
		if not cur_node.negative_child and not cur_node.positive_child:
			return tuple([cur_node.data, cur_node.data])
		if cur_node.positive_child:
			positive_leaf = self._minimize_helper_false(
				cur_node.positive_child)[0]
		if cur_node.negative_child:
			negative_leaf = self._minimize_helper_false(
				cur_node.negative_child)[1]
		if negative_leaf == positive_leaf:
			self.root = self.root.positive_child

	def _minimize_helper_true(self, cur_node, lst):
		if not cur_node.negative_child and not cur_node.positive_child:
			lst.append(cur_node.data)
			return
		if cur_node.positive_child:
			self._all_illnesses_helper(cur_node.positive_child, lst)
		if cur_node.negative_child:
			self._all_illnesses_helper(cur_node.negative_child, lst)
		return set(lst)

	def minimize(self, remove_empty=False):
		if remove_empty is False:
			return self._minimize_helper_false(self.root)
		else:
			return self._minimize_helper_true(self.root)


def sort_list_by_frequency(non_sorted_lst):
	item_frequency_dict = {}
	for item in set(non_sorted_lst):
		item_frequency_dict[non_sorted_lst.count(item)] = item
	return item_frequency_dict[max(item_frequency_dict)]


def _find_leaf_data(records, symptoms_lst, non_symptoms_lst):
	symptoms_contestants = []
	contestants_fail = False
	for record in records:
		for symptom in symptoms_lst:
			if symptom not in record.symptoms:
				contestants_fail = True
				break
		if not contestants_fail:
			for non_symptom in non_symptoms_lst:
				if non_symptom in record.symptoms:
					contestants_fail = True
					break
		if not contestants_fail:
			symptoms_contestants.append(record.illness)
		contestants_fail = False
	return sort_list_by_frequency(symptoms_contestants)


def _illnesses_placer(cur_node, records, symptoms_lst, non_symptoms_lst):
	if not cur_node.negative_child and not cur_node.positive_child:
		child_data = _find_leaf_data(records, symptoms_lst[:],
			non_symptoms_lst[:])
		cur_node.data = child_data
		return
	symptoms_lst.append(cur_node.data)
	_illnesses_placer(cur_node.positive_child, records, symptoms_lst,
		non_symptoms_lst)
	symptoms_lst.pop()
	non_symptoms_lst.append(cur_node.data)
	_illnesses_placer(cur_node.negative_child, records, symptoms_lst,
		non_symptoms_lst)
	non_symptoms_lst.pop()


def build_tree(records, symptoms):
	_symptoms = symptoms[::-1]
	symptoms_dict = {}
	for num, symptom in enumerate(_symptoms):
		symptom_node = None
		if num == 0:
			symptom_node = Node(symptom, Node("?"), Node("?"))
		else:
			symptom_node = Node(symptom, symptoms_dict[num - 1], symptoms_dict[
				num - 1])
		symptoms_dict[num] = symptom_node
	_root = symptoms_dict[max(symptoms_dict)]
	_illnesses_placer(_root, records, [], [])
	return Diagnoser(_root)


def optimal_tree(records, symptoms, depth):
	if 0 <= depth <= len(symptoms) or list(set(symptoms)) != symptoms:
		raise ValueError("depth's size doesn't fit or duplicate symptom/s ")
	for symptom in symptoms:
		if type(symptom) is not str:
			raise TypeError("every symptoms has to be str type")
	for record in records:
		if type(record) is not Record:
			raise TypeError("every record has to be Record type")
	if depth == 0:
		return Diagnoser(Node(None))
	trees_dict = {}
	for combination in itertools.combinations(symptoms, depth):
		tree = build_tree(records, combination)
		trees_dict[tree.calculate_success_rate(records)] = tree
	return trees_dict[max(trees_dict)]



if __name__ == "__main__":
	
	# Manually build a simple tree.
	#                cough
	#          Yes /       \ No
	#        fever           healthy
	#   Yes /     \ No
	# covid-19   cold
	
	flu_leaf = Node("covid-19", None, None)
	cold_leaf = Node("cold", None, None)
	inner_vertex = Node("fever", flu_leaf, cold_leaf)
	healthy_leaf = Node("healthy", None, None)
	root = Node("cough", inner_vertex, healthy_leaf)
	
	diagnoser = Diagnoser(root)
	
	# Simple test
	diagnosis = diagnoser.diagnose(["cough"])
	if diagnosis == "cold":
		print("Test passed")
	else:
		print("Test failed. Should have printed cold, printed: ", diagnosis)

	print(diagnoser.all_illnesses())
		
	# Add more tests for sections 2-7 here.


