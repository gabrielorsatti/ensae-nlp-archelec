import pandas as pd

# Télécharger les métadonnées directement depuis le site Archelec
url_metadata = "https://archelec.sciencespo.fr/export/csv"  
metadata = pd.read_csv(url_metadata, sep=';')
metadata.to_csv('../data/archelec_metadata.csv', index=False)
