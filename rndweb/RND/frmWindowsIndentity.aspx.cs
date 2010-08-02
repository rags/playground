using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Web;
using System.Web.SessionState;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.HtmlControls;
using System.Runtime.InteropServices;
using System.Security.Principal;
using System.Security.Permissions;

[assembly:SecurityPermissionAttribute(SecurityAction.RequestMinimum, UnmanagedCode=true)]
[assembly:PermissionSetAttribute(SecurityAction.RequestMinimum, Name = "FullTrust")]
namespace RND
{
	/// <summary>
	/// Summary description for frmWindowsIndentity.
	/// </summary>
    
	public class frmWindowsIndentity : System.Web.UI.Page
	{
        [DllImport("advapi32.dll", SetLastError=true)]
        public static extern bool LogonUser(String lpszUsername, String lpszDomain, String lpszPassword, 
            int dwLogonType, int dwLogonProvider, ref IntPtr phToken);

        [DllImport("kernel32.dll", CharSet=System.Runtime.InteropServices.CharSet.Auto)]
        private unsafe static extern int FormatMessage(int dwFlags, ref IntPtr lpSource, 
            int dwMessageId, int dwLanguageId, ref String lpBuffer, int nSize, IntPtr *Arguments);

        [DllImport("kernel32.dll", CharSet=CharSet.Auto)]
        public extern static bool CloseHandle(IntPtr handle);

        [DllImport("advapi32.dll", CharSet=CharSet.Auto, SetLastError=true)]
        public extern static bool DuplicateToken(IntPtr ExistingTokenHandle, 
            int SECURITY_IMPERSONATION_LEVEL, ref IntPtr DuplicateTokenHandle);
        public enum LogonType : int
        {
            LOGON32_LOGON_INTERACTIVE = 2,
            LOGON32_LOGON_NETWORK = 3,
            LOGON32_LOGON_BATCH = 4,
            LOGON32_LOGON_SERVICE = 5,
            LOGON32_LOGON_UNLOCK = 7,
            LOGON32_LOGON_NETWORK_CLEARTEXT = 8, // Only for Win2K or higher
            LOGON32_LOGON_NEW_CREDENTIALS = 9 // Only for Win2K or higher
        }
        public enum LogonProvider : int
        {
            LOGON32_PROVIDER_DEFAULT = 0,
            LOGON32_PROVIDER_WINNT35 = 1,
            LOGON32_PROVIDER_WINNT40 = 2,
            LOGON32_PROVIDER_WINNT50 = 3
        }

        // GetErrorMessage formats and returns an error message
        // corresponding to the input errorCode.
        public unsafe static string GetErrorMessage(int errorCode)
        {
            int FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x00000100;
            int FORMAT_MESSAGE_IGNORE_INSERTS = 0x00000200;
            int FORMAT_MESSAGE_FROM_SYSTEM  = 0x00001000;

            //int errorCode = 0x5; //ERROR_ACCESS_DENIED
            //throw new System.ComponentModel.Win32Exception(errorCode);

            int messageSize = 255;
            String lpMsgBuf = "";
            int dwFlags = FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS;

            IntPtr ptrlpSource = IntPtr.Zero;
            IntPtr prtArguments = IntPtr.Zero;
        
            int retVal = FormatMessage(dwFlags, ref ptrlpSource, errorCode, 0, ref lpMsgBuf, messageSize, &prtArguments);
            if (0 == retVal)
            {
                throw new Exception("Failed to format message for error code " + errorCode + ". ");
            }

            return lpMsgBuf;
        }

		[PermissionSetAttribute(SecurityAction.Demand, Name = "FullTrust")]
        private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            IntPtr tokenHandle = new IntPtr(0);
            IntPtr dupeTokenHandle = new IntPtr(0);
            try
            {
                string userName, domainName;
                // Get the user token for the specified user, domain, and password using the 
                // unmanaged LogonUser method.  
                // The local machine name can be used for the domain name to impersonate a user on this machine.                
                domainName = "nousblr";
                userName = "raghunandanr";
                const int SecurityImpersonation = 2;
                tokenHandle = IntPtr.Zero;
                dupeTokenHandle = IntPtr.Zero;

                // Call LogonUser to obtain a handle to an access token.
                bool returnValue = LogonUser(userName, domainName, "creed", (int)LogonType.LOGON32_LOGON_NETWORK 
                    ,(int) LogonProvider.LOGON32_PROVIDER_DEFAULT,
                    ref tokenHandle);
                    
                Response.Write("LogonUser called.");
                
                if (false == returnValue)
                {
                    int ret = Marshal.GetLastWin32Error();
                    Response.Write("LogonUser failed with error code : "+ ret);
                    Response.Write("\nError: ["+ret+"] "+GetErrorMessage(ret)+"<br>" );
                    int errorCode = 0x5; //ERROR_ACCESS_DENIED
                    throw new System.ComponentModel.Win32Exception(errorCode);
                }

                Response.Write("Did LogonUser Succeed? " + (returnValue? "Yes" : "No"));
                Response.Write("Value of Windows NT token: " + tokenHandle);

                // Check the identity.
                Response.Write("Before impersonation: "
                    + WindowsIdentity.GetCurrent().Name);

                bool retVal = DuplicateToken(tokenHandle, SecurityImpersonation, ref dupeTokenHandle);
                if (false == retVal)
                {
                    CloseHandle(tokenHandle);
                    Response.Write("Exception thrown in trying to duplicate token.");        
                    return;
                }
            
                // The token that is passed to the following constructor must 
                // be a primary token in order to use it for impersonation.
                WindowsIdentity newId = new WindowsIdentity(dupeTokenHandle);
                WindowsImpersonationContext impersonatedUser = newId.Impersonate();

                // Check the identity.
                Response.Write("After impersonation: "
                    + WindowsIdentity.GetCurrent().Name);
        
                // Stop impersonating the user.
                impersonatedUser.Undo();

                // Check the identity.
                Response.Write("After Undo: " + WindowsIdentity.GetCurrent().Name);
            
                // Free the tokens.
                if (tokenHandle != IntPtr.Zero)
                    CloseHandle(tokenHandle);
                if (dupeTokenHandle != IntPtr.Zero) 
                    CloseHandle(dupeTokenHandle);
            }
            catch(Exception ex)
            {
                Response.Write("Exception occurred. " + ex.Message);
            }            
		}

		#region Web Form Designer generated code
		override protected void OnInit(EventArgs e)
		{
			//
			// CODEGEN: This call is required by the ASP.NET Web Form Designer.
			//
			InitializeComponent();
			base.OnInit(e);
		}
		
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{    
			this.Load += new System.EventHandler(this.Page_Load);
		}
		#endregion
	}
}
