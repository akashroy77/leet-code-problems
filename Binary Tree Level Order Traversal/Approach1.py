# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:11:57 2019

@author: akash
"""

import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if(root is None):
            return root
        else:
            q=queue.Queue()
            q.put(root)
            while(q.empty()!=True):
                level=[]
                for i in range(q.qsize()):
                    current=q.get()
                    level.append(current.val)
                    if(current.left is not None):
                        q.put(current.left)
                    if(current.right is not None):
                        q.put(current.right)
                result.append(level)
            return result