import java.io.*;

class Node {
    public int data;
    public Node next;
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}

class LinkedList{
    public Node head;
    LinkedList(){
        head = null;
    }

    public void insert_at_end(int new_data)
    {
        Node new_node = new Node(new_data);
        if (head == null){
            head = new_node;
            return;
        }
        new_node.next = null;
        Node mover = head;
        while(mover.next != null){
            mover = mover.next;
        }
        mover.next = new_node;
        return;
    }

    public void insert_at_begining(int new_data)
    {
        Node new_node = new Node(new_data);

        /* 3. Make next of new Node as head */
        new_node.next = head;

        /* 4. Move the head to point to new Node */
        head = new_node;
    }

    public void append(int new_data)
    {
        Node new_node = new Node(new_data);
        if (head == null) {
            head = new Node(new_data);
            return;
        }

        new_node.next = null;
        Node last = head;
        while (last.next != null)
            last = last.next;

        last.next = new_node;
        return;
    }


    public void print(){
        Node mover = head;
        while(mover != null){
            System.out.println(mover.data);
            mover = mover.next;
        }
    }
}

class GFG {
	public static void main (String[] args) {
        Node node = new Node(4);
        LinkedList li = new LinkedList();
        li.insert_at_begining(1);
        li.insert_at_begining(2);
        li.insert_at_begining(3);
        li.insert_at_end(4);
        li.print();
	}
}