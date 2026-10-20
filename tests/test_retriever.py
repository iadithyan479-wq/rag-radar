import unittest
from rag_radar.retriever import Passage,TfidfRetriever,citation_context
class TestRetriever(unittest.TestCase):
    def test_relevant_passage_ranks_first(self):
        r=TfidfRetriever([Passage('a.md',1,'edge inference reduces latency'),Passage('b.md',1,'cats sleep')]).search('edge latency',1)
        self.assertEqual(r[0].source,'a.md'); self.assertIn('[a.md:1]',citation_context(r))
if __name__=='__main__': unittest.main()
