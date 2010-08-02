<%@ Page language="c#" Codebehind="frmDataRelation.aspx.cs" AutoEventWireup="false" Inherits="RND.frmDataRelation" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmDataRelation</title>
    <meta content="Microsoft Visual Studio 7.0" name="GENERATOR">
    <meta content="C#" name="CODE_LANGUAGE">
    <meta content="JavaScript" name="vs_defaultClientScript">
    <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmDataRelation" method="post" runat="server">
      <asp:DataGrid id="DataGrid1" style="Z-INDEX: 101; LEFT: 353px; POSITION: absolute; TOP: 236px" runat="server">
        <Columns>
          <asp:TemplateColumn HeaderText="Department">
            <ItemTemplate>
              <span>
                <%#GetDeptName(Container.DataItem)%>
              </span>
            </ItemTemplate>
          </asp:TemplateColumn>
        </Columns>
      </asp:DataGrid>
      <asp:CheckBoxList id="DropDownList1" style="Z-INDEX: 102; LEFT: 410px; POSITION: absolute; TOP: 165px" runat="server" AutoPostBack="False" />
      <asp:Label id="Label1" style="Z-INDEX: 103; LEFT: 113px; POSITION: absolute; TOP: 238px" runat="server">
        <%#"Department " + DropDownList1.SelectedItem.Text%>
      </asp:Label></form>
  </body>
</HTML>
