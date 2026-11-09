notas= [10,8,9,5]
#insertolista 
print(notas[1])
notas.append(20)
notas.insert(1,10)
print(len(notas))
print(max(notas))
print(min(notas))

print(notas[:2])

meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

print(meses[0])
print(meses[-1])
meses["martes"]="martes"



estudiante= {
    "cedula":"0151150076",
    "nombre": "luis",
    "correo":"luis@gmail.com",
    "cedular":"0999366496",
    "notas":[10,8,9,5]



}
print(estudiante["cedula"])
print(estudiante["nombre"])
print(estudiante["correo"])     

print(estudiante.get("nombre"))
print(estudiante.keys())

conjunto_a={"1","4","6","8"}
conjunti_b={"2","4","6","8"}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)


