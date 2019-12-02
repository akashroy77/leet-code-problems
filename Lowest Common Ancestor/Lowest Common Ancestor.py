# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 00:33:09 2019

@author: akash
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r=self.search(root,p,q)
        return r
    def search(self,root,p,q):
        if(root is None):
            return None
        if(root.val==p.val or root.val==q.val):
            return root
        lt=self.search(root.left,p,q)
        rt=self.search(root.right,p,q)
        #print(lt.val,rt.val)
        if(lt is None):
            return rt
        if(rt is None):
            return lt
        return root