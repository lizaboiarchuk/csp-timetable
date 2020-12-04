from csp_init import *
csp = my_csp

counter = 0
var_domains = {}
degree_values = {}

#init empty assignment
def init_assignment_default(csp):
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

#recursive backtracking
def backtracking(assignment, csp, heuristic):
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






def get_counter_default():
  global counter
  return counter



#simple search 
def default_heuristic(assignment):
  res = []
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      res.append(i)
  return res[0] 
