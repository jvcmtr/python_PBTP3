from tabulate import tabulate
from utils import load_csv, tables
from datetime import datetime

data = dt = load_csv()


def print_t(s):
  print(tabulate(s, tablefmt="grid"))


def q1():
  print("\n1. Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.")
  for t in tables:
    print(f"\n\n table: {t}")
    print_t(data[t])


def q2():
  print("\n2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.")
  funcionarios = []
  for func in data['funcionarios']:
    f = {}
    f["nome"] = func[1]
    f["cargo"] = [x[1] for x in data['cargos'] if x[0] == func[3]][0]
    f["departamento"] = [
        x[1] for x in data['departamentos'] if x[0] == func[4]
    ][0]
    f["dependentes"] = [x[1] for x in data['dependentes'] if x[4] == func[0]]
    funcionarios.append(f)

    print_t(funcionarios)


def q3():
  print("\n3. Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.")
  historico = [x for x in data['historico'] if x[2] > '2024-03-01']

  funcionarios_com_aumento = []
  func = {}
  for pg in historico:
    if func.get(pg[1]) is None:
      func[pg[1]] = pg[3]

    elif func[pg[1]] < pg[3]:
      funcionarios_com_aumento.append(pg[1])

  print_t([[x[1]] for x in data['funcionarios'] if x[0] in funcionarios_com_aumento])


def q4():
  print("\n4. Listar a média de idade dos filhos dos funcionários por departamento.")
  funcionario_dep = {}
  for f in data['funcionarios']:
    funcionario_dep[f[0]] = f[4]

  dep_filhos = {}
  for fil in data['dependentes']:
    if fil[3] != 'filho':
      continue
    
    departamento = funcionario_dep[fil[4]]
    
    if dep_filhos.get(departamento) == None:
      dep_filhos[departamento] = []
    
    idade = datetime.today().year - int(fil[2].split('-')[0])
    dep_filhos[departamento].append(idade)

  for k in dep_filhos.keys():
    dep_filhos[k] = sum(dep_filhos[k]) / len(dep_filhos[k])

  print_t([(x[1], dep_filhos[x[0]]) for x in data['departamentos']])


def q5():
  print("\n5. Listar qual estagiário possui filho.")
  id_estagiario = [x[0] for x in data['cargos'] if x[1] == 'gerente'][0]

  func_filhos = {}
  for f in data['dependentes']:
    if f[3] == 'filho':
      func_filhos[f[4]] = True

  estagiarios = [x for x in data['funcionarios'] if x[3] == id_estagiario]
  print_t([[x[1]] for x in estagiarios if x[0] in func_filhos.keys()])

q1()
q2()
q3()
q4()
q5()