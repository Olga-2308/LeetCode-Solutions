class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        # If all cards have the same suit, we immediately return the flush
        if len(set(suits)) == 1:
            return "Flush"

        # we determine the frequency of each card
        d = {}
        for rank in ranks:
            if rank not in d:
                d[rank] = 1
            else:
                d[rank] += 1

        # we find the maximum frequency by which we will determine the required combination
        max_cards = max(d.values())

        # we return combinations according to the number of identical cards
        if max_cards >= 3:
            return "Three of a Kind"
        elif max_cards == 2:
            return "Pair"
        else:
            return "High Card"