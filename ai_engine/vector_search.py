def cosine_similarity(
    vector_a,
    vector_b
):
    dot_product = sum(
        a * b
        for a, b
        in zip(
            vector_a,
            vector_b
        )
    )
    norm_a = (
        sum(
            a*a
            for a in vector_a
        ) ** 0.5
    )
    norm_b = (
        sum(
            b*b
            for b in vector_b
        ) ** 0.5
    )
    if (
        norm_a == 0
        or
        norm_b == 0
    ):
        return 0
    return (
        dot_product
        /
        (norm_a * norm_b)
    )