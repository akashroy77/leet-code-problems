# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:53:43 2019

@author: akash
"""

 isS=self.order(root,root)
        return isS
    def order(self,tree1,tree2):
        val=False
        if(tree1 is None and tree2 is None):
            return True
        if(tree1 is None or tree2 is None):
            return False
        if(tree1 and tree2):
            return (tree1.val==tree2.val) and self.order(tree1.right,tree2.left) and self.order(tree1.left,tree2.right)