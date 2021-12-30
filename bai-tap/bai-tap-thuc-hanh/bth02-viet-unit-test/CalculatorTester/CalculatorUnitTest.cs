using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Calculator;
using System.Data;

namespace CalculatorTester
{
    /// <summary>
    /// Summary description for UnitTest1
    /// </summary>
    [TestClass]
    public class CalculatorUnitTest
    {
        private Calculation calculation;

        public TestContext TestContext { get; set; }

        // Khởi tạo các giá trị trước mỗi Test Case
        [TestInitialize]
        public void SetUp()
        {
            this.calculation = new Calculation(10, 5);
        }

        #region TestOperation

        /* Các Test Case cho trường hợp đúng */

        // Test Case cộng
        [TestMethod]
        public void TestAddOperator()
        {
            // Dùng lớp Assert để kiểm tra
            // liệu kết quả của phép cộng có bằng 15
            Assert.AreEqual(calculation.Execute("Plus"), 15);
        }

        // Test Case trừ
        [TestMethod]
        public void TestSubOperator()
        {
            // Dùng lớp Assert để kiểm tra
            // liệu kết quả của phép trừ có bằng 5
            Assert.AreEqual(calculation.Execute("Minus"), 5);
        }

        // Test Case nhân
        [TestMethod]
        public void TestMulOperator()
        {
            // Dùng lớp Assert để kiểm tra
            // liệu kết quả của phép nhân có bằng 50
            Assert.AreEqual(calculation.Execute("Multiply"), 50);
        }

        // Test Case chia
        [TestMethod]
        public void TestDivOperator()
        {
            // Dùng lớp Assert để kiểm tra
            // liệu kết quả của phép chia có bằng 2
            Assert.AreEqual(calculation.Execute("Divide"), 2);
        }

        /* Các Test Case cho trường hợp sai */

        [TestMethod]

        // Kết quả lỗi mong đợi muốn bắt là lỗi chia cho 0
        [ExpectedException(typeof(DivideByZeroException))]
        public void TestDivByZero()
        {
            Calculation c = new Calculation(2, 0);
            c.Execute("Divide");
        }

        // Thêm một test case
        // kiểm tra làm tròn trong kết quả phép chia
        [TestMethod]
        public void TestDivRound()
        {
            // Vì chưa có hàm làm tròn
            // nên kết quả thực tế bằng 1 ≠ mong đợi bằng 2
            Calculation c = new Calculation(5, 3);
            Assert.AreEqual(c.Execute("Divide"), 2);
        }

        // Đọc dữ liệu kiểm thử
        // cho bốn phép toán từ tập tin csv
        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
                    @".\Data\TestDataOperation.csv",
                    "TestDataOperation#csv",
                    DataAccessMethod.Sequential)]

        public void TestOperationWithDataSource()
        {
            int a = int.Parse(TestContext.DataRow[0].ToString());
            int b = int.Parse(TestContext.DataRow[1].ToString());
            string operation = TestContext.DataRow[2].ToString();
            int expected = int.Parse(TestContext.DataRow[3].ToString());

            Calculation c = new Calculation(a, b);
            int actual = c.Execute("operation");
            
            Assert.AreEqual(expected, actual);
        }
		 
	    #endregion

        #region TestPower

        // Kiểm tra hàm mũ - 1
        [TestMethod]
        public void TestPower1()
        {
            // 2^0 = 1
            Assert.AreEqual(Calculation.Power(2, 0), 1);
        }

        // Kiểm tra hàm mũ - 2
        [TestMethod]
        public void TestPower2()
        {
            // 2^3 = 8
            // Xảy ra lỗi vì
            // kết quả thực tế bằng 6 ≠ mong đợi bằng 8
            Assert.AreEqual(Calculation.Power(2, 3), 8);
        }

        // Kiểm tra hàm mũ - 3
        [TestMethod]
        public void TestPower3()
        {
            // 2^(-1) = -0.5
            Assert.AreEqual(Calculation.Power(2, -1), 0.5);
        }

        // Đọc dữ liệu kiểm thử
        // cho hàm mũ từ tập tin csv
        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
                    @".\Data\TestDataPower.csv",
                    "TestDataPower#csv",
                    DataAccessMethod.Sequential)]

        public void TestPowerWithDataSource()
        {
            int n;
            double x;
            double expected, actual;

            x = double.Parse(TestContext.DataRow[0].ToString());
            n = int.Parse(TestContext.DataRow[1].ToString());
            expected = double.Parse(TestContext.DataRow[2].ToString());
            actual = Calculation.Power(x, n);

            Assert.AreEqual(expected, actual);
        }
		 
	    #endregion

        #region TestPolynomial

        // Có xử lý ngoại lệ - nhập không đủ n + 1 hệ số
        [TestMethod]
        [ExpectedException (typeof(ArgumentException))]
        public void TestPolynomial1()
        {
            int n = 3;
            List<int> a = new List<int>() { 1, 2, 3 };
            Polynomial p = new Polynomial(n, a);
        }

        // Có xử lý ngoại lệ - nhập n âm
        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void TestPolynomial2()
        {
            // Chạy sai khi list a = rỗng
            int n = -1;
            List<int> a = new List<int>() { };
            Polynomial p = new Polynomial(n, a);
        }

        // Test Case pass
        [TestMethod]
        public void TestPolynomial3()
        {
            int n = 2;
            List<int> a = new List<int>() { 1, 2, 3 };
            Polynomial p = new Polynomial(n, a);
            double x = 2;
            Assert.AreEqual(p.Cal(x), 17);
        }
		 
	    #endregion

        #region Redix

        // Hiển thị thông báo lỗi
        [TestMethod]
        [ExpectedException (typeof(ArgumentException))]
        public void Radix1()
        {
            int number = -1;
            Radix r = new Radix(number);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void ConvertDecimalToAnother1()
        {
            int number = 7;
            int radix = 1;
            Radix r = new Radix(number);
            r.ConvertDecimalToAnother(radix);
        }

        [TestMethod]
        public void ConvertDecimalToAnother2()
        {
            // So sánh số sau khi chuyển với 101
            int number = 5;
            int radix = 2;
            Radix r = new Radix(number);
            Assert.AreEqual(r.ConvertDecimalToAnother(radix), "101");
        }

        // Đọc dữ liệu kiểm thử cho đa thức từ tập tin csv
        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
                    @".\Data\TestDataRadix.csv",
                    "TestDataRadix#csv",
                    DataAccessMethod.Sequential)]

        public void ConvertDecimalToAnother3()
        {
            int radix = int.Parse(TestContext.DataRow[0].ToString());
            int number = int.Parse(TestContext.DataRow[1].ToString());
            string expected = TestContext.DataRow[2].ToString();
            
            Radix r = new Radix(number);
            Assert.AreEqual(expected, r.ConvertDecimalToAnother(radix));
        }

        #endregion

    }
}
