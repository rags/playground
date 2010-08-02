using System;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.ComponentModel;
using System.Drawing;

[assembly: TagPrefix("RND.CutomControls","RagsLogin")]//to be included in assemblyinfo.cs....
namespace RND.CutomControls
{
    /// <summary>
    /// Summary description for LoginControl.
    /// </summary>
    
    [ToolboxData("<{0}:LoginControl runat='server'>Login Title</{0}:LoginControl>"),
    DefaultEvent("OnLogin"),ToolboxBitmap(typeof(LoginControl),"Pencil.bmp")	
    ]
    public class LoginControl : Control, INamingContainer,IPostBackEventHandler  //, IPostBackDataHandler 
    {
        private string userNameTxt = "Username: ",loginTxt = "Login";
        public void OnInit(object sender,EventArgs e)
        {
            userNameTxt = "Username: ";
            loginTxt = "Login";
            ViewState["pwdTxt"] = "Password: ";
        }

        //LoginControl1.UserNameText = "abcd";  or   <logincontrol UserNameText="user" .... works fine
        //but if(!IsPostback) LoginControl1.UserNameText = "abcd";  wont work. value not persisted
        public string UserNameText
        {            
            get{return userNameTxt;}
            set{userNameTxt = value;}
        }

        //note that this property can be assigned dynamically from code behind and the value will persist on postback
        //ex: if(!IsPostback) LoginControl1.PasswordText = "abcd";  
        public string PasswordText
        {
            get{return ViewState["pwdTxt"] as string;}
            set{ViewState["pwdTxt"] = value;}
        }
        public string LoginText
        {
            get{return loginTxt;}
            set{loginTxt = value;}
        }
        public delegate void Login(string userName,string password);
        private Login loginEvent;
        private Login adminLoginEvent;
        public event Login OnLogin
        {
            add
            {
                loginEvent += value;
            }
            remove
            {
                loginEvent -= value; 
            }
        }
        
        public event Login OnAdminLogin
        {
            add
            {
                adminLoginEvent += value;
            }
            remove
            {
                adminLoginEvent -= value; 
            }
        }

        protected override void CreateChildControls()
        {      
            string header =((LiteralControl) Controls[0]).Text;
            Controls.Clear();
            HtmlTable table = new HtmlTable();
            HtmlTableRowCollection rows = table.Rows;
            HtmlTableRow tr;      
            HtmlTableCellCollection cells;
            HtmlTableCell td;
            HtmlInputText txtBox;
            HtmlInputButton btn;
      
            rows.Add(tr=new HtmlTableRow());
            cells=tr.Cells;
            cells.Add(td = new HtmlTableCell());
            td.Align="center";
            td.ColSpan=2;
            td.InnerHtml=header;

            rows.Add(tr = new HtmlTableRow());
            cells=tr.Cells;
            cells.Add(td = new HtmlTableCell());
            td.Style.Add("Font-weight","bold");
            td.InnerText=userNameTxt;
            cells.Add(td = new HtmlTableCell());      
            td.Controls.Add(txtBox=new HtmlInputText());
            txtBox.ID="txtName";

            rows.Add(tr=new HtmlTableRow());
            cells=tr.Cells;
            cells.Add(td=new HtmlTableCell());      
            td.Style.Add("Font-weight","bold");
            td.InnerText=PasswordText;
            cells.Add(td = new HtmlTableCell());      
            td.Controls.Add(txtBox=new HtmlInputText("password"));
            txtBox.ID="txtPwd";

            rows.Add(tr=new HtmlTableRow());
            cells=tr.Cells;
            cells.Add(td = new HtmlTableCell());
            td.InnerHtml += "<button onclick=\"" + Page.GetPostBackEventReference(this,"AdminLogin") + "\">Admin Login</button>";
            cells.Add(td = new HtmlTableCell());
            //td.Align="center";
            //td.ColSpan=2;
            td.Controls.Add(btn=new HtmlInputButton("submit"));
            btn.ID="btnLogin";
            btn.Value=loginTxt;
            btn.ServerClick +=new EventHandler(btn_ServerClick); 
            this.Controls.Add(table);
        }

        private void btn_ServerClick(object sender, EventArgs e)
        {
            EnsureChildControls();
            loginEvent(((HtmlInputText)this.FindControl("txtName")).Value,((HtmlInputText)this.FindControl("txtPwd")).Value);
        }
        void IPostBackEventHandler.RaisePostBackEvent(string args)        
        {
            if("AdminLogin".Equals(args))
            {
                adminLoginEvent(((HtmlInputText)this.FindControl("txtName")).Value,((HtmlInputText)this.FindControl("txtPwd")).Value);
            }
        }
    }
}