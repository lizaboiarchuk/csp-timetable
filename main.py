from csp_init import *
import prettytable
from csp import *
from degree_heuristic import *
from lcv import *
from mrv import *
from forward_checking import *
from constraint_propagation import *







result_default = backtracking(init_assignment_default(my_csp), my_csp, default_heuristic)
#print("Counter for default backtracking: " + str(get_counter_default()))

result_lcv = backtracking_lcv(init_assignment_lcv(my_csp), my_csp, lcv_heuristic)
print("Counter for backtracking with LCV: " + str(get_counter_lcv()))


result_mrv = mrv_backtracking(init_assignment_mrv(my_csp),my_csp)
print("Counter for backtracking with MRV: " + str(get_counter_mrv()))



result_degree = degree_backtracking(init_assignment_degree(my_csp), my_csp)
print("Counter for backtracking with Degree Heuristic: " + str(get_counter_degree()))


result_forward_check = forward_checking(init_assignment_forw(my_csp), my_csp)
print("Counter for backtracking with Forward Checking: " + str(get_counter_forw()))


result_constraint_propagation = constraint_propagation(init_assignment_con(my_csp), my_csp)
print("Counter for backtracking with Constraint Propagation: " + str(get_counter_con()))


result = result_constraint_propagation


monday, tuesday, wednesday, thursday, friday = [], [], [], [], []
days = [monday, tuesday, wednesday, thursday, friday]
for i in result.keys():
    if result[i] < 6:
        monday.append((i,result[i]))
    elif result[i] < 12 and result[i]>=6:
        tuesday.append((i,result[i]-6))
    elif result[i] < 18 and result[i]>=12:
        wednesday.append((i,result[i] - 12))
    elif result[i] < 24 and result[i]>=18:
        thursday.append((i, result[i] - 18))
    elif result[i] >= 24:
        friday.append((i, result[i] - 24))


def print_day(day,l):
	r = ""
	for d,n in day:
		if (l == n):
			r += str(d) + "\n" 
	return r


table = prettytable.PrettyTable(['Lesson Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
k = 0
for i in range(len(MEETING_TIMES)):
    table.add_row([MEETING_TIMES[i], print_day(monday,k), print_day(tuesday,k), print_day(wednesday,k), print_day(thursday,k), print_day(friday,k)])
    k+=1
print(table)
	



