n = int(raw_input().strip())
vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
pattern = map(int, raw_input().strip().split())

isPattern = True

for i in range(n):
  count = 0
  for token in raw_input().strip().split():
    filterVowels = filter(lambda x: x in vowels, token)
    count += len(filterVowels)
  if count != pattern[i]:
    isPattern = False
    break

print('YES' if isPattern else 'NO')
