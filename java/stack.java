/*package whatever //do not write package name here */

import java.io.*;

class Stack {
    public int capacity;
    public int a[];
    public int top;
    public Stack(int capacity){
        this.top = -1;
        this.capacity = capacity;
        this.a = new int [capacity];
    }
    
    boolean isEmpty(){
        if (top<0){
            System.out.println("The stack is Empty");
            return true;
        }
        return false;
    }
    
    boolean push(int item){
        if (top >= capacity-1){
            System.out.println("Stack overflow");
            return false;
        }
        else {
            a[++top] = item;
            System.out.println(item+" is pushed");
            return true;
        }
    }
    
    boolean pop(){
        if (top < 0){
            System.out.println("Stack underflow");
            return false;
        }
        else {
            int item = a[top--];
            System.out.println(item+" is popped");
            return true;
        }
    }
    
    int peak(){
        if (top < 0){
            System.out.println("Stack underflow");
            return 0;
        }
        else {
            int item = a[top];
            System.out.println(item+" is the value");
            return item;
        }   
    }
    
    void print(){
        if(top < 0){
            System.out.println("Nothing to print");
        } 
        for (int i = this.top; i>=0; i--){
            System.out.println(a[i]);
        }
    }
}

class GFG {
	public static void main (String[] args) {
        Stack s = new Stack(3);	
        boolean check = s.isEmpty();
        s.push(1);
        s.push(2);
        s.push(5);
        s.print();
        s.pop();
        s.print();
	}
}