ligands_directory="erDecoy-ago_pdbqt"
output_directory="erDecoy-ago_log"
receptor_path="3ert.pbdqt"
config_directory="config-3ert.txt"
iterations=1
for ligand_path in "$ligands_directory"/*
do
    ligand_name=$(basename "$ligand_path" | cut -f1 -d '.')
    # Create output directory if it doesn't exist
    mkdir -p "$output_directory/$ligand_name"

    # Create an empty log file
    echo -e "\n" > "$output_directory/$ligand_name/LOG.txt"
    for ((i=1; i<=iterations; i++))
    do
        ./vina --receptor "$receptor_path" --ligand "$ligand_path" --config "$config_directory" --cpu 36 --exhaustiveness 10 --num_modes 10 --out "$output_directory/$ligand_name/${i}_out.pdbqt" --energy_range 20 >> "$output_directory/$ligand_name/LOG.txt"
    done
done
