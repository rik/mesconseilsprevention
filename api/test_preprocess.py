def test_transform_list():
    from preprocess import transform_list

    assert transform_list(
        [
            "La santé des adolescents (11 à 17 ans)",
            "La santé des jeunes adultes (18 à 35 ans)",
            "La santé des adultes (35 à 55 ans)",
        ]
    ) == (
        "["
        '"La santé des adolescents (11 à 17 ans)",'
        '"La santé des jeunes adultes (18 à 35 ans)",'
        '"La santé des adultes (35 à 55 ans)"'
        "]"
    )


def test_extract_ages():
    from preprocess import extract_ages

    assert (
        extract_ages(
            [
                "La santé des adolescents (11 à 17 ans)",
                "La santé des jeunes adultes (18 à 35 ans)",
                "La santé des adultes (35 à 55 ans)",
            ]
        )
        == (11, 55)
    )


def test_extract_ages_without_ages_returns_zeros():
    from preprocess import extract_ages

    assert extract_ages(["La santé des personnes âgées (85 ans et plus)"]) == (0, 0)


def test_transform_row():
    from preprocess import transform_row

    assert transform_row(
        {
            "Centres d'intérêt santé": (
                "La santé des adolescents (11 à 17 ans)|"
                "La santé des jeunes adultes (18 à 35 ans)|"
                "La santé des adultes (35 à 55 ans)"
            )
        }
    ) == {
        "Age_max": 55,
        "Age_min": 11,
        "Centres d'intérêt santé": (
            "["
            '"La santé des adolescents (11 à 17 ans)",'
            '"La santé des jeunes adultes (18 à 35 ans)",'
            '"La santé des adultes (35 à 55 ans)"'
            "]"
        ),
    }


def test_transform_row_without_cis_is_noop():
    from preprocess import transform_row

    assert transform_row({"foo": "bar"}) == {"foo": "bar"}
