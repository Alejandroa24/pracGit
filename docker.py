API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"  # demo read-only API key
import meraki
import requests
import time

dashboard = meraki.DashboardAPI(API_KEY)
r=requests.get("https://developer.cisco.com/meraki/")
response = dashboard.organizations.getOrganizations() #lista detallada de organizaciones
print(response)
print(r.raise_for_status)

listica=[]
file= open("listaOrg.txt", "w")
file.write("Lista de nombre de organizaciones\n")


for i in response:
    listica.append(i["name"])
    file.write("\n")
    file.write(i["name"])
  
file.close()

def ejecutaScript():
    time.sleep(300)
    inventario= dashboard.organizations.getOrganizationDevices("681155")
    dispositivos=open("dispositivosWirelessYApplianceDetallado.csv","w")
    dispositivos.write("INVENTARIO DE DISPOSITIVOS WIRELESS Y APPLIANCE \n Alejandro Blanco 11-10108\n")

    for k in inventario:
        if k["productType"]=="wireless" or k["productType"]=="appliance":
            tipoProducto=k["productType"]
            nombreEquipo=k["name"]
            modeloEquipo=k["model"]
            mac=k["mac"]
            ipPublica=k["networkId"]
            numSerial=k["serial"]
            statusDisp=k["configurationUpdatedAt"]
        
            dispositivos.write("\n")
            dispositivos.write("Tipo del producto : ")
            dispositivos.write(tipoProducto)
            dispositivos.write("\n")
            dispositivos.write("Nombre del equipo: ")
            dispositivos.write(nombreEquipo)
            dispositivos.write("\n")
            dispositivos.write("Modelo: ")
            dispositivos.write(modeloEquipo)
            dispositivos.write("\n")
            dispositivos.write("Mac: ")
            dispositivos.write(mac)
            dispositivos.write("\n")
            dispositivos.write("Ip publica: ")
            dispositivos.write(ipPublica)
            dispositivos.write("\n")
            dispositivos.write("Serial: ")
            dispositivos.write(numSerial)
            dispositivos.write("\n")
            dispositivos.write("Status del dispositivo: ")
            dispositivos.write(statusDisp)
            dispositivos.write("\n")

            if k["productType"]=="wireless":
                lanIp5=k["lanIp"]
                if not lanIp5:
                    lanIp5="N/A"
                dispositivos.write("Direccion Lan: ")
                dispositivos.write(lanIp5)
                dispositivos.write("\n")
            if k["productType"]=="appliance":
                wan1Ip=k["wan1Ip"]
                if not wan1Ip:
                    wan1Ip="N/A"

                dispositivos.write("Direccion wan1: ")
                dispositivos.write(wan1Ip)
                dispositivos.write("\n")
    dispositivos.close()
    

while True:
    ejecutaScript()