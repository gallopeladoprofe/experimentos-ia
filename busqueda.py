import webbrowser

def buscar(r: str):
    algo = r.replace("buscar", "").strip()
    print(f"Buscando {algo}")
    webbrowser.open(f"https://www.google.com/search?q={algo}")
    
buscar("literatura rusa")