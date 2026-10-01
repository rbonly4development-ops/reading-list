from reading_list import compute_stats, group_books, render_page, sort_books

SAMPLE = [
    {"title": "B Book", "author": "Zed", "status": "read", "rating": 4},
    {"title": "A Book", "author": "Ann", "status": "to-read", "rating": None},
]


def test_compute_stats_counts_read():
    assert compute_stats(SAMPLE) == {"total": 2, "read": 1, "average_rating": 4.0}


def test_sort_books_orders_by_author():
    result = sort_books(SAMPLE)
    assert [b["title"] for b in result] == ["A Book", "B Book"]


def test_render_page_contains_title():
    assert "My Reading List" in render_page(SAMPLE)


def test_render_page_escapes_html():
    tricky = [{"title": "<script>", "author": "X", "status": "read", "rating": 5}]
    assert "<script>" not in render_page(tricky)

def test_group_books_makes_rows_of_three():
    assert group_books(list(range(7)), 3) == [[0, 1, 2], [3, 4, 5], [6]]