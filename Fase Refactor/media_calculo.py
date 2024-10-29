def calcula_media(nota1, nota2, nota3):
    # Verifica se todas as notas são numéricas
    if not all(isinstance(nota, (int, float)) for nota in [nota1, nota2, nota3]):
        raise ValueError("Todas as notas devem ser números.")
    
    return (nota1 + nota2 + nota3) / 3