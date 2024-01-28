#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:34:26 2023

@author: kakshay
"""
def check_and_process_files(inp_path, inp_bif, bofs, inp_res, bofs_num):
    set_id_fn_in = os.path.join(inp_path, "Schrauben/SET_ID_FN.in")
    
    if os.path.isfile(set_id_fn_in):
        text = "FNS.in found"
        # Set the text color to white on a green background
        formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
        print(formatted_text)
    else:
        print('''#---------------------------------------------------------#
        ERROR: 3
        
        SET_ID_FN.in or SET_ID_FNS.in not found.
        Please insert SET_ID in --> SET_ID_FN.in <--
        Syntax:
        3001
        3002
        3003
        WICHTIG bitte REIHENFOLGE BEACHTEN!!!
        #---------------------------------------------------------#''')
    
        sys.exit()
    
    # Read the contents of LF.in into lf_out
    lf_in_path = os.path.join(inp_path, "Schrauben/LF.in")
    with open(lf_in_path, 'r') as lf_in_file:
        lf_out = lf_in_file.read().splitlines()
    
    # Read the contents of SET_ID_FN.in into set_id_fn
    set_id_fn_path = os.path.join(inp_path, "Schrauben/SET_ID_FN.in")
    with open(set_id_fn_path, 'r') as set_id_fn_file:
        set_id_fn = set_id_fn_file.read().splitlines()
        
    
    # Read the contents of SET_ID_FNS.in into set_id_fns
    set_id_fns_path = os.path.join(inp_path, "Schrauben/SET_ID_FNS.in")
    with open(set_id_fns_path, 'r') as set_id_fns_file:
        set_id_fns = set_id_fns_file.read().splitlines()
    
    # Auswahl Bif & Bof
    # Text to append to the file
    text_to_append = f'''* * --------------- MEDINA PostProcessing 8.4.2.2 - Protocol -------------
* * Scripted Schraubenkraefte für Medina * *
ReadParam BOF_mode="merge" Read_rotations_DEFO_DEFOK_=ON _OK
ReadMod   "{inp_bif}"\n'''
    
    
    # Path to the output file
    output_file_path = os.path.join(inp_path, "FN_FNS.prot")
    
    # Append the text to the file
    with open(output_file_path, 'w') as output_file:
        output_file.write(text_to_append)
    
    # Append the ReadRes lines for each BOF file
    for bof in bofs:
        with open(os.path.join(inp_path, "FN_FNS.prot"), 'a') as prot_file:
            prot_file.write(f'ReadRes   "{bof}"\n')
    
    # Append the EShow and LF information
    with open(os.path.join(inp_path, "FN_FNS.prot"), 'a') as prot_file:
        prot_file.write('EShow\n  EMethod_sel="ID" EMode_sel="Direct"\n Eid=ALL\n')
    
    i = 0
    # Iterate over the lf_out array
    for lf in lf_out:
    
        print(f'Lastfall T = {lf}.0 ==> Lastfall RES = {int(lf) + 1}\n')
        
        # Append content to FN_FNS.prot
        with open(os.path.join(inp_path, "FN_FNS.prot"), 'a') as prot_file:
            
            # Text block to append
            text_block_1 = f'''RType/1
RSelect description_text="" Use_filters=OFF RSelIndexCol=ON RSelLoadCaseCol=ON
  RSelLoadIncrementCol=ON RSelLoadFactorCol=ON RSelLayerCol=ON
  RSelDescriptionCol=ON RSelCombineCol=ON RSelCAEKeyCol=ON RSelRecordCol=ON
  RSelAnaTypeCol=ON RSelLoCaTitleCol=ON RSelSourceCol=ON RSelNamF=""
  RSelWMode="Overwrite" RSelWriteDisplayed=ON RSelWriteCopy=OFF
  RSelResData="Selected" RSelXY="None" RSelWriShow="All" RSelLocalSys="Local"
  RSelMethod="Maximum" RSelFactor=1 RSelToggCom=ON
 CAE_key_sel=(208) Load_case_sel=({int(lf)+1}) Layer_sel=(0) Lincrement_sel=({int(lf)+1})
  file_id_sel=({i+2}) description_text_sel="Contact Force, Normal Direction"
  load_sel _OK\n'''
     
            prot_file.write(text_block_1)
            
            # Text block to append
            text_block_2 = f'''RCHNode Output_mode="LayoutElement" Representative_value="AbsMax"
  Result_filter="Summation" Extrema_filter="None" Limit=0 Limit2=0
  Output_options=ON RepValue=ON Node_Elem_result=OFF Node_ID=OFF Element_ID=ON
  Property_ID=OFF Node_coordinates=OFF Vector_components=ON
  Displacement_rotations=OFF Tensor_components=OFF Tensor_shear_components=OFF
  Principal_tensor_values_=ON Gap_force_opening=OFF Additional_data=OFF
  SPC_checking=OFF Force_checking=OFF Contact_force_opening=OFF Imaginary=OFF
  Real=OFF Magnitude=OFF Phase_angle=OFF Logfile_output=OFF File_output=ON
  General_information=OFF Significant_digits="3" Number_format="Decimal"
  Defined_symbol=";"
  RChFilename="{inp_path}/TEST.temp"
  Column_separation="Defined_symbol" Between_column="1"
  Defined_symbol=";"
 NMethod_sel="Set" NType_filter_sel="Any" NVisible_sel=OFF
  NBoundary=OFF NNeighbour_sel=OFF NNode_filter_sel=OFF PickThShaded=OFF
  NOperation_sel="Add" NFLocal_node_coord_system_sel=OFF
  NFLocal_node_coord_system_ID_sel=OFF NFLocal_node_coord_system_ID=0
  NFLocal_displ_coord_system_sel=OFF NFLocal_displ_coord_system_ID_sel=OFF
  NFLocal_displ_coord_system_ID=0 NFScalar_elements_sel=OFF NFMPC_nodes_sel=OFF
  NFSPC_nodes_sel=OFF NFNodal_forces_sel=OFF NFBar_beam_elements_sel=OFF
  NFWeldspot_elements_sel=OFF NFProperty_limits_sel=OFF NFLabel_sel=OFF
  NFLabel_text="*" NFNoLabel_sel=OFF NFBasNod_sel=OFF NFFiltermode="OR"
  NFSuperId=0 NFSuper_sel=OFF NFMaxDist=0 NFMaxDist_sel=OFF NGeo_dist_sel=0.1
 SetType_filter_sel="Node" SetSelectionFilter=OFF Check_sets_sel="No"
  SetSolverkey_filter_sel="Any" SetList_sel=ON SetLabel_filter_sel=""\n'''
            
            prot_file.write(text_block_2)
            
            prot_file.write(f' RChFilename="{inp_path}/FN.out"\n')
            
            for si_fn in set_id_fn:
                prot_file.write(f' Setid=({si_fn})\n')
            
            prot_file.write(f' RChFilename="{inp_path}/FNS.out"\n')
            
            for si_fns in set_id_fns:
                prot_file.write(f' Setid=({si_fns})\n')
            
            prot_file.write(' _OK\n')
            
          
            ### Mehrere BOFs Beta
            # Check the length of the bofs array
            if len(bofs) != 1:
                i += 1
    
    # Append the 'Quit' and '_OK' lines to FN_FNS.prot
    with open(os.path.join(inp_path, "FN_FNS.prot"), 'a') as prot_file:
        prot_file.write('Quit\n _OK\n')
    
    if len(sys.argv) < 3:
        text = "Batch-Mode starten? j/n"
        
        # Set the text color to white on a green background
        formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
        # Display a message with colored text
        user_input = input(f'{formatted_text}')
        
    else:
        user_input = "j"
    
    while True:
        if user_input.lower() == "j":
            print("Batch-Mode wird gestartet.")
            break
        
        elif user_input.lower() == "n":
            print("Exiting the program")
            sys.exit()
            
        else:
            text = "Invalid input. Batch-Mode starten? j/n"
    
            # Set the text color to white on a green background
            formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
            # Display a message with colored text
            user_input = input(f'{formatted_text}')
           
    
    # Define the paths
    source_path1 = os.path.expanduser("~/.medina/medpost84.userparm")
    destination_path1 = os.path.expanduser("~/.medina/medpost84.userparm_old")
    
    source_path2 = "/CAE/90_Lauer-Weiss/10_Know-How/03_Achsen_Berndt/Scripte_Protokolle/Schraubenkraefte/medpost84.userparm"
    destination_path2 = os.path.expanduser("~/.medina/medpost84.userparm")
    
    # Rename the existing userparm file to a backup file
    try:
        shutil.move(source_path1, destination_path1)
        print("Old userparm file renamed to medpost84.userparm_old.")
    except FileNotFoundError:
        print("Old userparm file not found, skipping renaming.")
    
    # Copy the new userparm file to the destination
    shutil.copy(source_path2, destination_path2)
    print("New userparm file copied to ~/.medina/medpost84.userparm.")
    
    if len(sys.argv) < 3: 
        text = "Continue with Batch-Mode? Enter 'j' for yes, 'n' to exit.: "
        
        # Set the text color to white on a green background
        formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
        
        # Read user input
        source = input(f'{formatted_text}')
    
    else:
        source = "j"
        
    while True:
        if source.lower() == "j":
            # Execute the medpost84 command
            cmd = "medpost84_8.4.2.2 prot={} inprot={} batch".format(
                os.path.join(inp_path, "dummy.prot"),
                os.path.join(inp_path, "FN_FNS.prot")
            )
            
            os.system(cmd)
        
            # Remove temporary files
            temp_files = [os.path.join(inp_path, "dummy.prot"), os.path.join(inp_path, "TEST.temp")]
            for temp_file in temp_files:
                try:
                    os.remove(temp_file)
                except FileNotFoundError:
                    pass  # Handle errors if the file doesn't exist
           
           # Replace dots with commas and remove lines starting with '#' in .out files
            out_files = glob.glob(os.path.join(inp_path, "*.out"))
    
            for out_file in out_files:
                with open(out_file, 'r') as file:
                    lines = file.readlines()
            
                modified_lines = [line.replace('.', ',') for line in lines if not line.startswith('#')]
            
                with open(out_file, 'w') as file:
                    file.writelines(modified_lines)
            
            print('.out files are modified.')
            break
                
        elif source.lower() == "n":
            print("Exiting the program.")
            sys.exit()
            
        else:
            source = input("Invalid input. Continue with Batch-Mode? Enter 'j' for yes, 'n' to exit.: ")
    
    # Check if the lengths of set_id_fn and set_id_fns lists are equal
    if len(set_id_fn) == len(set_id_fns):
        print("\033[30;102mEs sind gleich viele FN & FNS & EForce vorhanden\033[m")
    else:
        print("\033[97;41mACHTUNG: FNS & FN & EForce nicht gleichviele vorhanden!\033[m")
    
    
    def copy_file(src, dest):
        with open(src, 'rb') as source_file:
            with open(dest, 'wb') as destination_file:
                destination_file.write(source_file.read())
    
    # Copy FNS.out and FN.out to temporary files
    copy_file(os.path.join(inp_path, "FNS.out"), os.path.join(inp_path, "FNS_copy.temp"))
    copy_file(os.path.join(inp_path, "FN.out"), os.path.join(inp_path, "FN_copy.temp"))
    
    
    # Iterate over all files in the directory ending with "_copy.temp"
    for filename in os.listdir(inp_path):
        if filename.endswith("_copy.temp"):
            file_path = os.path.join(inp_path, filename)
    
            # Read the content of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
    
            # Modify the content by replacing only the second occurrence of ';'
            for i in range(len(lines)):
                line = lines[i]
                count = 0
                new_line = ''
                for char in line:
                    if char == ';':
                        count += 1
                        if count == 2:
                            new_line += '|'
                        else:
                            new_line += char
                    else:
                        new_line += char
                lines[i] = new_line
    
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)
                
    
    # Iterate over all files in the directory ending with "_copy.temp"
    for filename in os.listdir(inp_path):
        if filename.endswith("_copy.temp"):
            file_path = os.path.join(inp_path, filename)
    
            # Read the content of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Process each line to remove everything after the first '|'
            modified_lines = [line.split('|')[0] for line in lines]
            
            
            # Process each line to remove everything before and including the last '; '
            modified_content = [line.rsplit('; ', 1)[-1] for line in modified_lines]
            
            # Add newline character to each line
            modified_content = [line + '\n' for line in modified_content]
    
    
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(modified_content)
    
    # Read the content of FN_copy.temp into a list
    with open(inp_path + "/FN_copy.temp", 'r') as fn_file:
        fn = fn_file.readlines()   
        fn = [line.strip() for line in fn]
    
    # Read the content of FNS_copy.temp into a list
    with open(inp_path + "/FNS_copy.temp", 'r') as fns_file:
        fns = fns_file.readlines()
        fns = [line.strip() for line in fns]
    
    eforce = []
    
    with open(inp_path + "/EForce_NID_MON_ZUG_SCHUB.csv", 'r', newline='', encoding='utf-8') as eforce_file:
        csv_reader = csv.reader(eforce_file)
        
        for row in csv_reader:
            # Concatenate items in the row into a single string, removing double quotes
            row_string = ';'.join(item.strip('"') for item in row)
            eforce.append(row_string)
            
    # Initialize variables
    i = 0
    az = len(set_id_fn)
    
    # Create and write the header row to the CSV file
    with open(inp_path + "/FN_FNS_fin.csv", 'w') as csv_file:
        csv_file.write('FN_Mon;FN_Zug;FN_Sch;FNS_Mon;FNS_Zug;FNS_Sch;MONTAGE_Y;MONTAGE_Z;ZUG_Y;ZUG_Z;SCHUB_Y;SCHUB_Z;BALKEN_ID;SET_ID_FN;SET_ID_FNS\n')
    
    # Iterate through the arrays and write data to the CSV file
    with open(inp_path + "/FN_FNS_fin.csv", 'a') as csv_file:
        while i < len(set_id_fn):
            csv_file.write(f'{fn[i]};{fn[i+az]};{fn[i+az+az]};{fns[i]};{fns[i+az]};{fns[i+az+az]};{eforce[i+1]};{set_id_fn[i]};{set_id_fns[i]}\n')
            i += 1
    
    # Read the content of FN_FNS_fin.csv
    with open(inp_path + "/FN_FNS_fin.csv", 'r') as csv_file:
        lines = csv_file.readlines()
    
    # Remove spaces from each line
    cleaned_lines = [line.replace(' ', '') for line in lines]
    
    # Overwrite the file with the updated content
    with open(inp_path + "/FN_FNS_fin.csv", 'w') as csv_file:
        csv_file.writelines(cleaned_lines)
    
    
    #Postfix fuer CSV-Datei ueber Lastfall-Array
    # Generate the postfix
    #postfix = "LF"
    #for lf in lf_out:
        #postfix = postfix + "_" + lf
    
    # Define the original and new file paths
    original_file_path = os.path.join(inp_path, "FN_FNS_fin.csv")
    #new_file_path = os.path.join(inp_path, f"FN_FNS_fin_{postfix}.csv")
    
    # Rename the file with the new postfix
    #os.rename(original_file_path, new_file_path)
    
    # Open the edited file in a text editor
    editor_command = f"nedit {original_file_path}"
    os.system(editor_command)
    
    print('delete old files')
    
    #extensions_to_remove = ['.temp', '.out']
    #suffix_to_remove = '_start.res'
                
    # Remove additional files based on the debug variable
    if debug == 0:
        # Remove EForce_NID_MON_ZUG_SCHUB.csv
        eforce_csv_path = os.path.join(inp_path, "EForce_NID_MON_ZUG_SCHUB.csv")
        if os.path.exists(eforce_csv_path):
            os.remove(eforce_csv_path)
    
        # Remove FN_FNS.prot
        fn_fns_prot_path = os.path.join(inp_path, "FN_FNS.prot")
        if os.path.exists(fn_fns_prot_path):
            os.remove(fn_fns_prot_path)
            
    # userparm change to existing user file
    # Define the file paths
    userparm_path = os.path.expanduser("~/.medina/medpost84.userparm")
    userparm_old_path = os.path.expanduser("~/.medina/medpost84.userparm_old")
    
    # Remove the existing userparm file
    if os.path.exists(userparm_path):
        os.remove(userparm_path)
    
    # Rename the old userparm file to the current userparm file
    if os.path.exists(userparm_old_path):
        os.rename(userparm_old_path, userparm_path)
        
    print(f'''\033[30;102mWas wurde alles verwendet:\033[m
    Eforce.eforce: {inp_res}''')
    
    for lf in lf_out:
        print(f'Lastfall T = {int(lf)}.0 ==> Lastfall RES = {int(lf) + 1}')
    
    print(f'''BIF:		{inp_bif}
    anzahl der BOFs: {bofs_num}''')
    
    for bof in bofs:
        print(f"BOFs:		{bof}")
    
    print("\033[30;102mFertig Viel Spass damit\033[m")
    

print('''EFORCE EXPORT FOR EXCEL (BERNDT-AUSWERTUNG) code by jlink 20.08.2019
V1.3.2: Change directory for *.in files to ../tmp_ut/Schrauben/*.in for copy-package
ausgabe als CSV bei 3 Lastfaellen fuer Berndt-Schrauben-Auswertung
benoetigt:
--> EForce.eforce muss durch UCI PRINT Befehl erstellt sein
--> EForce_array.in mit den EID der Balken sortiert
--> LF.in mit den T=? der Lastfaelle
--> SET_ID_FN.in & SET_ID_FNS.in mit Set_IDs sortiert

Weitere Hilfe ist im Script (auskommentiert) enthalten!!!

#-----------------------------------------------------------------------------------#''')

# UCI FILE ANPASSEN!!!
# ACTIVE RESET
# PRINT
# PORT RES REPLACE FILE = EForce.eforce
# ITEM STRESS RESULTANTS
# PORT RES RESET

# Parameter
# debug = 0 => OFF
# debug = 1 => ON 
debug=1

import os
import sys
import subprocess
from colorama import init, Fore, Back, Style
# Initialize colorama
init()

files_eforce = [f for f in os.listdir(os.getcwd()) if f.endswith(".eforce")]

if len(sys.argv) < 3:
    # If no command-line argument is provided, list .eforce files in the current directory
    for file in files_eforce:
        print(os.path.join(os.getcwd(), file))
    
    # Text with custom color formatting
    text = "Pfad + EFroce-RES File"

    # Set the text color to white on a green background
    formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"

    # Read user input
    inp_res = input(f"{formatted_text}: ")

else:
    inp_res = os.path.join(os.getcwd(), files_eforce[0])

inp_file = os.path.splitext(inp_res)[0]
inp_path = os.path.dirname(inp_res)

print(f'''\naktueller Pfad
{inp_path}
Ausgewaehltes RES-File:
{inp_res}''')


if os.path.isfile(os.path.join(inp_path, 'Schrauben', 'EForce_array.in')):
    print("Schrauben/EForce_array.in found.")
else:
    print('''#--------------------------------------------------------#
    ERROR: 1
    
    Schrauben/EForce_array.in not found.
    Please insert EID of beams in --> EForce_array.in <--
    Syntax for EID = 1001 1002 1003 in file EForce_array.in
    1001
    1002
    1003
    WICHTIG bitte REIHENFOLGE BEACHTEN!!!
    Bitte EID der Balken in --> EForce_array.in <-- einfügen!
    #--------------------------------------------------------#''')

    sys.exit()
    
if os.path.isfile(os.path.join(inp_path, 'Schrauben', 'LF.in')):
    print("Schrauben/LF.in found.")
else:
    print('''#--------------------------------------------------------#
    ERROR: 2
    
    Schrauben/LF.in not found.
    Please insert EID of beams in --> LF.in <--
    Syntax for EID = 1001 1002 1003 in file LF.in
    1001
    1002
    1003
    WICHTIG bitte REIHENFOLGE BEACHTEN!!!
    Bitte EID der Balken in --> LF.in <-- einfügen!
    #--------------------------------------------------------#''')

    sys.exit()
    
print('alte Files loeschen')


import shutil

files_csv_txt= [
    os.path.join(inp_path, 'EForce_NID_MON_ZUG_SCHUB.csv'),
    os.path.join(inp_path, 'EForce_for_Excel.txt'),
    os.path.join(inp_path, 'array_Bereinigt.txt'),
    os.path.join(inp_path, 'test_array.txt'),
    os.path.join(inp_path, 'EForce_fin.txt')
]

for file in files_csv_txt:
    if os.path.exists(file):
        os.remove(file)

if os.path.exists(inp_res):
    shutil.copy(inp_res, inp_file + '_start.res')

    
beam_id = []
with open(os.path.join(inp_path, 'Schrauben', 'EForce_array.in'), 'r') as file:
    for line in file:
        beam_id.append(line.strip()) 
        
print(f'''
Es sind {len(beam_id)} Balken/EForce in der Auswertung vorhanden!
Gesuchte Elemente suchen
''')

with open(os.path.join(inp_path, 'test_array.txt'), 'a') as output_file:
    for i in beam_id:
        k = f"{int(i): #10d}"  # Convert to integer before formatting
        with open(inp_file + '_start.res', 'r') as input_file:
            for line_number, line in enumerate(input_file, start=1):
                if f'             Element No.{k}' in line:
                    output_file.write(f"{line_number}:{line}")
                    
print('Bearbeiten der txt fuer Weiterverarbeitung')

# Process text for further use
with open(os.path.join(inp_path, 'test_array.txt'), 'r') as file:
    test_array_lines = [line.split(':')[0] for line in file]

with open(os.path.join(inp_path, 'array_Bereinigt.txt'), 'w') as file:
    for line in test_array_lines:
        file.write(line + '\n')

print('Kraefte suchen und kopieren')  
      
# Search for forces and copy them
with open(os.path.join(inp_path, 'EForce_Export.txt'), 'w') as eforce_export_file:
    for a in test_array_lines:
        line_number = int(a) + 1
        with open(inp_res, 'r') as input_file:
            for current_line_number, line in enumerate(input_file, start=1):
                if current_line_number == line_number:
                    extracted_data = line[25:54]  # Extract characters from column 26 to 54
                    eforce_export_file.write(extracted_data + '\n')
            
NLast = len(test_array_lines) // len(beam_id)

print(f'''Anzahl der Lastfaelle im Res-File {NLast}
{len(test_array_lines)}
{len(beam_id)}
print({len(test_array_lines)}/{len(beam_id)})''', end=' ')

try:
    result = len(test_array_lines) / len(beam_id)
    print(f'= {result}')
    if result.is_integer():
        text = "-- Check for integer: Yes, Result is an Integer."

        # Set the text color to white on a green background
        formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
        print(f"{formatted_text}")
    else:
        print("Result is not an integer")
except ZeroDivisionError:
    print("Division by zero error")

print('Erstelle gesammtels File mit EID')


l = 0
source_file = os.path.join(inp_path, 'EForce_Export.txt')
dest_file_0 = os.path.join(inp_path, 'EForce_Export_0.txt')

# Copy the content of EForce_Export.txt to EForce_Export_0.txt
with open(source_file, 'r') as src, open(dest_file_0, 'w') as dest_0:
    dest_0.write(src.read())
        
while l < len(beam_id):
    eingabe = (l * (NLast + 1) + 1)
    dest_file_next = os.path.join(inp_path, f'EForce_Export_{l+1}.txt')
          
    try:
        # Use sed-like logic to modify the content of EForce_Export_$l.txt
        with open(f'EForce_Export_{l}.txt', 'r') as input_file:
            content = input_file.readlines()
            # Add beam_id[l] at line number eingabe
            content.insert(eingabe - 1, f"{beam_id[l]}\n")
            
            # Write the modified content to dest_file_next
        with open(dest_file_next, 'w') as output_file:
            output_file.writelines(content)
            
    except Exception as e:
        print(f"Error processing files for Beam_ID[{l}]: {e}")
                
    l += 1

# Rename the file
os.rename(os.path.join(inp_path, f'EForce_Export_{l}.txt'), os.path.join(inp_path, 'EForce_fin.txt'))

print('Ausgabe der Lastfaelle gesammelt LF.in')


# Read the contents of the LF.in file into a list
lf_out = []
with open(os.path.join(inp_path, 'Schrauben', 'LF.in'), 'r') as file:
    for line in file:
        lf_out.append(line.strip())

print('Anzahl der auszugeben Lastfaelle:', len(lf_out))


# Initialize an empty list to store the lines from the file
Eforce_all = []

# Concatenate the directory path and file name
eforce_fin_file_path = inp_path + '/' + "EForce_fin.txt"

# Open the file and read its contents line by line
with open(eforce_fin_file_path, 'r') as file:
    for line in file:
        Eforce_all.append(line.strip())

# Iterate through the LF_out list
for lf in lf_out:
    lf = int(lf)
    res_lf = int(lf + 1)
    print(f'Lastfall T = {lf:.1f} ==> Lastfall RES = {res_lf}')
       

n = 0
with open(os.path.join(inp_path, 'EForce_for_Excel.txt'), 'w') as output_file:
    with open(os.path.join(inp_path, 'EForce_fin.txt'), 'r') as input_file:
        lines = input_file.readlines()
        while n < len(beam_id):
            line_number_eid = n * (NLast + 1) + 1
            try:
                output_eid = lines[line_number_eid - 1]
                output_file.write(output_eid)
            except IndexError:
                pass  # Handle errors if the line number is out of bounds

            for lf in lf_out:
                line_number_lf = n * (NLast + 1) + (int(lf) + 2)
                try:
                    output_lf = lines[line_number_lf - 1]
                    output_file.write(output_lf)
                except IndexError:
                    pass  # Handle errors if the line number is out of bounds

            n += 1

# Replace '.' with ',' in the resulting EForce_for_Excel.txt file
with open(os.path.join(inp_path, 'EForce_for_Excel.txt'), 'r') as file:
    file_data = file.read()
    file_data = file_data.replace('.', ',')
with open(os.path.join(inp_path, 'EForce_for_Excel.txt'), 'w') as file:
    file.write(file_data)
    
### NEUE AUSGABE V1.1 ###

print('ACHTUNG AKTUELL NUR FUER 3 LASTFAELLE moeglich!')
print('fuer Berndt Auswertung mit Montage Zug Schub Lastfaellen')

# Read the contents of EForce_for_Excel.txt into a list
with open(inp_path + "/EForce_for_Excel.txt", 'r') as file:
    List_fin = file.read().splitlines()

n = 0
a = 0
csv_file_path = f"{inp_path}/EForce_NID_MON_ZUG_SCHUB.csv"

import csv

# Write header to CSV file
with open(csv_file_path, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['MONTAGE_Y', 'MONTAGE_Z', 'ZUG_Y', 'ZUG__Z', 'SCHUB_Y', 'SCHUB_Z', 'BALKEN_ID'])

    # Write data to CSV file
    for a in range(0, len(List_fin), 4):
        group = List_fin[a:a + 4]  # Extract a group of four items
        
        # Ensure that each item in the group contains two values
        for i in range(1, 4):
            values = group[i].split()
            if len(values) == 2:
                group[i] = values
            else:
                # Handle cases where there are not exactly two values
                group[i] = [group[i], '']

        # Write the group to the CSV file
        csv_writer.writerow([group[1][0], group[1][1], group[2][0], group[2][1], group[3][0], group[3][1], group[0]])
       
 ### ENDE NEUE AUSGABE ###

print('''
Alle temp-Daten loeschen


                   ''')

# List of files you want to remove
files_to_remove = [
    "array_Bereinigt.txt",
    "test_array.txt",
    "EForce_fin.txt",
    "EForce_for_Excel.txt"
]

 # Remove the specified files
for file in files_to_remove:
    file_path = os.path.join(inp_path, file)
    if os.path.exists(file_path):
        os.remove(file_path)

import glob        
# Remove files with the wildcard pattern
matching_files = glob.glob(os.path.join(inp_path, "EForce_Export*.txt"))
for file_path in matching_files:
    os.remove(file_path)
    
print(f'''#-----------------------------------------#
      
     
{inp_path}/EForce_NID_MON_ZUG_SCHUB.csv

#-----------------------------------------#
                                                    ''')
                                                    
                                                    
if len(sys.argv) < 3:                                                    
    # Text with custom color formatting
    text = "Weiter mit Batchmode j/n"
    
    # Set the text color to white on a green background
    formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
    
    # Read user input
    source = input(f"{formatted_text} j/n: ")
else:
    source = "j"
    
while True:
    if source.lower() == "j":
        print(formatted_text)
        break
    
    elif source.lower() == "n":
        file_path = os.path.join(inp_path, 'EForce_NID_MON_ZUG_SCHUB.csv')

        # Open the file with nano editor
        subprocess.run(['nano', file_path])
        sys.exit()
        
    else:
        source = input(f"Invalid input. {formatted_text} j/n: ")


################################################################################
# FNS & FN #
################################################################################

print('alte Files  Loeschen')

import glob 

# List of files to remove
files_to_remove = [
    "*.temp",
    "FNS.out",
    "FN.out",
    "FN_FNS_fin.csv",
    "FN_FNS.prot",
]

for file in files_to_remove:
    file_pattern = os.path.join(inp_path, file)
    for file in glob.glob(file_pattern):
        if os.path.exists(file):
            os.remove(file)

# List .bif files in the parent directory
bif_files = [f for f in os.listdir(os.path.dirname(inp_path)) if f.endswith('.bif')]

# Print the list of .bif files
print("List of .bif files:")
for bif_file in bif_files:
    full_path_bif = os.path.join(os.path.dirname(inp_path), bif_file)
    print(full_path_bif)


# Initialize colorama
init(autoreset=True)

if len(sys.argv) < 3: 
    # Define the text to be printed
    text = "Pfad + Model.BIF"
    
    # Set the text color to white on a green background
    formatted_text = f"{Style.BRIGHT}{Fore.WHITE}{Back.GREEN}{text}{Style.RESET_ALL}"
    
    # Prompt the user for input bif file
    inp_bif = input(f"{formatted_text}: ")

else:
    inp_bif = full_path_bif

bofs_num = len(lf_out)

# List .bof files in the directory
bof_files = [f for f in os.listdir(inp_path) if f.endswith('.bof')]

# Initialize an empty list to store BOF file paths
bofs = []

# Print the list of .bof files
print("List of .bof files:")

for i, bof_file in enumerate(bof_files):
    print(f"{i + 1}: {bof_file}")

# Define the original and new file paths
original_file_path = os.path.join(inp_path, "FN_FNS_fin.csv")
    
if len(sys.argv) < 3:
    # Prompt the user for BOF file paths
    for i in range(bofs_num):
        inp_model_bof = input(f"\nPlease enter the path for Model.BOF No. {i + 1} for evaluation (1-{len(bof_files)}): ")
        #inp_model_bof = i
        try:
            index = int(inp_model_bof) - 1  # Subtract 1 to adjust for 0-based indexing
            if 0 <= index < len(bof_files):
                bofs.append(os.path.join(inp_path, bof_files[index]))
            
            else:
                print("Invalid selection. Please enter a valid number.")
                i -= 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    check_and_process_files(inp_path, inp_bif, bofs, inp_res, bofs_num)
    
    postfix = "LF"
    for lf in lf_out:
        postfix = postfix + "_" + lf
        
    new_file_path = os.path.join(inp_path, f"FN_FNS_fin_{postfix}.csv")
    
    # Rename the file with the new postfix
    os.rename(original_file_path, new_file_path)
    sys.exit()

else:
    k = 0       
    while k <= (len(bof_files)-1)/2:
     
        bofs.append(os.path.join(inp_path, bof_files[k]))
        bofs.append(os.path.join(inp_path, bof_files[k+1]))
        bofs.append(os.path.join(inp_path, bof_files[k+2]))
        
        check_and_process_files(inp_path, inp_bif, bofs, inp_res, bofs_num)
        postfix = f'LF_0_{k+1}_{k+2}.csv'
        new_file_path = os.path.join(inp_path, f"FN_FNS_fin_{postfix}")
        
        # Rename the file with the new postfix
        os.rename(original_file_path, new_file_path)
        k +=2


    
########END##########