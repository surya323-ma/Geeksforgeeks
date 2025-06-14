Given the root of a binary tree, check whether it is symmetric, i.e., whether the tree is a mirror image of itself.
A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

#code here

/*
class of the node of the tree is as
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}

*/
class Solution {
    public static boolean isSymmetric(Node root) {
        // your code here;
        Stack<Node> left = new Stack<>();
        Stack<Node> right = new Stack<>();
        left.push(root.left);
        right.push(root.right);
        while(!left.isEmpty() && !right.isEmpty())
        {
            Node a = left.pop();
            Node b = right.pop();
            
            if(a==null && b==null)
                continue;
                
            if(a==null || b==null || a.data != b.data)
                return false;
                
            left.push(a.left);
            left.push(a.right);
            
            right.push(b.right);
            right.push(b.left);
        }
        return true;
    }
    
}
