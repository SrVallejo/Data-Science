import warnings
warnings.filterwarnings("ignore")
import pandas as pd
df = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Municipios_de_Espa%C3%B1a_por_poblaci%C3%B3n', header=0)
print(len(df))

print(df)