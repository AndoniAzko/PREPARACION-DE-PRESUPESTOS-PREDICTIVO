import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import re
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error,explained_variance_score
from sklearn.preprocessing import StandardScaler
from pickle import load

scaler = StandardScaler()
lr = RandomForestRegressor()

df_cilindros_ent = pd.read_csv(r'C:\Users\Andoni\Desktop\MASTER DATA SCIENCE\TFM\DATA\DFCILINDROS_ENTRADA.csv')
loaded_model = load(open('pipe.pkl', 'rb'))
contador_amarre = 0
contador_extra = 0
key_amarres = 'AMARRE {}'.format(contador_amarre)
materiales = ['NO','ACERO', 'ALUMINIO', 'CROMADO', 'BRONCE','F-2111','INOX','MP','METACRILATO','COMPRADO']
amarres = ['FUELLE','DETECTOR','ESCUADRA','BRIDA','ARTICULACION MACHO','ARTICULACION HEMBRA','SOPORTE','SOPORTE ARTICULACION','ZUNCHO','ARTICULACION SOPORTE ROTULA','SOPORTE CON ROTULA','ARTICULACION TRASERA CON ROTULA','ROTULA','HORQUILLA','BULON','CONTRATUERCA','BLOQUEO','GUIADO','CREMALLERA','SOPORTE CENTRAL','PIÑON']
prueba = {'MP CAMISA':['NO'],'MP VASTAGO':['NO'],'MP VARILLAS':['NO'],'MP CABEZA PISTON':['ACERO'],'MP TAPA GUIA':['NO'],'MP TAPA TRASERA':['NO'],'DIAMETRO':[0],'CARRERA':[0],'KIT':[0],'ALTA TEMPERATURA':[0],'AMARRE 0':['NO'],'AMARRE 1':['NO'],'AMARRE 2':['NO'],'AMARRE 3':['NO'],'AMARRE 4':['NO'],'AMARRE 5':['NO'],'AMARRE 6':['NO'],'AMARRE 7':['NO'],'AMARRE 8':['NO'],'AMARRE 9':['NO'],'AMARRE 10':['NO'],'EXTRA 1':['NO'],'EXTRA 2':['NO'],'EXTRA 3':['NO'],'EXTRA 4':['NO'],'EXTRA 5':['NO'],'EXTRA 6':['NO'],'EXTRA 7':['NO'],'UNIDADES':[1]}

st.title('Calculadora de presupuestos de cilindros especiales')

st.header('Inserta la referencia del cilindro:')

#referencia = st.text_input("REFERENCIA")
#prueba['ARTICULO'] = referencia

st.header('Inserta el diametro del cilindro:')

diametro = st.text_input("DIAMETRO")
prueba['DIAMETRO'] = diametro

st.header('Inserta la carrera del cilindro:')

carrera = st.text_input("CARRERA")
prueba['CARRERA'] = carrera

st.header('Inserta las unidades:')

unidades = st.text_input("UNIDADES",1)
prueba['UNIDADES'] = unidades

st.header('Elige los materiales de los siguientes elementos:')

st.subheader('Es de Alta temperatura?')

ALTA_TEMPERATURA = st.checkbox('ALTA TEMPERATURA')

if ALTA_TEMPERATURA:
    prueba['KIT'] = 1

st.subheader('Lleva KIT?')

KIT = st.checkbox('KIT')

if KIT:

    prueba['KIT'] = 1

    option_tapaguia = 'NO'
    prueba['MP TAPA GUIA'] = option_tapaguia

    option_tapatrasera = 'NO'
    prueba['MP TAPA TRASERA'] = option_tapatrasera

    option_piston = 'NO'
    prueba['MP CABEZA PISTON'] = option_piston

    st.subheader('Tirantes')

    option_tirantes = st.selectbox('Material tirantes:',materiales)
    prueba['MP VARILLAS'] = option_tirantes

    st.subheader('Vastago')

    option_vastago = st.selectbox('Material vastago:',materiales)
    prueba['MP VASTAGO'] = option_vastago

    st.subheader('Camisa')

    option_camisa = st.selectbox('Material camisa:',materiales)
    prueba['MP CAMISA'] = option_camisa


    


else:

    prueba['KIT'] = 0

    st.subheader('Tapa Guia')

    option_tapaguia = st.selectbox('Material tapa guia:',materiales)
    prueba['MP TAPA GUIA'] = option_tapaguia

    st.subheader('Tapa Trasera')

    option_tapatrasera = st.selectbox('Material tapa trasera:',materiales)
    prueba['MP TAPA TRASERA'] = option_tapatrasera

    st.subheader('Pistón')

    option_piston = st.selectbox('Material pistón:',materiales)
    prueba['MP CABEZA PISTON'] = option_piston

    st.subheader('Tirantes')

    option_tirantes = st.selectbox('Material tirantes:',materiales)
    prueba['MP VARILLAS'] = option_tirantes

    st.subheader('Vastago')

    option_vastago = st.selectbox('Material vastago:',materiales)
    prueba['MP VASTAGO'] = option_vastago

    st.subheader('Camisa')

    option_camisa = st.selectbox('Material camisa:',materiales)
    prueba['MP CAMISA'] = option_camisa


