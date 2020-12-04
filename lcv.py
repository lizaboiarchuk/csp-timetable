from csp_init import *
csp = my_csp

counter = 0
var_domains = {}
degree_values = {}

#init empty assignment
def init_assignment_lcv(csp):
  global var_domains
  global counter
  counter = 0
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
    var_domains[var] = csp[DOMAINS].copy()
  return assignment


def getRoom(csp, assignment,var, value):
  rooms = data._rooms
  rooms.sort(key=lambda c: c[1])
  
  for r in rooms:
    if (r[1] >= var._number_of_students):
      free = True
      for k in csp[VARIABLES]:
        if (assignment[k] is not None):
          if (k._room == r and assignment[k] == value):
            free = False
      if free:
       return r



def is_in_domain(var,value):
  global var_domains
  for d in var_domains[var]:
    if (d == value):
      return True
  return False

def add_domains(assignment, csp, value):
  global var_domains
  j = value
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      if (not i==j):
        if (i._teacher == j._teacher):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._type_of_class == j._type_of_class):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._speciality == j._speciality and (i._type_of_class == "lecture") or (j._type_of_class == "lecture")):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None




def backtracking_lcv(assignment, csp, heuristic):
  global counter
  while True:
    if is_complete(assignment):
      return assignment
    for value in csp[DOMAINS]:
      var = heuristic(assignment)
      assignment[var] = value
      var._room = getRoom(csp,assignment, var, value)
      counter+=1
      if is_consistent(assignment, csp[CONSTRAINTS]):    
        break
      else: 
        assignment[var] = None
        var._room = None
  return FAILURE


def lcv_heuristic(assignment):
  teach = {}
  for i in csp[VARIABLES]:
    teach[i._teacher] = 0
  res = []
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      teach[i._teacher]+=1
      res.append(i)
  res.sort(key=lambda l: teach[l._teacher])
  return res[0]


def get_counter_lcv():
  global counter
  return counter



