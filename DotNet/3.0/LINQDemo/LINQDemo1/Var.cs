using Microsoft.VisualStudio.TestTools.UnitTesting;
namespace LINQDemo
{
    [TestClass]
    public class Var
    {
        [TestMethod]
        public void Test()
        {
            var i = 34;
            var str = "string";
            //i = str;
            //i = 1.4;
            Assert.AreEqual(typeof(int),i.GetType());
            Assert.AreEqual(typeof(string),str.GetType());
        }
    }
}