st.header('Elige los mamarre/extras que va a llevar:')


FUELLE = st.checkbox('FUELLE')

if FUELLE:
    prueba['AMARRE {}'.format(contador_amarre)] = 'FUELLE'
    contador_amarre = contador_amarre + 1

DETECTOR = st.checkbox('DETECTOR')

if DETECTOR:
    prueba['AMARRE {}'.format(contador_amarre)] = 'DETECTOR'
    contador_amarre = contador_amarre + 1

ESCUADRA = st.checkbox('ESCUADRA')

if ESCUADRA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ESCUADRA'
    contador_amarre = contador_amarre + 1

BRIDA = st.checkbox('BRIDA')

if BRIDA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'BRIDA'
    contador_amarre = contador_amarre + 1

ARTICULACION_MACHO = st.checkbox('ARTICULACION MACHO')

if ARTICULACION_MACHO:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ARTICULACION MACHO'
    contador_amarre = contador_amarre + 1

ARTICULACION_HEMBRA = st.checkbox('ARTICULACION HEMBRA')

if ARTICULACION_HEMBRA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ARTICULACION HEMBRA'
    contador_amarre = contador_amarre + 1

SOPORTE = st.checkbox('SOPORTE')

if SOPORTE:
    prueba['AMARRE {}'.format(contador_amarre)] = 'SOPORTE'
    contador_amarre = contador_amarre + 1

SOPORTE_ARTICULACION = st.checkbox('SOPORTE ARTICULACION')

if SOPORTE_ARTICULACION:
    prueba['AMARRE {}'.format(contador_amarre)] = 'SOPORTE ARTICULACION'
    contador_amarre = contador_amarre + 1

ZUNCHO = st.checkbox('ZUNCHO')

if ZUNCHO:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ZUNCHO'
    contador_amarre = contador_amarre + 1

ARTICULACION_SOPORTE_ROTULA = st.checkbox('ARTICULACION SOPORTE ROTULA')

if ARTICULACION_SOPORTE_ROTULA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ARTICULACION SOPORTE ROTULA'
    contador_amarre = contador_amarre + 1

SOPORTE_CON_ROTULA = st.checkbox('SOPORTE CON ROTULA')

if SOPORTE_CON_ROTULA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'SOPORTE CON ROTULA'
    contador_amarre = contador_amarre + 1

ARTICULACION_TRASERA_CON_ROTULA = st.checkbox('ARTICULACION TRASERA CON ROTULA')

if ARTICULACION_TRASERA_CON_ROTULA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ARTICULACION TRASERA CON ROTULA'
    contador_amarre = contador_amarre + 1

ROTULA = st.checkbox('ROTULA')

if ROTULA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'ROTULA'
    contador_amarre = contador_amarre + 1

HORQUILLA = st.checkbox('HORQUILLA')

if HORQUILLA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'HORQUILLA'
    contador_amarre = contador_amarre + 1

BULON = st.checkbox('BULON')

if BULON:
    prueba['AMARRE {}'.format(contador_amarre)] = 'BULON'
    contador_amarre = contador_amarre + 1

CONTRATUERCA = st.checkbox('CONTRATUERCA')

if CONTRATUERCA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'CONTRATUERCA'
    contador_amarre = contador_amarre + 1

BLOQUEO = st.checkbox('BLOQUEO VASTAGO')

if BLOQUEO:
    prueba['AMARRE {}'.format(contador_amarre)] = 'BLOQUEO'
    contador_amarre = contador_amarre + 1

GUIADO = st.checkbox('GUIADO')

if GUIADO:
    prueba['AMARRE {}'.format(contador_amarre)] = 'GUIADO'
    contador_amarre = contador_amarre + 1

CREMALLERA = st.checkbox('CREMALLERA')

if CREMALLERA:
    prueba['AMARRE {}'.format(contador_amarre)] = 'CREMALLERA'
    contador_amarre = contador_amarre + 1

SOPORTE_CENTRAL = st.checkbox('SOPORTE CENTRAL')

if SOPORTE_CENTRAL:
    prueba['AMARRE {}'.format(contador_amarre)] = 'SOPORTE CENTRAL'
    contador_amarre = contador_amarre + 1

PIÑON = st.checkbox('PIÑON')

if PIÑON:
    prueba['AMARRE {}'.format(contador_amarre)] = 'PIÑON'
    contador_amarre = contador_amarre + 1

st.header('Elige si hay mas de un elemento (tapas, varillas...')

CAMISA = st.checkbox('CAMISA')

if CAMISA:
    prueba['EXTRA {}'.format(contador_amarre)] = 'CAMISA'
    contador_extra = contador_extra + 1

VASTAGO = st.checkbox('VASTAGO')

if VASTAGO:
    prueba['EXTRA {}'.format(contador_amarre)] = 'VASTAGO'
    contador_extra = contador_extra + 1

VARILLA = st.checkbox('VARILLA')

