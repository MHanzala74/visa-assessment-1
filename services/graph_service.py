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