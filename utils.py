import csv

tables = ['funcionarios', 'departamentos', 'cargos', 'historico', 'dependentes']

def load_csv():
  dt = {}
  for t in tables:
    with open(f"data/{t}.csv", "r") as file:
      reader = csv.reader(file)
      dt[t] = [x for x in reader]
  return dt
