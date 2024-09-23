def createComplex(receptor_path, ligand_path):
    with open(receptor_path) as f:
        receptor = f.readlines()
    with open(ligand_path) as f:
        ligand = f.readlines()
    ligand_cleand = []
    for line in ligand:
        if line[:4] == "ATOM":
            ligand_cleand.append(line)
        elif line[:6] == "CONECT":
            break
        #     ligand_cleand.append(line)
        # elif line[:6] == "MASTER":
        #     ligand_cleand.append(line)
        # # elif line[:6] == "CONECT" or line[:6] == "MASTER" or line[:6] == "ENDMDL":
        # elif line[:6] == "ENDMDL":
        #     ligand_cleand.append("END\n")
        #     break
    with open(ligand_path[:-4] + '_complex.pdb', 'w') as f:
        f.writelines(receptor + ligand_cleand)

import os
universalPath = './'
receptor1 = universalPath + "3ert_edited.pdb"
receptor2 = universalPath + "1gwq_a_edited.pdb"

receptor1LogFoldersPath = ['erDecoy-ant_log', 'erLigand-ant_log']
receptor2LogFoldersPath = ['erDecoy-ago_log', 'erLigand-ago_log']

for logFolder in receptor1LogFoldersPath:
    for ligand in os.listdir(universalPath + logFolder):
        if ligand[:4] == "ZINC":
            createComplex(receptor1, f'{universalPath}{logFolder}/{ligand}/{ligand}.pdb')

for logFolder in receptor2LogFoldersPath:
    for ligand in os.listdir(universalPath + logFolder):
        if ligand[:4] == "ZINC":
            createComplex(receptor2, f'{universalPath}{logFolder}/{ligand}/{ligand}.pdb')
