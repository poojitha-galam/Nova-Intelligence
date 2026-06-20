import re
def extract_requirements(jd_text):
    skills = []
    common_skills = [
        "Python",
        "Java",
        "SQL",
        "MongoDB",
        "React",
        "Node.js",
        "AWS",
        "Docker",
        "Kubernetes",
        "Machine Learning"
    ]
    for skill in common_skills:
        if skill.lower() in jd_text.lower():
            skills.append(skill)
    experience_match = re.search(
        r"(\d+)\+?\s*years",
        jd_text.lower()
    )
    experience = (
        experience_match.group(1)
        if experience_match
        else "Not Specified"
    )
    return {
        "skills": skills,
        "experience": experience,
        "raw_text": jd_text
    }