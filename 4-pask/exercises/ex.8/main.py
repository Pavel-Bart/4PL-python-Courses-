
def unique_list(list):
  unq = []
  for x in list:
    if x not in unq:
      unq.append(x)
  return unq


print(unique_list([1,2,3,3,3,3,4,5]))