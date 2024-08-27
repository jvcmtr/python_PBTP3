from tabulate import tabulate
import sqlite3

def querie(s):
  cursor.execute(s)
  print(tabulate(cursor.fetchall(), tablefmt="grid"))

def q6():
  print("\n6. Listar o funcionário que teve o salário médio mais alto." )
  querie("""
    SELECT f.nome, AVG(h.pagamento) FROM funcionarios f 
      JOIN historico h ON f.id = h.funcionario_id
    GROUP BY f.id
    ORDER BY AVG(h.pagamento) DESC
      LIMIT 1
   """)

def q7():
  print("\n7. Listar o analista que é pai de 2 (duas) meninas." )
  querie("""
    SELECT f.nome , c.nome FROM funcionarios f
      JOIN dependentes d ON f.id = d.funcionario_id
      JOIN cargos c ON f.cargo_id = c.id
    GROUP BY f.id
    HAVING COUNT(d.parentesco) = 2 
      AND c.nome = 'analista' 
      AND d.genero = 'f'
  """)

def q8():
  print("\n8. Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000." )

  querie("""
    SELECT f.nome , c.nome, f.salario 
    FROM funcionarios f
      JOiN cargos c ON f.cargo_id = c.id
    WHERE c.nome = 'analista'
      AND f.salario BETWEEN 5000 AND 9000
    ORDER BY f.salario DESC
      LIMIT 1
  """)

def q9():
  print("\n9. Listar qual departamento possui o maior número de dependentes." )
  querie("""
    SELECT d.nome, COUNT(d2.id) FROM departamentos d
      JOIN funcionarios f ON d.id = f.departamento_id
      JOIN dependentes d2 ON f.id = d2.funcionario_id
    GROUP BY d.id
    ORDER BY COUNT(d2.id) DESC
      LIMIT 1
  """)

def q10():
  print("\n10. Listar a média de salário por departamento em ordem decrescente") 
  querie("""
    SELECT d.nome, AVG(f.salario) FROM departamentos d
      JOIN funcionarios f ON d.id = f.departamento_id
    GROUP BY d.id
    ORDER BY AVG(f.salario) DESC
  """)

conection = sqlite3.connect("db/empresa.db")
cursor = conection.cursor()
q6()
q7()
q8()
q9()
q10()
cursor.close()
conection.close()
