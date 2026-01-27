import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse

def generate_score_graph(score_breakdown: dict):
    labels = score_breakdown.keys()
    values = score_breakdown.values()

    plt.figure()
    plt.bar(labels, values)
    plt.title("Visa Score Breakdown")
    plt.xlabel("Criteria")
    plt.ylabel("Points")
    plt.xticks(rotation=30)

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    return buffer

def calculate_visa_logic(
    age, education, aus_experience, overseas_exp,
    marital_status, english_test_type, english_test_score
):
    score = 0
    breakdown = {
        "Age": 0,
        "Education": 0,
        "Aus Experience": 0,
        "Overseas Experience": 0,
        "Language": 0,
        "Marital Status": 0
    }

    education = education.lower()
    english_test_type = english_test_type.lower()
    marital_status = marital_status.lower()

    # AGE
    if 18 <= age <= 24:
        breakdown["Age"] = 25
    elif 25 <= age <= 32:
        breakdown["Age"] = 30
    elif 33 <= age <= 39:
        breakdown["Age"] = 25
    elif 40 <= age <= 44:
        breakdown["Age"] = 15

    # OVERSEAS EXPERIENCE
    if 3 <= overseas_exp < 5:
        breakdown["Overseas Experience"] = 5
    elif 5 <= overseas_exp < 8:
        breakdown["Overseas Experience"] = 10
    elif overseas_exp >= 8:
        breakdown["Overseas Experience"] = 15

    # MARITAL STATUS
    if marital_status in ['single', 'partner_pr_or_citizen', 'partner_skilled']:
        breakdown["Marital Status"] = 10
    elif marital_status == 'partner_english_only':
        breakdown["Marital Status"] = 5

    # AUSTRALIAN EXPERIENCE
    if 1 <= aus_experience <= 2:
        breakdown["Aus Experience"] = 5
    elif 3 <= aus_experience <= 4:
        breakdown["Aus Experience"] = 10
    elif 5 <= aus_experience <= 7:
        breakdown["Aus Experience"] = 15
    elif aus_experience >= 8:
        breakdown["Aus Experience"] = 20

    # ENGLISH
    if english_test_type == 'ielts':
        if english_test_score in [7.0, 7.5]:
            breakdown["Language"] = 10
        elif english_test_score >= 8.0:
            breakdown["Language"] = 20

    elif english_test_type == 'pte':
        if 63 <= english_test_score <= 78:
            breakdown["Language"] = 10
        elif english_test_score >= 79:
            breakdown["Language"] = 20

    # EDUCATION
    if education in ['bachelor', 'masters']:
        breakdown["Education"] = 15
    elif education == 'doctorate':
        breakdown["Education"] = 20
    elif education == 'diploma':
        breakdown["Education"] = 10

    # TOTAL
    score = sum(breakdown.values())

    return score, breakdown