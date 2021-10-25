from operator import itemgetter

class Cond:
 def __init__(self, id, name):
  self.id = id
  self.name = name

class Orch:
 def __init__(self, id, type, number, id_cond):
  self.id = id
  self.type = type
  self.number = number
  self.id_cond = id_cond

class Orch_Cond:
 def __init__(self, id_orch, id_cond):
  self.id_orch = id_orch
  self.id_cond = id_cond

Conductor = [
 Cond(1, 'Leonard Bernstein'),
 Cond(2, 'Claudio Abbado'),
 Cond(3, 'Herbert von Karajan'),
 Cond(4, 'Nikolaus Harnoncourt'),
 Cond(5, 'Simon Rattle'),
 Cond(6, 'Wilhelm Furtwangler'),
]

Orchestra = [
 Orch(1, 'Symphony Orchestra', 38, 2),
 Orch(2, 'Brass band', 40, 2),
 Orch(3, 'Military band', 75, 1),
 Orch(4, 'String Orchestra', 93, 1),
 Orch(5, 'Folk Instruments Orchestra', 56, 5),
 Orch(6, 'Variety orchestra', 123, 4),
 Orch(7, 'Jazz orchestra', 30, 6),
 Orch(8, 'School Orchestra', 5, 1),
]

Orchestra_Conductor = [
 Orch_Cond(1, 2),
 Orch_Cond(2, 2),
 Orch_Cond(3, 1),
 Orch_Cond(4, 1),
 Orch_Cond(5, 2),
 Orch_Cond(6, 1),
 Orch_Cond(7, 3),
 Orch_Cond(8, 1),
 Orch_Cond(1, 5),
 Orch_Cond(2, 5),
 Orch_Cond(3, 4),
 Orch_Cond(4, 4),
 Orch_Cond(5, 5),
 Orch_Cond(6, 4),
 Orch_Cond(7, 6),
 Orch_Cond(8, 4),
]

def main():
  one_to_many = [(orch.type, orch.number, cond.name)
   for orch in Orchestra
   for cond in Conductor
   if orch.id_cond == cond.id]

  many_to_many_temp = [(cond.name, orch_cond.id_orch, orch_cond.id_cond)
   for cond in Conductor
   for orch_cond in Orchestra_Conductor
   if cond.id == orch_cond.id_cond]

  many_to_many = [(orch.type, cond_name)
   for cond_name, id_orch, id_cond in many_to_many_temp
   for orch in Orchestra if orch.id == id_cond]

  print('\n\nЗадание В1')
  res = list(filter(lambda i: str(i[0]).startswith('S'), one_to_many))
  res = [
   (elem[0], elem[2])
   for elem in res
  ]
  print(res)

  print('\n\nЗадание В2')
  res = sorted(one_to_many, key=itemgetter(1))
  res = [
   (elem[2], elem[1])
   for elem in res
  ]
  print(res)

  print('\n\nЗадание В3')
  res = sorted(many_to_many, key=itemgetter(0))
  print(res)
  print('\n\n')

if __name__ == '__main__':
  main()