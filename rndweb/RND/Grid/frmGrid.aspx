<%@ Page language="c#" Codebehind="frmGrid.aspx.cs" AutoEventWireup="false" Inherits="RND.frmGrid" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmGrid</title>
    <meta content="Microsoft Visual Studio 7.0" name="GENERATOR">
    <meta content="C#" name="CODE_LANGUAGE">
    <meta content="JavaScript" name="vs_defaultClientScript">
    <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
    <script>
    function selectRow(chkBox)
    {
        var ele = chkBox;    
        do ele = ele.parentNode 
        while(ele!=null && ele.tagName!="TR");
        //use ele.className to set css
        if(chkBox.checked) ele.style.backgroundColor="red";
        else ele.style.backgroundColor="";
    }
    function chkAll(boolChecked)
    {      
      var chkBoxes = document.getElementsByName("gridChkBox");
      for(var i=0;i<chkBoxes.length;i++) chkBoxes[i].checked=boolChecked;
    }    
    function validateEmail()
    {
        var object = arguments[0];
        var args = arguments[1];
        var value = args.Value;        
        var matches = value.match(/^(http|https|ftp):\/\/(([A-Za-z0-9][A-Z0-9_-]*)(\.[A-Za-z0-9][A-Za-z0-9_-]*)+)(:(\d+))?/i);
        //args.IsValid = matches!=null && matches.length>0;
        alert("client validation");
        args.IsValid = true;
    }
    </script>
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmGrid" method="post" runat="server">
      <table>  
      <tr>
      <td>
      <asp:ValidationSummary DisplayMode=SingleParagraph HeaderText="All fields marked with * are mandatory" ID=valSummary Runat=server />
      </td>
      </tr>
        <!--1ST row-->
        <tr>
          <td>
            <table cellpadding="0">
              <tr>
                <td nowrap> 
                        Customer Name: &nbsp;<INPUT id="txtCustomer" type="text" runat=server >
                        <!--<asp:RequiredFieldValidator ControlToValidate=txtCustomer ID=txtCustomerValidator Runat_=server >*</asp:RequiredFieldValidator>-->
                </td>
                <td nowrap>
                Company Logo: &nbsp;<INPUT id="txtLogo" type="text" runat=server >
                <!--<asp:RequiredFieldValidator ControlToValidate=txtLogo ID="txtLogoValidator" Runat_=server >*</asp:RequiredFieldValidator>-->
                </td>
              </tr>
              <tr>
                <td nowrap>
                Company URL: &nbsp;&nbsp;&nbsp;<INPUT id="txtURL" type="text" runat=server >
                <!--
                <asp:RequiredFieldValidator ControlToValidate=txtURL ID="txtURLValidator" Runat_=server >*</asp:RequiredFieldValidator>
                <asp:RegularExpressionValidator ControlToValidate=txtURL ID="txtURLRegexVal" ValidationExpression="/^(http|https|ftp):\/\/(([A-Za-z0-9][A-Z0-9_-]*)(\.[A-Za-z0-9][A-Za-z0-9_-]*)+)(:(\d+))?\//i" runat_=server >Not a valid url</asp:RegularExpressionValidator>-->
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
          <td colspan=2>
            <asp:datagrid id="DataGrid1" runat="server" OnUpdateCommand="Update"  PageSize="3" AllowPaging="True" OnPageIndexChanged="PageChange" OnCancelCommand="Cancel" OnEditCommand="Edit" AutoGenerateColumns="False" DataKeyField="Customer_Number" OnDeleteCommand="Delete" OnSortCommand="Sort" AllowSorting="true" OnItemDataBound=ChangeHeader OnItemCreated="CustomizePager" Width="100%">
            
              <HeaderStyle BackColor="#9999ff" />
              <ItemStyle BackColor="#ff9933" />
              <AlternatingItemStyle BackColor="#99cc99" />
              <PagerStyle PrevPageText="<" NextPageText=">" Mode="NumericPages" PageButtonCount="3" Position="TopAndBottom" HorizontalAlign="Right" BackColor="#ffffff" />              
              <Columns>                
                <asp:BoundColumn FooterText="Customer" DataField="Customer_Name" ReadOnly="True" HeaderText="Customer" SortExpression="Customer_Name" />
                <asp:BoundColumn DataField="Logo_Path" HeaderText="Logo" />
                <asp:BoundColumn DataField="URL" HeaderText="URL" />
                <asp:BoundColumn DataField="Record_Status" HeaderText="Status" SortExpression="Record_Status">                              
                </asp:BoundColumn>
                <asp:EditCommandColumn HeaderText="Edit" CancelText="cancel" EditText="edit" ButtonType="LinkButton" UpdateText="update"  />
                <asp:ButtonColumn ButtonType="LinkButton" CommandName="Delete" ItemStyle-HorizontalAlign="Center" HeaderText="Delete" Text="x" />
                <asp:TemplateColumn ItemStyle-HorizontalAlign="Right">
                  <HeaderTemplate>
                    Select &nbsp; <input type="checkbox" id="selAll" onclick="chkAll(this.checked)">
                  </HeaderTemplate>                  
                  <ItemTemplate>
                    <input type=checkbox value='<%#DataBinder.Eval(Container.DataItem,"Customer_Number")%>' id="gridChkBox" name="gridChkBox" <%#("Active".Equals(DataBinder.Eval(Container.DataItem,"Record_Status"))?"":"CHECKED")%> onclick="selectRow(this)"> <!--check when records are not active-->
                  </ItemTemplate>
                </asp:TemplateColumn>
                <asp:TemplateColumn ItemStyle-HorizontalAlign="Right">
                  <HeaderTemplate>
                    Serials 
                  </HeaderTemplate>
                  <ItemTemplate>
                    <%#Container.ItemIndex%>
                  </ItemTemplate>
                </asp:TemplateColumn>
              </Columns>
            </asp:datagrid>
          </td>
        </tr>
        <!--2nd row-->
        <!--3rd row
        
      <P class=tal>Messenger of fear in sight<BR>Dark deception kills the 
