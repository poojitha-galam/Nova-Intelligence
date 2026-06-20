from flask import (
    Blueprint,
    request,
    jsonify
)
from backend.database.mongodb import (
    candidate_collection
)
candidate_bp = Blueprint(
    "candidate",
    __name__
)
@candidate_bp.route(
    "/add",
    methods=["POST"]
)
def add_candidate():
    try:
        candidate = request.json
        candidate_collection.insert_one(
            candidate
        )
        return jsonify(
            {
                "success": True,
                "message":
                "Candidate Added"
            }
        )
    except Exception as e:
        return jsonify(
            {
                "success": False,
                "error": str(e)
            }
        )
@candidate_bp.route(
    "/all",
    methods=["GET"]
)
def get_candidates():
    candidates = []
    for candidate in (
        candidate_collection.find()
    ):
        candidate["_id"] = str(
            candidate["_id"]
        )
        candidates.append(
            candidate
        )
    return jsonify(
        candidates
    )
@candidate_bp.route(
    "/<candidate_id>",
    methods=["GET"]
)
def get_candidate(
    candidate_id
):
    candidate = (
        candidate_collection.find_one(
            {
                "candidate_id":
                candidate_id
            }
        )
    )
    if not candidate:

        return jsonify(
            {
                "error":
                "Candidate Not Found"
            }
        )
    candidate["_id"] = str(
        candidate["_id"]
    )
    return jsonify(
        candidate
    )