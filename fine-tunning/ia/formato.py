import json

dataa = {}
dataa['ia'] = []

with open('data.json') as file:
    data = json.load(file)

    for Carrera in data['Carreras']:
        nombre= Carrera['Nombre']
        prom= "Person: "+Carrera['Nombre']+"\n\n###\n\n"
        A = Carrera['Descripcion']
        StrA = "".join(A)
        
        B = Carrera['Modalidad']
        StrB = "".join(B)
        #print(StrB)
        #print(StrA)

        comple= "La carrera tiene como nombre "+Carrera['Nombre']+" Se encuentra en la modalidad de "+StrB+" Esta carrera se describe asi misma asi "+StrA+" El titulo con el obtiene sera "+Carrera['Titulo']+ " y tiene una duracuion de "+Carrera['Duracion']+"\n\n###\n\n" 

        dataa['ia'].append({'prompt': prom,'completion': comple})
        
        #print('First name:', Carrera['Nombre'])

with open('ia.json', 'w') as file:
    json.dump(dataa, file, indent=4)
