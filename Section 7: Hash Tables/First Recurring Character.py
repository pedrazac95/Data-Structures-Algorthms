def firstRecurringCharacter (array:list) -> int:
  resultado = "undefined"
  table = {}
  for fish in array:
      
                   
      if table.get(fish) == 1: 
          resultado = fish
          break                     
      else:
          table[fish] = 1
  #return resultado
  print (resultado, 'result')

array = [2,1,1,0,3,8,11,9,4]
firstRecurringCharacter(array)
