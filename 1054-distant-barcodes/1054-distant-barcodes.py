class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        n=len(barcodes)
        count = Counter(barcodes)
        barcodes.sort(key=lambda x: (count[x],x))

        res= [""]*n
        for i in range(0,n,2):
            res[i]=barcodes.pop()
        for i in range(1,n,2):
            res[i]=barcodes.pop()
        return res      
