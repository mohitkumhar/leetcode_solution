class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = []
        deck = sorted(deck, reverse=True)

        for card in deck:
            if queue:
                queue.insert(0, queue.pop())
            queue.insert(0, card)
        
        return queue
