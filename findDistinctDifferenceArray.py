class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        global arry
        arry = []
        for i in range(len(nums)):
            sufix = nums[:i+1]
            prefix = nums[i+1:]
            differentsIzq=[]
            differentsDer=[]
            for i in range(len(sufix)):
                if sufix[i] in differentsIzq:
                    pass
                else:
                    differentsIzq.append(sufix[i])
            for i in range(len(prefix)):
                if prefix[i] in differentsDer:
                    pass
                else:
                    differentsDer.append(prefix[i])
            arry.append(int(len(differentsIzq)-len(differentsDer))) 
        return arry

solucion = Solution()
nums = [2,5,9,8,2]
print(solucion.distinctDifferenceArray(nums))