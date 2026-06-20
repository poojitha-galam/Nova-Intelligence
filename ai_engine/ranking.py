from ai_engine.embeddings import (
    create_embedding
)
from ai_engine.vector_search import (
    cosine_similarity
)
def rank_candidates(
    jd_embedding,
    candidates
):
    results = []
    for candidate in candidates:
        candidate_embedding = (
            create_embedding(
                candidate[
                    "summary"
                ]
            )
        )
        similarity = (
            cosine_similarity(
                jd_embedding,
                candidate_embedding
            )
        )
        final_score = round(
            similarity * 100,
            2
        )
        results.append(
            {
                "candidate_id":
                candidate.get(
                    "candidate_id"
                ),

                "name":
                candidate.get(
                    "name"
                ),

                "score":
                final_score
            }
        )
    results.sort(
        key=lambda x:
        x["score"],
        reverse=True
    )
    return results