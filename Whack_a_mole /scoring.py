# -------------------------
# Scoring system
# -------------------------

def update_score(current_score, hit):
    """
    Update the score based on whether the mole was hit.
    hit: True if player hit the mole, False otherwise
    """
    if hit:
        current_score += 1
    else:
        current_score -= 1
    return current_score
