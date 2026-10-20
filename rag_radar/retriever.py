from dataclasses import dataclass
import math, re
@dataclass
class Passage: source: str; line: int; text: str; score: float=0.0
class TfidfRetriever:
    def __init__(self, passages):
        self.passages=passages; self.docs=[self._tokens(p.text) for p in passages]; self.df={}
        for doc in self.docs:
            for t in set(doc): self.df[t]=self.df.get(t,0)+1
    def _tokens(self,text): return re.findall(r"[a-z0-9]+",text.lower())
    def search(self, query, k=3):
        q=self._tokens(query); n=len(self.docs); scores=[]
        for p,doc in zip(self.passages,self.docs):
            tf={t:doc.count(t)/max(1,len(doc)) for t in set(doc)}; score=0.0
            for t in q:
                if t in tf: score += tf[t]*math.log((n+1)/(self.df.get(t,0)+1))
            scores.append(Passage(p.source,p.line,p.text,score))
        return sorted(scores,key=lambda p:p.score,reverse=True)[:k]
def load_markdown(directory):
    from pathlib import Path
    out=[]
    for path in sorted(Path(directory).glob('*.md')):
        for i,line in enumerate(path.read_text().splitlines(),1):
            if line.strip(): out.append(Passage(path.name,i,line.strip()))
    return out
def citation_context(results): return '\n'.join(f'[{p.source}:{p.line}] {p.text}' for p in results)
