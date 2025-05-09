from collections import defaultdict
from datetime import datetime as x

a=[{"i":1,"m":"Matrix","h":"A","d":"2025-05-01 18:00","p":50},{"i":2,"m":"Inception","h":"B","d":"2025-05-01 20:00","p":60},{"i":3,"m":"Interstellar","h":"A","d":"2025-05-02 19:00","p":55}]
b=[{"f":1,"s":[1,2,3]},{"f":1,"s":[4,5]},{"f":2,"s":[1,2,3,4]},{"f":3,"s":[10]},{"f":2,"s":[5,6]}]

def c(dt_str):
    return x.strptime(dt_str,"%Y-%m-%d %H:%M")

def d(lst_f,lst_r,n=5):
    e=defaultdict(int)
    for r in lst_r: e[r["f"]]+=len(r["s"])
    f=[]
    for u in lst_f: f.append((u["i"],u["m"],u["h"],e[u["i"]]))
    f.sort(key=lambda t:t[3],reverse=True)
    return f[:n]

def g(lst_f,lst_r):
    h={u["i"]:u["p"]for u in lst_f}
    i=defaultdict(float)
    for r in lst_r:
        fn=next((u for u in lst_f if u["i"]==r["f"]),None)
        if not fn: continue
        ds=c(fn["d"]).date().isoformat()
        i[ds]+=h[fn["i"]]*len(r["s"])
    return dict(i)

def j(lst_f,lst_r,caps):
    k=defaultdict(int)
    for r in lst_r:
        fn=next((u for u in lst_f if u["i"]==r["f"]),None)
        if not fn: continue
        k[fn["h"]]+=len(r["s"])
    l={}
    for hall,sold in k.items():
        l[hall]=round((sold/caps.get(hall,1))*100,2)
    return l

m={"A":100,"B":80,"C":120}
print("=== Top 3 más vistas ===")
for tid,mv,hl,vs in d(a,b,n=3): print(f"Función {tid} | {mv} en Sala {hl}: {vs} asientos vendidos")
print("=== Ingresos por día ===")
for day,val in sorted(g(a,b).items()): print(f"{day}: ${val:.2f}")
print("=== Ocupación por sala ===")
for hall,pct in j(a,b,m).items(): print(f"Sala {hall}: {pct}% ocupada")
