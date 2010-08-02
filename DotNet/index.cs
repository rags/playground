// Decompiled by Salamander version 1.0.9
// Copyright 2002 Remotesoft Inc. All rights reserved.
// http://www.remotesoft.com/salamander

using System;

class x
{

    public object[] this[int index]
    {
        get
        {
            return new object[1];
        }

        set
        {
            object [] obj = value;
        }
    }

    public int Itemx
    {
        get
        {
            return 2;
        }

        set
        {
            Console.Write(value);
        }
    }

}


