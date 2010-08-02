using System;
using System.Collections;
using System.ComponentModel;
using System.Configuration.Install;


    /// <summary>
    /// Summary description for ServerInstaller.
    /// </summary>
    [RunInstaller(true)]
    public class ServerInstaller : System.Configuration.Install.Installer
    {
        private System.ServiceProcess.ServiceProcessInstaller serviceProcessInstaller1;
        private System.ServiceProcess.ServiceInstaller serviceInstaller1;
        /// <summary>
        /// Required designer variable.
        /// </summary>
        //private System.ComponentModel.Container components = null;

        public ServerInstaller()
        {
            // This call is required by the Designer.
            InitializeComponent();

            // TODO: Add any initialization after the InitComponent call
        }

		#region Component Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.serviceProcessInstaller1 = new System.ServiceProcess.ServiceProcessInstaller();
            this.serviceInstaller1 = new System.ServiceProcess.ServiceInstaller();
            // 
            // serviceProcessInstaller1
            // 
            this.serviceProcessInstaller1.Password = null;//"";
            this.serviceProcessInstaller1.Username = null;//"nousblr/raghunandanr";
            // 
            // serviceInstaller1
            // 
            this.serviceInstaller1.ServiceName = "MyServer";
            // 
            // ServerInstaller
            // 
            this.Installers.AddRange(new System.Configuration.Install.Installer[] {
                                                                                      this.serviceProcessInstaller1,
                                                                                      this.serviceInstaller1});

        }
		#endregion
    }



