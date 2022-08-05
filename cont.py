import time
fin=False
def countdown():
    a=1
    while a:
        m,s = divmod(a, 60)
        print(m)
        minSeg = '{:02d}:{:02d}'.format(m, s)
        print(minSeg)
        time.sleep(1)
        a -= 1
  
    fin=True
    return fin

play=countdown()
if play==True:
    print("Se logro vinotinto")