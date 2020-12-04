from csp_init import *
from csp import *
csp = my_csp

counter = 0
degree_values = [[]]

#init empty assignment
def init_assignment_degree(csp):
  global degree_values
  global counter
  counter = 0
  assignment = {}
  j = 0
  for var in csp[VARIABLES]:
    assignment[var] = None
    degree_values.append([var,0])
    j+=1
  init_degree_values(csp)  
  return assignment

def init_degree_values(csp):
  global degree_values
  l = 0
  for i in csp[VARIABLES]:
    degree = 0
    for j in csp[VARIABLES]:
      if (i!=j):
        if (i._teacher == j._teacher):
          degree+=1
        if (i._type_of_class == j._type_of_class and i._speciality == j._speciality):
          degree+=1
        if (i._speciality == j._speciality and (i._type_of_class == "lecture")  and j._type_of_class != "lecture"):
          degree+=1
    degree_values[l] = [i,degree]
    l+=1

#recursive backtracking
def degree_backtracking(assignment, csp):
  global degree_values
  global counter
  while True:
    if is_complete(assignment):
      return assignment
    for value in csp[DOMAINS]:
      var = choose_value(assignment,csp)
      assignment[var] = value
      update_values(assignment,csp)
      var._room = getRoom(csp,assignment, var, value)
      counter+=1
      if is_consistent(assignment, csp[CONSTRAINTS]):    
        break
      else: 
        assignment[var] = None
        var._room = None
        update_values(assignment,csp)
  return FAILURE

def choose_value(assignment, csp):
  global degree_values
  degree_values.sort(key=lambda l:l[1], reverse=False)
  for i in degree_values:
    if assignment[i[0]] is None:
      return i[0]

def update_values(assignment, csp):
  global degree_values
  l = 0
  for i in csp[VARIABLES]:
    degree = 0
    for j in csp[VARIABLES]:
      if (assignment[j] is None):
        if (i!=j):
          if (i._teacher == j._teacher):
            degree+=1
          if (i._type_of_class == j._type_of_class and i._speciality == j._speciality):
            degree+=1
          if (i._speciality == j._speciality and (i._type_of_class == "lecture") and j._type_of_class != "lecture"):
            degree+=1
    degree_values[l] = [i,degree]
    l+=1


def get_counter_degree():
  global counter
  return counter



