szavak = ['alma', 'bab','tó','telefon']

nagybetűs = list(
    map(lambda szavak: szavak.upper() if len(szavak) > 3 else szavak, szavak))

print("Eredeti lista:", szavak)
print("Generált lista nagybetűs formában:", nagybetűs)