if VARILLA:
    prueba['EXTRA {}'.format(contador_amarre)] = 'VARILLA'
    contador_extra = contador_extra + 1

PISTON = st.checkbox('PISTON')

if PISTON:
    prueba['EXTRA {}'.format(contador_amarre)] = 'PISTON'
    contador_extra = contador_extra + 1

TAPA_TRAS = st.checkbox('TAPA TRAS')

if TAPA_TRAS:
    prueba['EXTRA {}'.format(contador_amarre)] = 'TAPA TRAS'
    contador_extra = contador_extra + 1

TAPA_GUIA = st.checkbox('TAPA GUIA')

if TAPA_GUIA:
    prueba['EXTRA {}'.format(contador_amarre)] = 'TAPA GUIA'
    contador_extra = contador_extra + 1


#def nuevo_input(variables):
    
    #añado la linea al dataframe original para poder hacer encoding con las nuevas variables categoricas
       
    #df = df_cilindros_ent.append(variables, ignore_index=True)

    #array = np.array(list(variables))
    
    #defino los tipos de las variables
    #df['AÑO'] = pd.to_numeric(df['AÑO'], downcast='integer')
    #df['UNIDADES'] = pd.to_numeric(df['UNIDADES'], downcast='integer')
    #df['DIAMETRO'] = pd.to_numeric(df['DIAMETRO'], downcast='integer')
    #df['CARRERA'] = pd.to_numeric(df['CARRERA'], downcast='integer')
    #df['KIT'] = df['KIT'].astype("category")
    #df['MP CAMISA'] = df['MP CAMISA'].astype("category")
    #df['MP VASTAGO'] = df['MP VASTAGO'].astype("category")
    #df['MP VARILLAS'] = df['MP VARILLAS'].astype("category")
    #df['MP CABEZA PISTON'] = df['MP CABEZA PISTON'].astype("category")
    #df['MP TAPA GUIA'] = df['MP TAPA GUIA'].astype("category")
    #df['MP TAPA TRASERA'] = df['MP TAPA TRASERA'].astype("category")
    ####df['MP CABEZA PISTON'] = df['MP CABEZA PISTON'].astype("category")
    # df['AMARRE 0'] = df['AMARRE 0'].astype("category")
    # df['AMARRE 1'] = df['AMARRE 1'].astype('category')
    # df['AMARRE 2'] = df['AMARRE 2'].astype('category')
    # df['AMARRE 3'] = df['AMARRE 3'].astype('category')
    # df['AMARRE 4'] = df['AMARRE 4'].astype('category')
    # df['AMARRE 5'] = df['AMARRE 5'].astype('category')
    # df['AMARRE 6'] = df['AMARRE 6'].astype('category')
    # df['AMARRE 7'] = df['AMARRE 7'].astype('category')
    # df['AMARRE 8'] = df['AMARRE 8'].astype('category')
    # df['AMARRE 9'] = df['AMARRE 9'].astype('category')
    # df['AMARRE 10'] = df['AMARRE 10'].astype('category')
    # df['EXTRA 1'] = df['EXTRA 1'].astype('category')
    # df['EXTRA 2'] = df['EXTRA 2'].astype('category')
    # df['EXTRA 3'] = df['EXTRA 3'].astype('category')
    # df['EXTRA 4'] = df['EXTRA 4'].astype('category')
    # df['EXTRA 5'] = df['EXTRA 5'].astype('category')
    # df['EXTRA 6'] = df['EXTRA 6'].astype('category')
    # df['EXTRA 7'] = df['EXTRA 7'].astype('category')
    # df['UNIDADES'] = pd.to_numeric(df['UNIDADES'], downcast='integer')
    
    #guardo las columnas que quiero hacer encoding segun su tipo
    # obj_columns=list(df.select_dtypes(include =['category']).columns)
    # df_cilindros_encoded = pd.get_dummies(data=df, columns = obj_columns)
    
    
    # #quito las columnas que no necesito
    # df_cilindros_encoded=df_cilindros_encoded.drop(["SEQ_ARTICULO",'REF_ALTERNATIVA','NOMBRE','NOMBRE_ABR','FEC_ALTA','OBSER','DIM CAMISA','DIM VASTAGO','DIM VARILLAS','DIM CABEZA PISTON','DIM TAPA GUIA','DIM TAPA TRASERA','PRECIO1','FEC_MOV','AÑO'],axis=1)    
    # #selecciono solo la linea que quiero predecir
    # df_cilindros_encoded = df_cilindros_encoded[df_cilindros_encoded['ARTICULO']== referencia]
    # #quito la columna articulo para predecir
    # df_cilindros_encoded = df_cilindros_encoded.loc[:, df_cilindros_encoded.columns != 'ARTICULO']
    # df_cilindros_encoded = df_cilindros_encoded.to_numpy()
    # st.text(type(df_cilindros_encoded))

    # #hago la predicción y lo printeo

    
    # return precio


df_prueba = pd.DataFrame.from_dict(prueba)


if st.button('CALCULAR'):
   st.text(loaded_model.predict(df_prueba)) 