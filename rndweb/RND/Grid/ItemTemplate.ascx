<%@ Control Language="c#" AutoEventWireup="false" TargetSchema="http://schemas.microsoft.com/intellisense/ie5"%>
<a href='javascript:alert(<%#DataBinder.Eval(((DataGridItem)Container).DataItem,"Customer_Number")%>)'>click</a>
<input type=checkbox value='chk_<%#DataBinder.Eval(((DataGridItem)Container).DataItem,"Customer_Number")%>' id="ChkBox" name="ChkBox" <%#("Active".Equals(DataBinder.Eval(((DataGridItem)Container).DataItem,"Record_Status"))?"":"CHECKED")%>> 
