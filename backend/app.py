from flask import (
    Flask,
    jsonify
)
from flask_cors import (
    CORS
)
from backend.routes.jd_routes import (
    jd_bp
)
from backend.routes.candidate_routes import (
    candidate_bp
)
from backend.routes.ranking_routes import (
    ranking_bp
)
from backend.config import (
    config
)
def create_app():
    app = Flask(__name__)
    app.config[
        "SECRET_KEY"
    ] = config.SECRET_KEY
    CORS(app)
    app.register_blueprint(
        jd_bp,
        url_prefix="/api/jd"
    )
    app.register_blueprint(
        candidate_bp,
        url_prefix="/api/candidates"
    )
    app.register_blueprint(
        ranking_bp,
        url_prefix="/api/ranking"
    )
    @app.route("/")
    def home():
        return jsonify(
            {
                "project":
                "TalentSphere",

                "version":
                "1.0.0",

                "status":
                "running",

                "features":
                [
                    "Semantic Search",
                    "Resume Parsing",
                    "Candidate Ranking",
                    "Fraud Detection",
                    "Explainable AI"
                ]
            }
        )
    @app.route("/health")
    def health():
        return jsonify(
            {
                "status":
                "healthy"
            }
        )

    return app
app = create_app()
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=config.DEBUG
    )