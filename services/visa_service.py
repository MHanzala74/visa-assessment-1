def calculate_visa_logic(age, education_level, aus_experience, overseas_exp, marital_status,english_test_type,english_test_score):
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
    if english_test_type == 'ielts':
        if english_test_score in [6.0, 6.5]:
            score += 0          
        elif english_test_score in [7.0, 7.5]:
            score += 10         
        elif english_test_score >= 8.0:
            score += 20         
    elif english_test_type == 'pte':
        if 52 <= english_test_score <= 58:
            score += 0          
        elif 63 <= english_test_score <= 78:
            score += 10         
        elif 79 <= english_test_score <= 85:
            score += 20         

    # EDUCATION
    if education_level in ['bachelor', 'masters']:
        score += 15
    elif education_level == 'doctorate':
        score += 20
    elif education_level == 'diploma':
        score += 10

    return score
