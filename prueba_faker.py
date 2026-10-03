from faker import Faker

# Inicializamos la herramienta (le ponemos 'es_CO' para que genere datos de Colombia)
fake = Faker('es_CO') 

print("Generando 3 clientes falsos:")
print("-" * 30)

# Usamos un ciclo simple para generar 3 registros
for _ in range(3):
    nombre = fake.name()
    correo = fake.email()
    ciudad = fake.city()
    print(f"Nombre: {nombre} | Correo: {correo} | Ciudad: {ciudad}")