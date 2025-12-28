# Implementa tu solución aquí

def existencias(ids:list[str]):
    existentes = set(["a_1", "a_2", "a_3", "b_1", "b_2", "b_4", "b_5", "b_8", 
        "c_3", "c_7", "c_9", "c_10", "c_11", "d_2", "d_3", "d_6", "d_8", 
        "d_9", "d_23", "d_35"])
    
    
    return sorted(list(existentes & set(ids)))