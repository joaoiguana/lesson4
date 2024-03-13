benfica = ["trubin", "bah", "a silva", "otamendi", "aursnes", "j neves", "florentino", "kokcu", "neres", "rafa", "m leonardo"]
print(benfica)

benfica.pop(-1)
benfica.append("a cabral")

print(benfica)

benfica.remove("neres")
benfica.insert(8, "di maria")

print(benfica)

goalkeeper = benfica[0]
defense = benfica[1:5]
midfield = benfica[6:8]
attack = benfica[8:]

print("goalkeeper:", goalkeeper)
print("defense:", ' '.join(defense))
print("midfield:", ' '.join(midfield))
print("attack:", ' '.join(attack))

staff = ('roger schimdt', 'rui costa')
coach, president = staff

print("coach:", coach)

