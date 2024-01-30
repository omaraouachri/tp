import pandas as pd
def encode_prenom(prenom: str) -> pd.Series:
    """
        This function encode a given name into a pd.Series.
        
        For instance alain is encoded [1, 0, 0, 0, 0 ... 1, 0 ...].
    """
    alphabet = "abcdefghijklmnopqrstuvwxyzé-'"
    prenom = prenom.lower()
    
    return pd.Series([letter in prenom for letter in alphabet]).astype(int)