using System;
using System.Collections;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
    [TestClass]
    internal class Yield
    {
        private class LinkedList<T> : IEnumerable, ICollection
        
        {
            public class Node<Typ>
            {   
                private Typ _value;
                private Node<Typ> _next;

                public Node<Typ> Next
                {
                    get { return _next; }
                    set { _next = value; }
                }

                public Typ Value
                {
                    get { return _value; }
                    set { _value = value; }
                }

                public Node(Typ value)
                {
                    _value = value;
                }
            }
            private Node<T> _first;
            private int count;

            public IEnumerator GetEnumerator()
            {
                for(Node<T> node = _first;node!=null;node=node.Next)
                {
                    yield return node;
                }
            }

            public void CopyTo(Array array, int index)
            {
                throw new NotImplementedException();
            }

            public int Count
            {
                get { return count; }
            }

            public object SyncRoot
            {
                get { throw new NotImplementedException(); }
            }

            public bool IsSynchronized
            {
                get { throw new NotImplementedException(); }
            }
            
             public void Add(T item)
             {
                 Add(new Node<T>(item));
             }
            
            public void Add(Node<T> node)
            {
                if(_first==null)
                {
                    _first = node;
                }
                else
                {
                    Node<T> curNode = _first;
                    for(;curNode.Next!=null;curNode=curNode.Next);
                    curNode.Next = node;
                }
                count++;
            }
            
        }

        [TestMethod]
        public void Test()
        {
            LinkedList<int> list = new LinkedList<int>();
            var arr = new[] {1, 2, 3};
            list.Add(arr[0]);
            list.Add(arr[1]);
            list.Add(arr[2]);
            Assert.AreEqual(3,list.Count);
            var i = 0;
            foreach (LinkedList<int>.Node<int> node in list)
            {
                Assert.AreEqual(arr[i++], node.Value);
            }
        }
        
    }
}