from flask import (
    Blueprint,
    request,
    jsonify
)

from ai_engine.jd_parser import (
    extract_requirements
)

jd_bp = Blueprint(
    "jd",
    __name__
)

@jd_bp.route(
    "/analyze",
    methods=["POST"]
)
def analyze_jd():

    try:

        data = request.json

        jd_text = data.get(
            "job_description",
            ""
        )

        if not jd_text:

            return jsonify(
                {
                    "error":
                    "Job Description Missing"
                }
            ), 400

        extracted_data = (
            extract_requirements(
                jd_text
            )
        )

        return jsonify(
            {
                "success": True,
                "analysis":
                extracted_data
            }
        )

    except Exception as e:

        return jsonify(
            {
                "success": False,
                "error": str(e)
            }
        ), 500