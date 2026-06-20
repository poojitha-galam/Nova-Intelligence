import re
def parse_resume(resume_text):
    email_pattern = (
        r"[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}"
    )
    emails = re.findall(
        email_pattern,
        resume_text
    )
    return {
        "email":
        emails[0]
        if emails
        else "",
        "resume_text":
        resume_text
    }