light<BR></P>
<P class=tal>Hybrid children watch the sea<BR>Pray for father, roaming 
free<BR></P>
<P class=tal>Fearless wretch<BR>Insanity<BR>He watches<BR>Lurking beneath the 
sea<BR>Great old one<BR>Forbidden site<BR>He searches<BR>Hunter of the shadows 
is rising<BR>Immortal<BR>In madness you dwell<BR></P>
<P class=tal>Crawling chaos underground<BR>Cult has summoned twisted 
sound<BR></P>
<P class=tal>Out from ruins once possessed<BR>Fallen city, living death<BR></P>
<P class=tal>Fearless wretch<BR>Insanity<BR>He watches<BR>Lurking beneath the 
sea<BR>Timeless sleep<BR>Has been upset<BR>He awakens<BR>Hunter of the shadows 
is rising<BR>Immortal<BR>In madness you dwell<BR>In madness you dwell<BR></P>
<P class=tal><BR>Not dead which eternal lie<BR>Stranger eons, death may 
die<BR></P>
<P class=tal>Drain you of your sanity<BR>Face the thing that should not 
be<BR></P>
<P class=tal>Fearless wretch<BR>Insanity<BR>He watches<BR>Lurking beneath the 
sea<BR>Great old one<BR>Forbidden site<BR>He searches<BR>Hunter of the shadows 
is rising<BR>Immortal<BR>In madness you dwell<BR></P>

<P style="MARGIN-LEFT: 10px; COLOR: #ffffff">Halls of justice painted 
green<BR>Money talking<BR>Power wolves beset your door<BR>Hear them 
stalking<BR>Soon you’ll please their appetite<BR>They devour<BR>Hammer of 
justice crushes you<BR>Overpower<BR><BR>The ultimate in vanity<BR>Exploiting 
their supremacy<BR>I can’t believe the things you say<BR>I can’t believe<BR>I 
can’t believe the price you pay<BR>Nothing can save you<BR><BR>Justice is 
lost<BR>Justice is raped<BR>Justice is gone<BR>Pulling your strings<BR>Justice 
is done<BR>Seeking no truth<BR>Winning is all<BR>Find it so grim<BR>So 
true<BR>So real<BR>
<BR>Apathy their stepping stone<BR>So unfeeling<BR>Hidden 
deep animosity<BR>So deceiving<BR>Through your eyes their light burns<BR>Hoping 
to find<BR>Inquisition sinking you<BR>With prying minds<BR>
<BR>Lady justice has been raped<BR>Truth 
assassin<BR>Rolls of red tape seal your lips<BR>Now you’re done in<BR>Their 
money tips her scales again<BR>Make your deal<BR>Just what is truth? i cannot 
tell<BR>Cannot feel<BR>

<BR>It’s high voltage you can’t shake the shock
<BR>Because nobody wants it to stop, check it out (4x)
<BR>
<BR>I’ve been taking into crates ever since I was livin’ in space
<BR>Before the rat-race, before monkeys had human traits
<BR>Mastered numerology and big-bang theology
<BR>Preformed lobotomies with telekinetic psychology
<BR>Invented the mic so I start blessin’ it
<BR>And chin-checkin’ kids to make my point like an impressionist
<BR>Many men have tried to shake us 
<BR>But I twist mic cords to double helixes and show them what I’m made of
<BR>I buckle knees like leg braces 
<BR>Cast the spell of instrumental-ness and all of the emcees that hate us
<BR>So try on, leave you without a shoulder to cry on
<BR>From now to infinity let icons be bygones
<BR>I fire bomb ghostly notes haunt this
<BR>I’ve tried threats but moved on to a promise
<BR>I stomp shit with or without an accomplish
<BR>(Mixed media)
<BR>The stamp of approval is on this
<BR>
<BR>Chorus (2x)
<BR>
<BR>Akira, put a kink in the backbones of clones with microphones
<BR>Never satisfy my rhyme jones
<BR>Sprayin’ bright day over what you might say
<BR>Blood type carillon 
<BR>Technicolor type A
<BR>On highways with road rage I’m patient to win
<BR>The cage and the tin to bounce all around
<BR>In surround sound devouring the scene
<BR>Subliminal gangrene paintings
<BR>Overall the same things sing songs karaoke copy madness
<BR>Break bones verbally to sticks and stone tactics 
<BR>Fourth dimension, combat convention 
<BR>Write rhymes at ease while the tracks stand at attention (Attention)
<BR>Meant to put you away with the pencil
<BR>Pistol, official, 16 line rhyme missile
<BR>Why you risk it all, I pick out of your flaws
<BR>Spin, blah-blah-blah-blah
<BR>You can say you saw
<BR>
<BR>Chorus (4x)
<BR>
<BR>Chorus (4x)
<BR>
<BR>

        -->
        
        <tr>
          <td align="right" colspan=2>
            <asp:Button id="btnDelete" runat="server" Text="Delete Selected" CausesValidation=False ></asp:Button></td>
        </tr>
        <!---->
      </table>
    </form>
  </body>
</HTML>

