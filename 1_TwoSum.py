class Solution(object):#
    def twoSum(self, nums, target): #self�ڶ�����ķ���ʱ����Ҫ��
        dict={}                     #�յ��ֵ�
        for i in  range(len(nums)): #ѭ�����
            if  target-nums[i] in dict: #�������֮��������ֵ��У�˵���Ѿ��ҵ��������
                return  [dict[target-nums[i]],i] #��������ֵ
            dict[nums[i]]=i 
        return  []
        