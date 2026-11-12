def average(scores):
    if not scores:
        raise ValueError("No scores given")
    return sum(scores) / len(scores)


def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"