import arxiv
from summarise import summarise_papers

def fetch_papers(query, max_results=10):
    
    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by = arxiv.SortCriterion.Relevance,
        sort_order = arxiv.SortOrder.Descending
        )
    papers = []
    results = client.results(search)
    for result in results:
        paper_info = {
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'summary': result.summary,
            'published': result.published,
            'pdf_url': result.pdf_url
        }
        papers.append(paper_info)
    return papers


def print_papers(papers):
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Published: {paper['published']}")
        print(f"Summary: {paper['summary']}")
        print(f"PDF URL: {paper['pdf_url']}")
        print("-" * 80)

if __name__ == "__main__":    
    query = "cs.AI" 
    papers = fetch_papers(query)
    for paper in papers:
        claude_summary = summarise_papers(paper['summary'])
        print(f"Title: {paper['title']}")
        print()
        print(claude_summary)
        print("-" * 80)

    