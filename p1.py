API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"  # demo read-only API key
from unicodedata import name
import meraki
import requests
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations() #lista detallada de organizaciones
#print(response)

listica=[]
file= open("listaOrg.txt", "w")
file.write("Lista de nombre de organizaciones\n")

for i in response:
    listica.append(i["name"])
    file.write("\n")
    file.write(i["name"])
  
print(listica)
file.close()