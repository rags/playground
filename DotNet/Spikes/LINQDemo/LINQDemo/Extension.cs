using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
    [TestClass]
    class ExtensionTest
    {
    static class Extension
    {
        public static bool TrimEquals(this string str,string otherStr)
        {
         return str.Trim().Equals(otherStr.Trim());   
        }
        
        /*public static bool IsNullOrEmpty1(string str)
        {
         return str==null||str.Trim()==string.Empty;   
        }*/
    }
    [TestMethod]        
    public void TestTrimEquals()
    {
        Assert.IsTrue(" foo ".TrimEquals("foo   "));
        Assert.IsFalse(" foo ".TrimEquals("foo1   "));
    } 
        
    /*[TestMethod]        
    public void TestIsEmptyorNull()
    {
        Assert.IsTrue(string.IsNullOrEmpty1("  "));
        Assert.IsFalse(string.IsNullOrEmpty1("foo1"));
        Assert.IsFalse(string.IsNullOrEmpty1(null));
    }*/
        
    }
}
