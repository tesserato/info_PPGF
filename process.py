import pandas as pd
from pandasgui import show
import yaml

converters={
  'DRE':int,
  'CPF':int
}

df = pd.read_excel("./0 Informacoes docentes e discentes.xlsx", "Discentes Ativos", converters=converters)

text = ""
for index, row in df.iterrows():
  text += f"{row['DRE']}_{row['Nome']}:\n"
  for e in row.items():
    if not pd.isna(e[1]):
      print(e[1], type(e[1]))
      text += f"  {e[0]}: {e[1]}\n"
  text += "\n"

  # print(row["DRE"])

# exit()

# # show(df)
# text = yaml.dump(
#   df.reset_index().to_dict(orient='records'),
#   sort_keys=False, 
#   width=72, 
#   indent=2,
#   default_flow_style=None
#   )

with open('01 alunos.yaml', 'w', encoding='utf8') as f:
  f.write(text)