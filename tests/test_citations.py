from generation.answer import answer_question


def test_answer_has_sources():
    result = answer_question(
        "What should QA teams test?"
    )

    assert "sources" in result

    assert len(result["sources"]) > 0