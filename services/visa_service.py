def calculate_visa_logic(age, education, aus_experience, overseas_exp, language, marital_status):
    score = 0

    # AGE POINTS
    if 18 <= age <= 24:
        score += 25
    elif 25 <= age <= 32:
        score += 30
    elif 33 <= age <= 39:
        score += 25
    elif 40 <= age <= 44:
        score += 15

    # OVERSEAS EXPERIENCE
    if overseas_exp < 3:
        score += 0
    elif 3 <= overseas_exp < 5:
        score += 5
    elif 5 <= overseas_exp < 8:
        score += 10
    elif overseas_exp >= 8:
        score += 15

    # PARTNER / MARITAL STATUS
    if marital_status in ['single', 'partner_pr_or_citizen', 'partner_skilled']:
        score += 10
    elif marital_status == 'partner_english_only':
        score += 5

    # AUSTRALIAN EXPERIENCE
    if aus_experience < 1:
        score += 0
    elif 1 <= aus_experience <= 2:
        score += 5
    elif 3 <= aus_experience <= 4:
        score += 10
    elif 5 <= aus_experience <= 7:
        score += 15
    elif aus_experience >= 8:
        score += 20

    # ENGLISH LANGUAGE
    if language == 'competent':
        score += 0
    elif language == 'proficient':
        score += 10
    elif language == 'superior':
        score += 20

    # EDUCATION
    if education in ['bachelor', 'masters']:
        score += 15
    elif education == 'doctorate':
        score += 20
    elif education == 'diploma':
        score += 10

    return score
