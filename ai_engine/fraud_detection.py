def detect_resume_fraud(
    candidate
):
    fraud_score = 0
    skills = candidate.get(
        "skills",
        []
    )
    projects = candidate.get(
        "projects",
        []
    )
    experience = candidate.get(
        "experience",
        0
    )
    if (
        len(skills) > 20
        and
        len(projects) < 2
    ):
        fraud_score += 0.4
    if (
        experience > 15
        and
        len(projects) == 0
    ):
        fraud_score += 0.4
    if fraud_score > 0.5:
        return {
            "flagged": True,
            "fraud_score":
            fraud_score
        }
    return {
        "flagged": False,
        "fraud_score":
        fraud_score
    }