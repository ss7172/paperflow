import sqlite3

def init_db():
    conn = sqlite3.connect('papers.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS papers (id INTEGER PRIMARY KEY, title TEXT, authors TEXT, abstract TEXT, claude_summary TEXT, published DATE, pdf_url TEXT UNIQUE)")
    conn.commit()
    conn.close()

def save_paper(title, authors, abstract, claude_summary, published, pdf_url):
    conn = sqlite3.connect('papers.db')
    cur = conn.cursor()

    authors = ', '.join(authors)  # Convert list of authors to a comma-separated string
    sql_query = "INSERT OR IGNORE INTO papers (title, authors, abstract, claude_summary, published, pdf_url) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(sql_query, (title, authors, abstract, claude_summary, published, pdf_url))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()