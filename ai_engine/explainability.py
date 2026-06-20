def generate_explanation(
    candidate
):
    score = candidate[
        "score"
    ]
    if score > 85:
        return (
            "Excellent Match: "
            "Strong alignment "
            "with job requirements."
        )
    elif score > 70:
        return (
            "Good Match: "
            "Most skills and "
            "experience aligned."
        )
    elif score > 50:
        return (
            "Moderate Match: "
            "Some missing skills."
        )
    return (
        "Low Match: "
        "Limited relevance."
    )