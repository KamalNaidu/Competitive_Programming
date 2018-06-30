import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }

        public BinaryTreeNode insertLeft(int leftValue) {
            this.left = new BinaryTreeNode(leftValue);
            return this.left;
        }

        public BinaryTreeNode insertRight(int rightValue) {
            this.right = new BinaryTreeNode(rightValue);
            return this.right;
        }
    }

    public static int findSecondLargest(BinaryTreeNode root) {
        // System.out.println(root.value);
        BinaryTreeNode curr=root;
        BinaryTreeNode prev=root;

        // find the second 3largest item in the binary search tree
        
        if(root==null)
            throw new IllegalArgumentException("Empty node");
        
        if(root.left==null&&root.right==null)
            throw new IllegalArgumentException("Noleft and right nodes");

        //Go to the largest node
        while(curr.right != null){
            prev = curr;
            curr= curr.right;
        }
        //If largest Node has left child, Then largest element of tree with its root as largest.left will be the second largest number.
        if(curr.left == null)
            return prev.value;
        else
            return findLargest(curr.left);
        // return 0;
    }
    public static int findLargest(BinaryTreeNode root){
        // No need toi check for null condition as in getSecondLargest method, its already done.
        BinaryTreeNode curr=root;
        //To find largest just keep on going to right child till leaf is encountered.
        while(curr.right != null){
            curr = curr.right;
        }
        return curr.value;
        
    }