
from csp_init import *


mrv_domains = {}
counter = 0


#init empty assignment
def init_assignment_mrv(csp):
  global mrv_domains
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
    mrv_domains[var] = csp[DOMAINS].copy()
  return assignment

#mrv backtracking
def mrv_backtracking(assignment, csp):
  global counter
  global mrv_domains
  if is_complete(assignment):
    return assignment
  var = find_mrv(assignment,csp)
  for value in csp[DOMAINS]:
    if (is_in_domain(value, mrv_domains[var])):
      assignment[var] = value
      counter+=1
      add_to_mrv_domains(assignment,csp,var)
      if is_consistent(assignment, csp[CONSTRAINTS]):
        result = mrv_backtracking(assignment, csp)
        if result != FAILURE:
          return result
      assignment[var] = None
      undo(assignment,csp)
  return FAILURE


def undo(assignment, csp):
  global mrv_domains
  for var in csp[VARIABLES]:
    mrv_domains[var] = csp[DOMAINS].copy()
  for i in csp[VARIABLES]:
    for j in csp[VARIABLES]:
      if (assignment[j] is not None):
        if (not i==j):
          if (i._teacher == j._teacher):
            for k in range(len(mrv_domains[i])):
              if (mrv_domains[i][k] == assignment[j]):
                mrv_domains[i][k] = None
         


def is_in_domain(value, domain):
  for d in domain:
    if (d == value):
      return True
  return False


def add_to_mrv_domains(assignment, csp, value):
  global mrv_domains
  global prev_assignment
  j = value
  for i in csp[VARIABLES]:
    if (not i==j):
      if (i._teacher == j._teacher):
        for k in range(len(mrv_domains[i])):
          if (mrv_domains[i][k] == assignment[j]):
            mrv_domains[i][k] = None
    

def get_domains():
  global mrv_domains
  return mrv_domains


def domain_len(domain):
  res = 0
  for d in domain:
    if d is not None:
      res +=1
  return res


def find_mrv(assignment, csp):
  global mrv_domains
  min_val = select_unassigned_variable(csp[VARIABLES], assignment)
  min_domain = domain_len(mrv_domains[min_val])
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      if (domain_len(mrv_domains[i]) < min_domain):
        min_val = i
        min_domain = domain_len(mrv_domains[min_val])
  return min_val


def get_counter_mrv():
  global counter
  return counter

