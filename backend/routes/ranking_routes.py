from flask import (
    Blueprint,
    request,
    jsonify
)
from ai_engine.embeddings import (
    create_embedding
)
from ai_engine.ranking import (
    rank_candidates
)
from ai_engine.explainability import (
    generate_explanation
)
ranking_bp = Blueprint(
    "ranking",
    __name__
)
@ranking_bp.route(
    "/match",
    methods=["POST"]
)
def match_candidates():
    try:
        data = request.json
        jd_text = data.get(
            "job_description"
        )
        candidates = data.get(
            "candidates"
        )
        jd_embedding = (
            create_embedding(
                jd_text
            )
        )
        ranked_results = (
            rank_candidates(
                jd_embedding,
                candidates
            )
        )
        for candidate in (
            ranked_results
        ):
            candidate[
                "explanation"
            ] = (
                generate_explanation(
                    candidate
                )
            )
        return jsonify(
            {
                "success": True,
                "rankings":
                ranked_results
            }
        )
    except Exception as e:
        return jsonify(
            {
                "success": False,
                "error": str(e)
            }
        )