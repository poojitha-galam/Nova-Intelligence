class Candidate:
    def __init__(
        self,
        candidate_id,
        name,
        email,
        skills,
        experience,
        education,
        certifications,
        projects,
        summary
    ):
        self.candidate_id = candidate_id
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.education = education
        self.certifications = certifications
        self.projects = projects
        self.summary = summary
    def to_dict(self):
        return {
            "candidate_id":
            self.candidate_id,

            "name":
            self.name,

            "email":
            self.email,

            "skills":
            self.skills,

            "experience":
            self.experience,

            "education":
            self.education,

            "certifications":
            self.certifications,

            "projects":
            self.projects,

            "summary":
            self.summary
        }