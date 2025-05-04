import mip
import math
from .utils import select_fractional_var

# Parte 1
def solve_lp(instance, extra_constraints=None, verbose=False, best_obj=-math.inf):
    """
    Solves the LP relaxation of the given problem.
    Returns the solution and the objective value.
    """

    n, m, obj_coef, constraints = instance.get_instance()

    model = mip.Model(sense=mip.MAXIMIZE, solver_name=mip.CBC)

    model.verbose = False

    x = [model.add_var(var_type=mip.CONTINUOUS, name=f"x{i}", lb=0, ub=1) for i in range(n)]

    # set the constraints
    for a,b in constraints:
        model.add_constr(mip.xsum(a[j] * x[j] for j in range(n)) <= b)
    
    # set extra constraints if any
    if extra_constraints:
        for idx, val in extra_constraints.items():
            x[idx].lb = val
            x[idx].ub = val
    
    model.cutoff = best_obj # for maximization, we can set a cutoff value to prune the search space
    
    model.objective = mip.xsum(obj_coef[j] * x[j] for j in range(n))

    status = model.optimize()

    if status in [mip.OptimizationStatus.OPTIMAL, mip.OptimizationStatus.FEASIBLE]:
        return [var.x for var in x], model.objective_value
    else:
        return None, None
    
# Parte 2
def branch_and_bound(instance, extra_constraints=None, verbose=False, best_solution=None, best_obj=-math.inf):
    """
    Solves the given problem using branch and bound.
    Returns the solution and the objective value.
    """

    # solve the LP relaxation first
    solution, obj_val = solve_lp(instance, extra_constraints, verbose, best_obj)

    # se for inviável ou não melhorou a solução, retorna a melhor solução encontrada
    # não faz sentido continuar a busca nesse nó
    if solution is None or obj_val is None or obj_val <= best_obj:
        return best_solution, best_obj
    
    # se for uma solução inteira, atualiza a melhor solução e não continua a busca
    frac_idx, _ = select_fractional_var(solution)
    if frac_idx is None:
        if obj_val > best_obj:
            return solution.copy(), obj_val
        else:
            return best_solution, best_obj
    
    new_constr = extra_constraints.copy() if extra_constraints else {}

    # left branch (fixes the fractional variable to 1)
    new_constr_left = new_constr.copy()
    new_constr_left[frac_idx] = 1
    best_solution, best_obj = branch_and_bound(instance, new_constr_left, verbose, best_solution, best_obj)

    # right branch (fixes the fractional variable to 0)
    new_constr_right = new_constr.copy()
    new_constr_right[frac_idx] = 0
    best_solution, best_obj = branch_and_bound(instance, new_constr_right, verbose, best_solution, best_obj)

    return best_solution, best_obj

# Parte 3 - Alternativa BFS
def bfs_bnb(instance):
    from collections import deque
    best_obj = -math.inf
    best_solution = None
    queue = deque([{}])  # Inicia com restrições vazias (nó raiz)

    while queue:
        extra_constraints = queue.popleft()  # FIFO = BFS
        solution, obj_val = solve_lp(instance, extra_constraints)

        if solution is None or obj_val <= best_obj:
            continue

        frac_idx, _ = select_fractional_var(solution)
        if frac_idx is None:
            best_solution, best_obj = solution, obj_val
        else:
            # Adiciona os dois ramos à fila
            left = extra_constraints.copy()
            left[frac_idx] = 1
            queue.append(left)

            right = extra_constraints.copy()
            right[frac_idx] = 0
            queue.append(right)

    return best_solution, best_obj