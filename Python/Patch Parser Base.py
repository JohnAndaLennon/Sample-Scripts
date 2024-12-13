#############################################################
# Project: Patching Report Parser                           #
# Description: Scans a text file containing information for #
#  User, Device and Policy and writes the results in a      #
#  separate file. Applications are compared to remove same  #
#  entries for easier reading.                              #
# Version: 1.0                                              #
#############################################################

applications = []
potential_names = []
# Defines the current device and then appends it to the list
def parser():
    device_name = ""
    device_user = ""
    current_policy = ""
    
    # Reads through the lines and finds matching information
    for line in f.readlines(): 

        # Checks for name of new device  
        if line.startswith(("LAPTOP", "DEVICE", "PC", "TABLET", "WORKSTATION")): # ADD MORE HERE FOR TESTS
            try:
                device_info = line.split(" - ") # Naming Convention = 'DEVICE NAME - USER NAME'
                device_name = device_info[0]
                device_user = device_info[1]
            except:
                device_info = line.split("(") # Second Naming Convention = 'DEVICE NAME (OS INFO)'
                device_name = device_info[0]   
                device_user = ""
        
        elif line.startswith("Policy:") and 'No Policy Assigned' not in line: # Takes policy unless "No Policy Assigned", as it can end there
            current_policy = line.split(":")[1].strip()

        # 'Application' checks for what the app is and goes from there
        elif "Application" in line or "Available" in line: # Takes info from "Application NAME" or "Available Update"
            app_info = line.split(" ") # Line is "DD Month YY HH:MM Application NAME ..."
            app_name = " ".join(app_info[4:])
            if app_name not in applications: #If not currently stored in the array applications, store it
                applications.append(app_name)

        #Adds to end if it shows no patch events
        elif "No patch events" in line:
            applications.append(line)
       
        # Writes to the file "New Report" when on the last two line options
        elif 'patch events generated in the last 30 days' in line or 'No Policy Assigned' in line:
            try:
                current_policy = line.split(":")[1].strip()
            except:
                pass #Don't care otherwise
            g.write(device_name + ": " + device_user +  current_policy + "\n")
            for app in applications:
                g.write(app)
            g.write("\n")

            #Once everything is written, clears to prevent using previous information
            device_name = ""
            device_user = ""
            current_policy = ""
            applications.clear() #Clears Application for next item
        elif line.startswith('Organization Name - Section'):
            g.write(line)
#Opens the File and then sends it to the def
f = open("Patch Report.txt")
g = open("New Report.txt", "w")
parser()
