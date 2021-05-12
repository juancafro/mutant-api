from mutant_validation_core.dna_evaluation_exception import InvalidDnaSequenceError


def is_mutant_dna(dna_sequence: list):
    rows = len(dna_sequence)
    columns = len(dna_sequence[0])
    mutant_genes_counter = 0
    repeated_consecutive_gene_counter = 0
    is_mutant = False
    for i in range(rows):
        if len(dna_sequence[i]) != rows or len(dna_sequence[i]) != columns:
            raise InvalidDnaSequenceError("row and columns has differ in length")
        for j in range(columns):
            gene_pivot = dna_sequence[i][j]
            if not is_valid_sequence_char(gene_pivot):
                raise InvalidDnaSequenceError("there's a no valid char in the sequence")
            for increment in range(1, 4, 1):
                if j + increment >= columns:
                    break
                if gene_pivot != dna_sequence[i][j + increment]:
                    break
                repeated_consecutive_gene_counter = repeated_consecutive_gene_counter + 1
                if repeated_consecutive_gene_counter >= 3:
                    mutant_genes_counter += 1
            repeated_consecutive_gene_counter = 0
            for increment in range(1, 4, 1):
                if i + increment >= rows:
                    break
                if gene_pivot != dna_sequence[i + increment][j]:
                    break
                repeated_consecutive_gene_counter = repeated_consecutive_gene_counter + 1
                if repeated_consecutive_gene_counter >= 3:
                    mutant_genes_counter += 1
            repeated_consecutive_gene_counter = 0
            for increment in range(1, 4, 1):
                if i + increment >= rows or j - increment < 0:
                    break
                if gene_pivot != dna_sequence[i + increment][j - increment]:
                    break
                repeated_consecutive_gene_counter = repeated_consecutive_gene_counter + 1
                if repeated_consecutive_gene_counter >= 3:
                    mutant_genes_counter += 1
            repeated_consecutive_gene_counter = 0
            for increment in range(1, 4, 1):
                if i + increment >= rows or j + increment >= columns:
                    break
                if gene_pivot != dna_sequence[i + increment][j + increment]:
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


def is_valid_sequence_char(sequence_schar):
    return sequence_schar in {"A", "T", "C", "G"}
