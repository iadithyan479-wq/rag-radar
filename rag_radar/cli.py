import argparse
from .retriever import load_markdown,TfidfRetriever,citation_context
p=argparse.ArgumentParser(); p.add_argument('--docs',required=True); p.add_argument('--query',required=True); a=p.parse_args()
results=TfidfRetriever(load_markdown(a.docs)).search(a.query)
print(citation_context(results) or 'No matching passages found.')
