class Job:
    def __init__(
        self,
        job_id,
        title,
        description,
        required_skills,
        preferred_skills,
        experience_required,
        education_required
    ):

        self.job_id = job_id
        self.title = title
        self.description = description
        self.required_skills = (
            required_skills
        )
        self.preferred_skills = (
            preferred_skills
        )
        self.experience_required = (
            experience_required
        )
        self.education_required = (
            education_required
        )

    def to_dict(self):

        return {

            "job_id":
            self.job_id,

            "title":
            self.title,

            "description":
            self.description,

            "required_skills":
            self.required_skills,

            "preferred_skills":
            self.preferred_skills,

            "experience_required":
            self.experience_required,

            "education_required":
            self.education_required
        }