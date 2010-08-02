<%@ Page language="c#" Codebehind="frmCustomPagingGrid.aspx.cs" AutoEventWireup="false" Inherits="RND.Grid.frmCustomPagingGrid" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
    <HEAD>
        <title>frmCustomPagingGrid</title>
        <meta content="Microsoft Visual Studio 7.0" name="GENERATOR">
        <meta content="C#" name="CODE_LANGUAGE">
        <meta content="JavaScript" name="vs_defaultClientScript">
        <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
        <script>
    function chkAll(boolChecked)
    {      
      var chkBoxes = document.getElementsByName("gridChkBox");
      for(var i=0;i<chkBoxes.length;i++) chkBoxes[i].checked=boolChecked;
    }
    
        </script>
    </HEAD>
    <body MS_POSITIONING="GridLayout">
        <form id="frmCustomPagingGrid" method="post" runat="server">
            <table>
                <!--0th row-->
                <tr>
                    <td>
                        <asp:ValidationSummary DisplayMode="SingleParagraph" HeaderText="All fields marked with * are mandatory" ID="valSummary" Runat="server" />
                    </td>
                </tr>
                <!--1ST row-->
                <tr>
                    <td>
                        <table cellpadding="0">
                            <tr>
                                <td nowrap>
                                    Customer Name: &nbsp;<INPUT id="txtCustomer" type="text" runat="server" NAME="txtCustomer">
                                    <asp:RequiredFieldValidator ControlToValidate="txtCustomer" ID="txtCustomerValidator" Runat="server">*</asp:RequiredFieldValidator>
                                </td>
                                <td nowrap>
                                    Company Logo: &nbsp;<INPUT id="txtLogo" type="text" runat="server" NAME="txtLogo">
                                    <asp:RequiredFieldValidator ControlToValidate="txtLogo" ID="txtLogoValidator" Runat="server">*</asp:RequiredFieldValidator>
                                </td>
                            </tr>
                            <tr>
                                <td nowrap>
                                    Company URL: &nbsp;&nbsp;&nbsp;<INPUT id="txtURL" type="text" runat="server" NAME="txtURL">
                                    <asp:RequiredFieldValidator ControlToValidate="txtURL" ID="txtURLValidator" Runat="server">*</asp:RequiredFieldValidator>
                                    <asp:RegularExpressionValidator ControlToValidate="txtURL" ID="txtURLRegexVal" ValidationExpression="/^(http|https|ftp):\/\/(([A-Za-z0-9][A-Z0-9_-]*)(\.[A-Za-z0-9][A-Za-z0-9_-]*)+)(:(\d+))?\//i" runat="server">Not a valid url</asp:RegularExpressionValidator>
                                </td>
                                <td>&nbsp;</td>
                                <td>
                                    &nbsp;&nbsp;&nbsp;<asp:Button id="btnAdd" runat="server" Text="Add Record"></asp:Button></td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!--END OF 1ST row-->
                <!--2nd row-->
                <tr>
                    <td colspan="2">
                        
                        <asp:datagrid id="DataGrid1" runat="server" PageSize="3" AllowPaging="True" AutoGenerateColumns="False" DataKeyField="Customer_Number" AllowSorting="true" Width="100%" AllowCustomPaging="True"
                        OnUpdateCommand="Update" 
                        OnPageIndexChanged="PageChange" 
                        OnCancelCommand="Cancel" 
                        OnEditCommand="Edit" 
                        OnDeleteCommand="Delete" 
                        OnSortCommand="Sort" 
                        OnItemDataBound="ChangeHeader" 
                        OnItemCreated="CustomizePager"
                        > 
                            <HeaderStyle BackColor="#9999ff" />
                            <ItemStyle BackColor="#ff9933" />
                            <AlternatingItemStyle BackColor="#99cc99" />
                            <PagerStyle PrevPageText="<" NextPageText=">" Mode="NextPrev" PageButtonCount="3" Position="TopAndBottom" HorizontalAlign="Right" BackColor="#ffffff" />
                            <Columns>
                                <asp:BoundColumn FooterText="Customer" DataField="Customer_Name" ReadOnly="True" HeaderText="Customer" SortExpression="Customer_Name" />
                                <asp:BoundColumn DataField="Logo_Path" HeaderText="Logo" />
                                <asp:BoundColumn DataField="URL" HeaderText="URL" />
                                <asp:BoundColumn DataField="Record_Status" HeaderText="Status" SortExpression="Record_Status"></asp:BoundColumn>
                                <asp:EditCommandColumn HeaderText="Edit" CancelText="cancel" EditText="edit" ButtonType="LinkButton" UpdateText="update" />
                                <asp:ButtonColumn ButtonType="LinkButton" CommandName="Delete" ItemStyle-HorizontalAlign="Center" HeaderText="Delete" Text="x" />
                                <asp:TemplateColumn ItemStyle-HorizontalAlign="Right">
                                    <HeaderTemplate>
                                        Select &nbsp; <input type="checkbox" id="selAll" onclick="chkAll(this.checked)">
                                    </HeaderTemplate>
                                    <ItemTemplate>
                                        <input type=checkbox value='<%#DataBinder.Eval(Container.DataItem,"Customer_Number")%>' id="gridChkBox" name="gridChkBox" <%#("Active".Equals(DataBinder.Eval(Container.DataItem,"Record_Status"))?"":"CHECKED")%>> <!--check when records are not active-->
                                    </ItemTemplate>
                                </asp:TemplateColumn>
                            </Columns>
                        </asp:datagrid>
                    </td>
                </tr>
                <!--2nd row-->
                <!--3rd row-->
                <tr>
                    <td align="right" colspan="2">
                        <asp:Button id="btnDelete" runat="server" Text="Delete Selected" CausesValidation="False"></asp:Button></td>
                </tr>
            </table>
        </form>
    </body>
</HTML>
