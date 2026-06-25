class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Map to store the count of each card value
        cardCount = defaultdict(int)
        for card in hand:
            cardCount[card] += 1

        # Sorted list of card values
        sortedCards = sorted(cardCount.keys())
        # Queue to keep track of the number of new groups
        # starting with each card value
        groupStartQueue = deque()
        lastCard = -1
        currentOpenGroups = 0

        for currentCard in sortedCards:
            # Check if there are any discrepancies in the sequence
            # or more groups are required than available cards
            if (
                currentOpenGroups > 0 and currentCard > lastCard + 1
            ) or currentOpenGroups > cardCount[currentCard]:
                return False

            # Calculate the number of new groups starting
            # with the current card
            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups)
            lastCard = currentCard
            currentOpenGroups = cardCount[currentCard]

            # Maintain the queue size to be equal to groupSize
            if len(groupStartQueue) == groupSize:
                currentOpenGroups -= groupStartQueue.popleft()

        # All groups should be completed by the end
        return currentOpenGroups == 0