using System;
using System.Collections.Generic;
static class ext{
        public static void Main(){
              new int[]{1,2,3}.Print();
        }
        public  static void Print<T>(this IEnumerable<T> a){ 
                foreach(var x in a){
                Console.WriteLine(x);
                }
        }
}
