"""Generate a static reading-list page from books.json."""

import json
from html import escape
from pathlib import Path

#Added Multiple jobs
def load_books(path="books.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compute_stats(books):
    read = [b for b in books if b["status"] == "read"]
    ratings = [b["rating"] for b in read if b.get("rating") is not None]
    average = round(sum(ratings) / len(ratings), 1) if ratings else None
    return {"total": len(books), "read": len(read), "average_rating": average}


def sort_books(books):
    return sorted(books, key=lambda b: (b["author"], b["title"]))


def render_page(books):
    stats = compute_stats(books)
    average = stats["average_rating"] if stats["average_rating"] is not None else "n/a"
    rows = "\n".join(
        f"<tr><td>{escape(b['title'])}</td><td>{escape(b['author'])}</td>"
        f"<td>{escape(b['status'])}</td><td>{escape(str(b.get('rating') or '-'))}</td></tr>"
        for b in sort_books(books)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>My Reading List</title>
<style>
body {{ font-family: sans-serif; max-width: 42rem; margin: 2rem auto; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border-bottom: 1px solid #ddd; padding: 0.4rem; text-align: left; }}
</style>
</head>
<body>
<h1>My Reading List</h1>
<p>{stats['total']} books &middot; {stats['read']} read &middot; average rating {average}</p>
<table>
<tr><th>Title</th><th>Author</th><th>Status</th><th>Rating</th></tr>
{rows}
</table>
</body>
</html>"""


def build(output_dir="site"):
    books = load_books()
    out = Path(output_dir)
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(render_page(books), encoding="utf-8")
    print(f"Built {out / 'index.html'} with {len(books)} books")


if __name__ == "__main__":
    build()

#edited py file