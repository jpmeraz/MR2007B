import pandas as pd
import math

ruta_archivo = "C:/Users/jpmeraz/Downloads/JPinalFinalahorasibueno_bueno.txt"
datos = pd.read_csv(ruta_archivo, delimiter=";")
df = datos.drop(datos.columns[1], axis=1)
df = pd.DataFrame(df).apply(lambda x: x.str.split())

# Expander arrays en celdas a distintas columnas
df = pd.DataFrame([item for col in df.columns for item in df[col].values.ravel()])
df = df.fillna("Blank")

# Mapeamos los códigos de los diferentes procesos a un dataframe distinto
careado_df = df.iloc[11:16]
escalonado_df = df.iloc[27:53]
barrenado_df = df.iloc[65:68]
grabado_df = df.iloc[79:452]

#Tratamos los datos faltantes
#Careado
temp_df = careado_df
for index, row in temp_df.iterrows():
  if "Y" in row[2]:
    temp_df.at[index, 3] = row[2]
    temp_df.at[index, 2] = "X0"
  elif "Blank" in row[2]:
    temp_df.at[index, 3] = "Y0"
  elif "Blank" in row[3]:
    temp_df.at[index, 3] = "Y0"
  if "Z" in row[2]:
    temp_df.drop(index)

#Grabado
temp_df = grabado_df
for index, row in temp_df.iterrows():
  if "Y" in row[2]:
    temp_df.at[index, 3] = row[2]
    temp_df.at[index, 2] = "X0"
  elif "Blank" in row[2]:
    temp_df.at[index, 3] = "Y0"
  elif "Blank" in row[3]:
    temp_df.at[index, 3] = "Y0"
  if "Z" in row[2]:
    temp_df.drop(index)

#Escalonado
temp_df = escalonado_df
for index, row in temp_df.iterrows():
  if "Y" in row[2]:
    temp_df.at[index, 3] = row[2]
    temp_df.at[index, 2] = "X0"
  elif "Blank" in row[2]:
    temp_df.at[index, 3] = "Y0"
  elif "Blank" in row[3]:
    temp_df.at[index, 3] = "Y0"
  if "Z" in row[2]:
    temp_df.drop(index)


#Funciones para cálculo de variables de proceso
def velocidad_corte(diametro, vc):
    return vc * 1000 / (diametro * math.pi)

def velocidad_de_avance(z, diametro, vc, an):
    return z * an * velocidad_corte(diametro, vc)

def variables_de_corte(diametro, vc, f, z, an):
    print(f"Diametro de la fresa: {diametro} mm")
    print(f"Velocidad de corte: {velocidad_corte(diametro, vc):.2f} rpm")
    print(f"Velocidad de corte con 30% de factor de potencia: {velocidad_corte(diametro, vc)*0.3:.2f} rpm")
    print(f"Profundidad de corte: {f:.2f} mm")
    print(f"Avanze por diente: {an:.2f} mm/diente")
    print(f"Velocidad de avance: {velocidad_de_avance(z, diametro, vc, an):.2f} mm/min")
    print(f"Velocidad de avance con 30% de factor de potencia: {velocidad_de_avance(z, diametro, vc, an)*0.3:.2f} mm/min")
    return (velocidad_corte(diametro, vc),f,an,velocidad_de_avance(z, diametro, vc, an))
#diametro en mm
#vc velocidad de corte en m/min del material
#an avance por diente
#f profundidad de corte en mm
#z numero de dientes de la fresa

#Función para realizar el cálculo de desplazamiento total para cada proceso
def desplazamiento_total(df_temp):
    total_displacement = 0
    previous_x = None
    previous_y = None

    for index, row in df_temp.iterrows():
        current_x = row[2]
        current_x = float(current_x[1:len(current_x)])
        current_y = row[3]
        current_y = float(current_y[1:len(current_y)])
        
        if previous_x is None:
            previous_x = current_x
            previous_y = current_y
   
        individual_displacement = math.sqrt((current_x - previous_x)**2 + (current_y - previous_y)**2)
        total_displacement += individual_displacement

        # Update previous coordinates for next iteration
        previous_x = current_x
        previous_y = current_y
    return total_displacement

desp_grabado = desplazamiento_total(grabado_df)
desp_careado = desplazamiento_total(careado_df)
desp_escalonado = desplazamiento_total(escalonado_df)

tiempo_grabado = desp_grabado / (variables_de_corte(25.3*(3/16), 150, 0.45 , 4, 0.04)[3]*0.3)
print(f"Tiempo de grabado: {tiempo_grabado:.2f} min")

tiempo_escalonado = desp_escalonado / (variables_de_corte(25.3*(1/2), 150, 1.06 , 4, 0.33)[3]*0.3)
print(f"Tiempo de escalonado: {tiempo_escalonado:.2f} min")

tiempo_careado = desp_careado / (variables_de_corte(25.3*(3), 250, 1.27 , 4, 0.016)[3])
print(f"Tiempo de careado: {tiempo_careado:.2f} min")

print(f"Tiempo total: {tiempo_grabado + tiempo_escalonado + tiempo_careado:.2f} min")