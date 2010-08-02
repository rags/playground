using System;
class LLImppl
{
    public static void Main()
    {
        LinkedList list = new LinkedList();
        for(;;)
        {
            Console.Write(
                                "-------------Menu-------------\n" +                   
                                "1. Append\n" +
                                "2. Insert at\n" +
                                "3. Delete at\n" +
                                "4. Display item\n" +
                                "5. Display All\n" +
                                "Or press any key other to exit\n" +
                                "Enter choice: "
                             );
            int ip = (int)Console.ReadLine()[0];
            switch(ip)
            {
                case 49:
                    Append(list);
                    break;
                case 50:
                    Insert(list);
                    break;
                case 51:
                    Delete(list);
                    break;
                case 52:
                    Display(list);
                    break;
                case 53:
                    list.PrintList();
                    break;
                default:
                    return;    
            }

        }
    }

    public static void Append(LinkedList list)
    {
        Console.Write("Enter number: ");
        int data;
        try
        {
            data = int.Parse(Console.ReadLine());
            Console.WriteLine("Append done");
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid data");
            return;
        }
        list.Append(data);

    }

    public static void Insert(LinkedList list)
    {   
        int pos,data;
        Console.Write("Enter number: ");
        try
        {
            data = int.Parse(Console.ReadLine());
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid data");
            return;
        }
        Console.Write("Enter index(0 based): ");
        try
        {
            pos = int.Parse(Console.ReadLine());
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }
        try
        {
            list.Insert(pos,data);
            Console.WriteLine("Insert done");
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }


    }

    public static void Delete(LinkedList list)
    {   
        int pos;
        Console.Write("Enter index(0 based): ");
        try
        {
            pos = int.Parse(Console.ReadLine());
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }
        try
        {
            list.RemoveAt(pos);
            Console.WriteLine("Delete done");
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }

    }
    public static void Display(LinkedList list)
    {   
        int pos;
        Console.Write("Enter index(0 based): ");
        try
        {
            pos = int.Parse(Console.ReadLine());
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }
        try
        {
            Console.WriteLine("Data @ "+ pos + " : " + list[pos]);
        }
        catch(Exception ex)
        {
            Console.WriteLine("Invalid postion");
            return;
        }
    }
    

}
