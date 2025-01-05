# Enumerate es una función en python que se usa para agregarle un contador a un iterable.
lenguajes={'Python','Ruby','Rust','Perl'}
for i,nombre in enumerate(lenguajes):
    print(f"{i}. {nombre}")