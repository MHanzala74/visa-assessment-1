def calculate_visa_logic(age,education,aus_experience,language):
    score = 0
    if age >= 18 and age <=24:
        score = score + 25
    elif age >= 25 and age <= 32:
        score = score + 30
    elif age >= 33 and age <= 39:
        score = score + 25
    elif age >= 40 and age <= 44:
        score = score + 15

    if aus_experience == 1:
        score = score + 5
    elif aus_experience > 1 and aus_experience <= 4:
        score = score + 10
    elif aus_experience > 4 and aus_experience <= 7:
        score = score + 15
    elif aus_experience > 7:
        score = score + 20

    if language == 'competent':
        score = score + 0
    elif language == 'proficient':
        score = score + 10 
    elif language == 'superior':
        score = score + 20

    if education == 'bachelor':
        score = score + 15
    elif education == 'masters':
        score = score + 15
    elif education == 'doctorate':
        score = score + 20
    elif education == 'diploma':
        score = score + 10

    return score

