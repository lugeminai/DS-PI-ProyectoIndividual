from re import X
from normalizador import NormalizadorDataFrame

from cargar import leerCSV_y_concat
from cargar import leerXLSX_y_concatCanalVenta
from cargar import leerCSV_y_concatClient_o_Sucur
from cargar import leerCSV_y_concatProveedor

# Se genera dataframes a partir de los archivos de la carpeta Datasets
df_clientes= leerCSV_y_concatClient_o_Sucur('Clien')
df_compra=leerCSV_y_concat('Compr')
df_gasto=leerCSV_y_concat('Gasto')
df_localidades= leerCSV_y_concat('Local')
df_proveedores= leerCSV_y_concatProveedor('Provee')
df_sucursales= leerCSV_y_concatClient_o_Sucur('Sucur')
df_ventas= leerCSV_y_concat('Vent')
df_tipoGasto = leerCSV_y_concat('TiposDeGas')
df_canalVenta=leerXLSX_y_concatCanalVenta('Canal')



nor = NormalizadorDataFrame()
#normalizar df_clientes
#n
df_clientes=nor.eliminar_columnas_vacias(df_clientes)
df_clientes= nor.corregir_geolocalizacion(df_clientes)
df_clientes= nor.agregar_rango_etario(df_clientes)
df_clientes= nor.llenar_nulos(df_clientes)
df_clientes= nor.renombrar_columnas(df_clientes,{"ID":"IdCliente","X":"Longitud","Y":"Latitud"})
df_clientes= nor.eliminar_duplicados(df_clientes)
df_clientes= nor.upper_strings(df_clientes)

print(df_clientes)

print(df_clientes.info())

#normalizar df_compra
df_compra= nor.llenar_nulos(df_compra)
df_compra= nor.parsear_fecha(df_compra,"Fecha")
df_compra= nor.eliminar_columnas(df_compra,["Fecha_Año","Fecha_Mes","Fecha_Periodo"])
df_compra= nor.upper_strings(df_compra)
print(df_compra)
#normalizar df_gasto
df_gasto = nor.parsear_fecha(df_gasto,"Fecha")
df_gasto = nor.upper_strings(df_gasto)


#normalizar df_proveedores
df_proveedores = nor.llenar_nulos(df_proveedores)
df_proveedores = nor.renombrar_columnas(df_proveedores,{"IDProveedor":"IdProveedor", "Address":"Domicilio","City":"Ciudad","State":"Provincia","Country":"Pais","departamen":"Localidad"})
df_proveedores = nor.upper_strings(df_proveedores)
print(df_proveedores)

#normalizar df_sucursales
df_suscursales = nor.renombrar_columnas(df_sucursales,{"ID":"IdSucursal"})
df_suscursales = nor.upper_strings(df_sucursales)
#normalizar df_venta
df_ventas = nor.parsear_fecha(df_ventas,"Fecha")
df_ventas = nor.parsear_fecha(df_ventas,"Fecha_Entrega")
df_ventas = nor.upper_strings(df_ventas)

#normalizar df_canalVenta
df_canalVenta = nor.renombrar_columnas(df_canalVenta,{"CODIGO":"IdCanal","DESCRIPCION":"Canal"})
df_canalVenta = nor.upper_strings(df_canalVenta)
print(df_canalVenta)


