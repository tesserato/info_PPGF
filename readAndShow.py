import pandas as pd
from pandasgui import show

converters={
  'DRE':int,
  'CPF':int
}

df = pd.read_excel("./0 Informacoes docentes e discentes.xlsx", "Discentes Ativos", converters=converters)



show(df)
