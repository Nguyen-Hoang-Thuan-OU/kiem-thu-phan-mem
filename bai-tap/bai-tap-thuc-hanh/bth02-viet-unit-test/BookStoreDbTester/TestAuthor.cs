using System;
using System.Text;
using System.Data;
using System.Data.Common;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Microsoft.Data.Schema.UnitTesting;
using Microsoft.Data.Schema.UnitTesting.Conditions;

namespace BookStoreDbTester
{
    [TestClass()]
    public class TestAuthor : DatabaseTestClass
    {

        public TestAuthor()
        {
            InitializeComponent();
        }

        [TestInitialize()]
        public void TestInitialize()
        {
            base.InitializeTest();
        }
        [TestCleanup()]
        public void TestCleanup()
        {
            base.CleanupTest();
        }

        #region Designer support code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            Microsoft.Data.Schema.UnitTesting.DatabaseTestAction dbo_Top3AuthorsTest_TestAction;
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TestAuthor));
            Microsoft.Data.Schema.UnitTesting.Conditions.RowCountCondition rowCountCondition1;
            Microsoft.Data.Schema.UnitTesting.Conditions.ChecksumCondition checksumCondition1;
            Microsoft.Data.Schema.UnitTesting.Conditions.ScalarValueCondition scalarValueCondition1;
            this.dbo_Top3AuthorsTestData = new Microsoft.Data.Schema.UnitTesting.DatabaseTestActions();
            dbo_Top3AuthorsTest_TestAction = new Microsoft.Data.Schema.UnitTesting.DatabaseTestAction();
            rowCountCondition1 = new Microsoft.Data.Schema.UnitTesting.Conditions.RowCountCondition();
            checksumCondition1 = new Microsoft.Data.Schema.UnitTesting.Conditions.ChecksumCondition();
            scalarValueCondition1 = new Microsoft.Data.Schema.UnitTesting.Conditions.ScalarValueCondition();
            // 
            // dbo_Top3AuthorsTestData
            // 
            this.dbo_Top3AuthorsTestData.PosttestAction = null;
            this.dbo_Top3AuthorsTestData.PretestAction = null;
            this.dbo_Top3AuthorsTestData.TestAction = dbo_Top3AuthorsTest_TestAction;
            // 
            // dbo_Top3AuthorsTest_TestAction
            // 
            dbo_Top3AuthorsTest_TestAction.Conditions.Add(rowCountCondition1);
            dbo_Top3AuthorsTest_TestAction.Conditions.Add(checksumCondition1);
            dbo_Top3AuthorsTest_TestAction.Conditions.Add(scalarValueCondition1);
            resources.ApplyResources(dbo_Top3AuthorsTest_TestAction, "dbo_Top3AuthorsTest_TestAction");
            // 
            // rowCountCondition1
            // 
            rowCountCondition1.Enabled = true;
            rowCountCondition1.Name = "rowCountCondition1";
            rowCountCondition1.ResultSet = 1;
            rowCountCondition1.RowCount = 3;
            // 
            // checksumCondition1
            // 
            checksumCondition1.Checksum = "2118284646";
            checksumCondition1.Enabled = true;
            checksumCondition1.Name = "checksumCondition1";
            // 
            // scalarValueCondition1
            // 
            scalarValueCondition1.ColumnNumber = 5;
            scalarValueCondition1.Enabled = true;
            scalarValueCondition1.ExpectedValue = "0984461466";
            scalarValueCondition1.Name = "scalarValueCondition1";
            scalarValueCondition1.NullExpected = false;
            scalarValueCondition1.ResultSet = 1;
            scalarValueCondition1.RowNumber = 1;
        }

        #endregion


        #region Additional test attributes
        //
        // You can use the following additional attributes as you write your tests:
        //
        // Use ClassInitialize to run code before running the first test in the class
        // [ClassInitialize()]
        // public static void MyClassInitialize(TestContext testContext) { }
        //
        // Use ClassCleanup to run code after all tests in a class have run
        // [ClassCleanup()]
        // public static void MyClassCleanup() { }
        //
        #endregion


        [TestMethod()]
        public void dbo_Top3AuthorsTest()
        {
            DatabaseTestActions testActions = this.dbo_Top3AuthorsTestData;
            // Execute the pre-test script
            // 
            System.Diagnostics.Trace.WriteLineIf((testActions.PretestAction != null), "Executing pre-test script...");
            ExecutionResult[] pretestResults = TestService.Execute(this.PrivilegedContext, this.PrivilegedContext, testActions.PretestAction);
            // Execute the test script
            // 
            System.Diagnostics.Trace.WriteLineIf((testActions.TestAction != null), "Executing test script...");
            ExecutionResult[] testResults = TestService.Execute(this.ExecutionContext, this.PrivilegedContext, testActions.TestAction);
            // Execute the post-test script
            // 
            System.Diagnostics.Trace.WriteLineIf((testActions.PosttestAction != null), "Executing post-test script...");
            ExecutionResult[] posttestResults = TestService.Execute(this.PrivilegedContext, this.PrivilegedContext, testActions.PosttestAction);
        }
        private DatabaseTestActions dbo_Top3AuthorsTestData;
    }
}
