   _____        _____ _            
  |  __ \      / ____| |           
  | |  | |_  __ (___ | |_ ___ _ __ 
  | |  | \ \/ /\___ \| __/ _ \ '__|
  | |__| |>  < ____) | |_  __/ |   
  |_____//_/\_\_____/ \__\___|_| 

# dxster

DxSter, the Alzheimer's Algorithmic Diagnostic Helper.

The DxSter module takes a Clincal  diagnosis (PhyDx) and the Neurophyscological diagnosis (NpDx) to output the algorithmic diagnosis (AlgDx). The idea is that the AlgDx saves time to formulate a diagnosis of an ALZ patient but reducing the need for consensus conferences.

#TODO: Add literature cited.

#TODO Write about the programing language selected to accomplish the calculation

#TODO Write about the 1Florida ADRC data source form to acquire NDX and PhyDX for the calculator


#INFO: settings.conf.example
You must have a settings.conf file. to create one copy the example. This file is
in the .gitignore. Secrets, like db config details, are meant to be in the settings.conf file DO NOT commit them to the repo and DO NOT REMOVE settings.conf from the .gitigore.

# INFO: Makefile.conf
This file is used to configure the developer tasks
defined in the Makefile, IE deployment and automation info NOT app settings.
to define app settings, like db config info, use the settings.conf file.
