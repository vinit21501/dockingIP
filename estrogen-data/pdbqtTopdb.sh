
ligands_directory=""

for pdbFile in *
do
    obabel -ipdbqt "$pdbFile/1_out.pdbqt" -opdb -O"$pdbFile/$pdbFile.pdb"
done
