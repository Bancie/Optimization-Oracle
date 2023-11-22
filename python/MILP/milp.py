from scipy.optimize import linprog


obj = [-1, -2]

lhs_ineq = [[5,15/7], [-2.4,30/7]]
rhs_ineq = [20, 15]

bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="highs")

opt