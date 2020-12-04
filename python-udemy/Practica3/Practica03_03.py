tareas = [[6, 'Distribución'],[2, 'Diseño'],[1, 'Concepción'],[7, 'Mantenimiento'],[4, 'Producción'],[3, 'Planificación'],[5, 'Pruebas']]


print("--Tareas sin orden--")
for tarea in tareas:
    print(f"{tarea[0]}\t{tarea[1]}")

from collections import deque
tareas.sort()

print("print(tareas)")
print(tareas)

cola=deque()
for tarea in tareas:
    cola.append(tarea[1])

print(cola)