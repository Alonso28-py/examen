productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            total_stock += stock.get(modelo, [0,0])[1]
            print(f"stock total de la marca {marca.upper()}:{total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, cantidad) in stock.item():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca} - {modelo}")
    if resultados:
        resultados.sort()
        print("modelos encontrados:")
        for r in resultados:
            print(r)
    else:
        print("no hay notebooks en ese rango de precios.")

def actualizar_precios(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    return False


def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. stock marca.")
        print("2. busqueda de precio.")
        print("3. actualizar precios.")
        print("4. salir")

        opcion = input("seleccione la opcion que quiere realizar:")

        if opcion == "1":
            marca = input("ingrese la marca :")
            stock_marca(marca)
        
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("ingrese precio minimo :"))
                    p_max = int(input("ingrese precio maximo :"))
                    break
                except ValueError:
                    print("debe ingreserar valores enteros")
            busqueda_precio(p_min, p_max)
        
        elif opcion == "3":
            while True:
                modelo = input("ingrese modelo a actualizar:")
                try:
                    nuevo_precio = int(input("debe ingresar el nuevo precio:"))
                except ValueError:
                    print("debe ingresar un numero entero para el precio")
                    continue
                actualizado = actualizar_precios(modelo, nuevo_precio)
                if actualizado:
                    print("precio actualizado")
                else:
                    print("el modelo no existe")
                otra = input("desea actualizar otro precio de notebooks (si/no):")
                if otra != "si":
                    break
        elif opcion == "4":
            print("progarama finalizado.")
            break

        else:
            print("debe seleccionar una opcion valida")
menu()