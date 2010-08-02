public class LinkedList
{
    Node head;
    int nodeCount=0;

    public int Count
    {
        get
        {
                return nodeCount;
        }
    }

    public bool Append(int value)
    {
        bool retVal = false;
        Node newNode =  new Node(value);
        if(head==null)
        {
                head = newNode;
                retVal = true;
        }
        else
        {
                Node tempNode = head;
                while(tempNode.Next!=null) tempNode = tempNode.Next;
                tempNode.Next=newNode;
                retVal = true;
        }
        if(retVal) nodeCount++;
        return retVal;
    }

    public bool Insert(int index/*0 based*/,int value)
    {
        Node newNode;
        if(index==0)
        {
                newNode =  new Node(value,head);
                head = newNode;
                nodeCount++;
                return true;
        }
        if(index>=nodeCount) throw new System.IndexOutOfRangeException();
        Node tempNode=head;
        for(int i=0;i<index-1;i++)tempNode = tempNode.Next;
        newNode =  new Node(value,tempNode.Next);
        tempNode.Next = newNode;
        nodeCount++;
        return true; 
    }

    public int RemoveAt(int index)
    {
        if(index>=nodeCount) throw new System.IndexOutOfRangeException();
        Node tempNode=head;
        for(int i=0;i<index-1;i++)tempNode = tempNode.Next;
        Node nodeToDelete = tempNode.Next;
        tempNode.Next = nodeToDelete.Next;
        int retVal=nodeToDelete.Data;
        nodeToDelete = null;
        nodeCount--;
        return retVal;
    }

    public int this[int index]
    {
        get
        {
            if(index>=nodeCount) throw new System.IndexOutOfRangeException();
            Node tempNode=head;
            for(int i=0;i<index;i++,tempNode = tempNode.Next);
            return tempNode.Data;
        }
    }

    public void PrintList()
    {
        if(head==null) return;
        for(Node tempNode=head;tempNode!=null;tempNode=tempNode.Next)
        {
           System.Console.Write(tempNode.Data + "-->");
        }
        System.Console.WriteLine("NULL");
    }
}

