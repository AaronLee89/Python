class Solution(object):#
    def twoSum(self, nums, target): #self在定义类的方法时必须要有
        dict={}                     #空的字典
        for i in  range(len(nums)): #循环语句
            if  target-nums[i] in dict: #如果两者之差出现在字典中，说明已经找到了这对数
                return  [dict[target-nums[i]],i] #返回索引值
            dict[nums[i]]=i 
        return  []
        