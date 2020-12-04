from data import *
data = Data()
classes = data._classes
meeting_times = data.get_domains()


DOMAINS = "DOMAINS"
VARIABLES = "VARIABLES"
CONSTRAINTS = "CONSTRAINTS"
FAILURE = "FAILURE"



def is_complete(assignment):
  return None not in (assignment.values())


def select_unassigned_variable(variables, assignment):
  for var in variables:
    if assignment[var] is None:
      return var  


def is_consistent(assignment, constraints):
  for constraint_violated in constraints:
    if constraint_violated(assignment):
      return False
  return True




def equal(a, b): return a is not None and b is not None and a == b

def get_var(assignment):
  arr = []
  for i in assignment.keys():
    newClass = i
    if assignment[i] is not None:
      arr.append(newClass)
  return arr


def same_teacher(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._teacher, j._teacher) and i!=j and assignment[i]==assignment[j]:
        return True
  return False









def same_spec(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._speciality._name, j._speciality._name) and i!=j and assignment[i]==assignment[j] and ((i._type_of_class == "lecture") or (j._type_of_class == "lecture")) :
        return True
  return False



def groups_conflict(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._type_of_class, j._type_of_class) and i!=j and assignment[i]==assignment[j] :
        return True
  return False



my_csp = {VARIABLES: classes,
          DOMAINS: meeting_times,
          CONSTRAINTS: [same_teacher, same_spec, groups_conflict]
          }