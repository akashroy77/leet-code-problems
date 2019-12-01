# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:15:26 2019

@author: akash
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        k=[]
        level=0
        result=[]
        k=self.order(root,k,level)
        if(len(k)==0):
            return result
        elif(len(k)==1):
            result=[[k[0][0]]]
        elif(len(k)==2):
            result=[[k[0][0]],[k[1][0]]]
        else:
            result=self.createOrder(k)
        return result
    
    def order(self,tree,k,level):
        if(tree):
            k.append([tree.val,level])
            level=level+1
            self.order(tree.left,k,level)
            self.order(tree.right,k,level)
        return k
    
    def createOrder(self,k):
        i=1
        z=[]
        c=1
        flag=0
        z.append([k[0][0]])
        k.sort(key=lambda x:x[1])
        print(k)
        i=1
        while(i<len(k)):
            temp=[]
            temp.append(k[i][0])
            for j in range(i+1,len(k)):               
                if(k[i][1]==k[j][1]):
                    temp.append(k[j][0])
            if(len(temp)>1):
                count=len(temp)-1
                i=i+1+count
            else:
                i+=1
            print(temp)
            z.append(temp)
        print(z)
        return z
                
   