public class Node
{
        int data;
        Node next;
        public Node(int data)
        {
                this.data = data;
        }
        
        public Node(int data,Node next)
        {
                this.data = data;
                this.next = next;
        }

        public int Data
        {
                get
                {
                        return data;
                }
                set
                {
                        data = value;
                }
        }
        
        public Node Next
        {
                get
                {
                        return next;
                }
                set
                {
                        next = value;
                }
        }
                
}
