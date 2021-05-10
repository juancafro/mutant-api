
def is_mutant_dna(dna_sequence):
    rows = len(dna_sequence)
    columns = len(dna_sequence[0])
    mutant_genes_counter = 0
    repeated_consecutive_gene_counter = 0
    is_mutant = False
    for i in range(rows):
        for j in range(columns):
            gene_pivot = dna_sequence[i][j]
            for increment in range(1, 4, 1):
                if j + increment >= columns:
                    break
                if gene_pivot != dna_sequence[i][j + increment]:
                    break
                repeated_consecutive_gene_counter = repeated_consecutive_gene_counter + 1
                if repeated_consecutive_gene_counter >= 3:
                    mutant_genes_counter += 1
            repeated_consecutive_gene_counter = 0
            if mutant_genes_counter > 1:
                is_mutant = True
                break
        if is_mutant:
            break
    return is_mutant

