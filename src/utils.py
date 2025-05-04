def is_integer(x, tol=1e-5):
    return abs(x - round(x)) < tol

def select_fractional_var(solution):
    """
    Selects a fractional variable that the value is closest to 0.5.
    Returns (index, value). If all variables are integer, returns (None, None).    
    """
    max_frac = 0.0
    selected_idx = None
    for idx, val in enumerate(solution):
        frac = abs(val - round(val))
        if 1e-5 < frac < 1 - 1e-5:  # Evita erros numéricos
            current_frac = min(val, 1 - val)
            if current_frac > max_frac:
                max_frac = current_frac
                selected_idx = idx
    return selected_idx, (solution[selected_idx] if selected_idx is not None else None)