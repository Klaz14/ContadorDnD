import os
"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("dnd.kv")
"""

class Perfil:
    @staticmethod
    def crear_personaje():
        if os.path.exists("perfiles.txt"):
            return

        else:
            print("No se encontró ningún personaje.")
            nombre = input("Introduce tu nombre: ")
            raza = input("Introduce tu raza: ")
            clase = input("Introduce tu clase: ")
            vida = int(input("Introduce la vida base de tu PJ: "))
            ca = int(input("Introduce la CA base de tu PJ: "))
            print("Por favor, ingrese la cantidad de hechizos de cada nivel.")
            nivel_1 = int(input("Nivel 1: "))
            nivel_2 = int(input("Nivel 2: "))
            nivel_3 = int(input("Nivel 3: "))
            vida_temp = vida
            nivel_1_temp = nivel_1
            nivel_2_temp = nivel_2
            nivel_3_temp = nivel_3
            contador_criticos = 0
            daño = 0
            contador_kills = 0

            with open("perfiles.txt", "a") as archivo:
                archivo.write(
                    f"{nombre},{raza},{clase},{vida},{ca},{nivel_1},{nivel_2},{nivel_3}\n"
                )

            with open(f"{nombre}_info.txt", "a") as archivo:
                archivo.write(
                    f"{vida_temp},{nivel_1_temp},{nivel_2_temp},{nivel_3_temp},{contador_criticos},{daño},{contador_kills}"
                )
                pass

            with open(f"{nombre}_items.txt", "a") as archivo:
                pass

            with open(f"{nombre}_consumibles.txt", "a") as archivo:
                pass

            print(f"Perfil de {nombre} guardado correctamente.")

    @staticmethod
    def selec_perfil():
        with open("perfiles.txt", "r") as archivo:
            perfiles = [linea.strip().split(",")[0] for linea in archivo]

        if len(perfiles) == 1:
            return perfiles[0]

    @staticmethod
    def mostrar_perfil():
        with open("perfiles.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                print(f"Bienvenido {datos[0]}, {datos[1]} {datos[2]}.")

    @staticmethod
    def reiniciar_personaje(perfil):
        print(
            "Esta accion eliminara tu personaje permanentemente y deberas reiniciar la aplicacion."
        )
        opcion = input(
            "¿Estás seguro que quieres reiniciar tu personaje? (1. Sí / 2. No): "
        )
        if opcion == "1":
            try:
                os.remove(f"{perfil}_items.txt")
                os.remove(f"{perfil}_consumibles.txt")
                os.remove(f"{perfil}_info.txt")
                os.remove("perfiles.txt")
                print("Personaje reiniciado exitosamente.")
                exit()
            except Exception as e:
                print(f"Error al reiniciar el personaje: {e}")
        elif opcion == "2":
            print("No se realizaron cambios.")
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")


class Contador:
    @staticmethod
    def contador(objeto):
        cant_total = int(input(f"Ingrese la cantidad actual que tienes de {objeto}: "))
        print(f"Usted tiene {cant_total} {objeto}.")
        return cant_total

    @staticmethod
    def sumar_contador(cant_total):
        cant_total += 1
        return cant_total

    @staticmethod
    def restar_contador(cant_total):
        cant_total -= 1
        return cant_total

    @staticmethod
    def sumar_cant(cant_total):
        sumar = int(input("Ingrese la cantidad a sumar: "))
        nueva_cant_total = cant_total + sumar
        return nueva_cant_total

    @staticmethod
    def restar_cant(cant_total):
        restar = int(input("Ingrese la cantidad a restar: "))
        nueva_cant_total = cant_total - restar
        return nueva_cant_total


class GestorVIdaCA:
    @staticmethod
    def mostrar_vida_temp(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo:
            lineas_info = [
                int(valor) for valor in archivo.readline().strip().split(",")
            ]

        vida_temp = lineas_info[0]

        print(f"Tienes {vida_temp} de vida.")

    @staticmethod
    def sumar_vida(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo:
            lineas_info = [
                int(valor) for valor in archivo.readline().strip().split(",")
            ]

        vida_temp = lineas_info[0]

        nueva_vida = Contador.sumar_cant(vida_temp)

        lineas_info[0] = nueva_vida

        with open(f"{perfil}_info.txt", "w") as archivo:
            archivo.write(",".join(map(str, lineas_info)))

    @staticmethod
    def restar_vida(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo:
            lineas_info = [
                int(valor) for valor in archivo.readline().strip().split(",")
            ]

        vida_temp = lineas_info[0]

        nueva_vida = Contador.restar_cant(vida_temp)

        lineas_info[0] = nueva_vida

        with open(f"{perfil}_info.txt", "w") as archivo:
            archivo.write(",".join(map(str, lineas_info)))

    @staticmethod
    def reest_vida(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo_info:
            lineas_info = [
                int(valor) for valor in archivo_info.readline().strip().split(",")
            ]

        with open("perfiles.txt", "r") as archivo_perfiles:
            for linea in archivo_perfiles:
                datos = linea.strip().split(",")

                if datos[0] == perfil:
                    vida = int(datos[3])
                    break

        lineas_info[0] = vida

        with open(f"{perfil}_info.txt", "w") as archivo_info:
            archivo_info.write(",".join(map(str, lineas_info)))

    @staticmethod
    def mod_ca(perfil):
        nueva_ca = int(input("Ingrese su nueva CA: "))

        with open("perfiles.txt", "r") as archivo:
            lineas = archivo.readlines()

        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")

            if datos[0] == perfil:
                datos[4] = str(nueva_ca)

            lineas[i] = ",".join(datos)

        with open("perfiles.txt", "w") as archivo:
            archivo.writelines(lineas)

        print(f"CA modificada correctamente, su nueva CA es de {nueva_ca}.")


class GestorHechizos:
    @staticmethod
    def cont_hechizos(perfil):
        try:
            with open(f"{perfil}_info.txt", "r") as archivo_info:
                lineas_info = [
                    int(valor) for valor in archivo_info.readline().strip().split(",")
                ]

            (
                vida_temp,
                nivel_1_temp,
                nivel_2_temp,
                nivel_3_temp,
                contador_criticos,
                daño,
                contador_kills,
            ) = lineas_info

            print(f"Nivel 1: {nivel_1_temp} hechizos")
            print(f"Nivel 2: {nivel_2_temp} hechizos")
            print(f"Nivel 3: {nivel_3_temp} hechizos")

            print("Deseas sumar o restar hechizos?")
            print("1. Sumar")
            print("2. Restar")
            print("3. Vover al Menu")

            opcion = input("Elige una opción (1/2/3): ")

            if opcion == "1":
                nivel = input("¿En qué nivel deseas sumar hechizos? (1/2/3): ")
                if nivel == "1":
                    nueva_cantidad = Contador.sumar_contador(nivel_1_temp)
                    nivel_1_temp = nueva_cantidad
                elif nivel == "2":
                    nueva_cantidad = Contador.sumar_contador(nivel_2_temp)
                    nivel_2_temp = nueva_cantidad
                elif nivel == "3":
                    nueva_cantidad = Contador.sumar_contador(nivel_3_temp)
                    nivel_3_temp = nueva_cantidad
                else:
                    print("Opción inválida.")
                    return
            elif opcion == "2":
                nivel = input("¿En qué nivel deseas restar hechizos? (1/2/3): ")
                if nivel == "1":
                    nueva_cantidad = Contador.restar_contador(nivel_1_temp)
                    nivel_1_temp = nueva_cantidad
                elif nivel == "2":
                    nueva_cantidad = Contador.restar_contador(nivel_2_temp)
                    nivel_2_temp = nueva_cantidad
                elif nivel == "3":
                    nueva_cantidad = Contador.restar_contador(nivel_3_temp)
                    nivel_3_temp = nueva_cantidad
                else:
                    print("Opción inválida.")
                    return
            elif opcion == "3":
                return
            else:
                print("Opción inválida.")
                return

            with open(f"{perfil}_info.txt", "w") as archivo_info:
                archivo_info.write(
                    f"{vida_temp},{nivel_1_temp},{nivel_2_temp},{nivel_3_temp},{contador_criticos},{daño}, {contador_kills}"
                )

            print("¡Cantidad de hechizos actualizada correctamente!")

        except Exception as e:
            print(f"Error al actualizar la cantidad de hechizos: {e}")

    @staticmethod
    def reset_hechizos(perfil):
        try:
            with open(f"{perfil}_info.txt", "r") as archivo_info:
                lineas_info = [
                    int(valor) for valor in archivo_info.readline().strip().split(",")
                ]

            vida_temp, _, _, _, contador_criticos, daño, contador_kills = lineas_info

            with open("perfiles.txt", "r") as archivo_perfiles:
                for linea in archivo_perfiles:
                    datos = linea.strip().split(",")

                    if datos[0] == perfil:
                        nivel_1 = int(datos[5])
                        nivel_2 = int(datos[6])
                        nivel_3 = int(datos[7])
                        break

            with open(f"{perfil}_info.txt", "w") as archivo_info:
                archivo_info.write(
                    f"{vida_temp},{nivel_1},{nivel_2},{nivel_3},{contador_criticos},{daño},{contador_kills}"
                )

            print("Hechizos reseteados correctamente!")

        except Exception as e:
            print(f"Error al resetear la cantidad de hechizos: {e}")


class Items:
    @staticmethod
    def añadir_item(perfil):
        opcion = input("¿Qué deseas añadir? (1. Item / 2. Consumible): ")
        if opcion == "1":
            nombre = input("Introduce el nombre del item: ")
            with open(f"{perfil}_items.txt", "a") as archivo:
                archivo.write(f"{nombre}\n")
            print(f"El item '{nombre}' ha sido añadido correctamente.")
        elif opcion == "2":
            nombre = input("Introduce el nombre del consumible: ")
            cantidad = int(input("Introduce la cantidad a guardar: "))
            with open(f"{perfil}_consumibles.txt", "a") as archivo:
                archivo.write(f"{nombre},{cantidad}\n")
            print(
                f"El consumible '{nombre}' con cantidad {cantidad} ha sido añadido correctamente."
            )
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")

    @staticmethod
    def borrar_item(perfil):
        pass

    @staticmethod
    def mostrar_cant_consumible():
        pass


class Varios:
    @staticmethod
    def cont_criticos(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo_info:
            lineas_info = [
                int(valor) for valor in archivo_info.readline().strip().split(",")
            ]
            (
                vida_temp,
                nivel_1_temp,
                nivel_2_temp,
                nivel_3_temp,
                contador_criticos,
                daño,
                contador_kills,
            ) = lineas_info

        contador_criticos += 1
        print(f"Felicidades por un critico mas! Con este ya van {contador_criticos}!")

        daño += int(input("Por favor, introduce la cantidad de daño hecho: "))
        print(
            f"Demasiado daño! Con esto acumulas {daño} de vida quitada solo con criticos!"
        )

        with open(f"{perfil}_info.txt", "w") as archivo_info:
            archivo_info.write(
                f"{vida_temp},{nivel_1_temp},{nivel_2_temp},{nivel_3_temp},{contador_criticos},{daño}, {contador_kills}"
            )

    @staticmethod
    def cont_kills(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo_info:
            lineas_info = [
                int(valor) for valor in archivo_info.readline().strip().split(",")
            ]
            (
                vida_temp,
                nivel_1_temp,
                nivel_2_temp,
                nivel_3_temp,
                contador_criticos,
                daño,
                contador_kills,
            ) = lineas_info

        contador_kills += 1

        print(f"Felicidades por tu nueva víctima! Con este ya van {contador_kills}!")

        with open(f"{perfil}_info.txt", "w") as archivo_info:
            archivo_info.write(
                f"{vida_temp},{nivel_1_temp},{nivel_2_temp},{nivel_3_temp},{contador_criticos},{daño},{contador_kills}"
            )

    @staticmethod
    def mostrar_criticos_y_kills(perfil):
        with open(f"{perfil}_info.txt", "r") as archivo_info:
            lineas_info = [
                int(valor) for valor in archivo_info.readline().strip().split(",")
            ]
            _, _, _, _, contador_criticos, daño, contador_kills = lineas_info

        print(f"Cantidad de críticos hechos: {contador_criticos}")
        print(f"Cantidad de enemigos asesinados: {contador_kills}")
        print(f"Daño crítico total: {daño}")

    @staticmethod
    def cerrar_app():
        print("Vuelve pronto!")
        exit()


class SubirNivel:
    @staticmethod
    def modificar_vida(perfil):
        try:
            with open(f"{perfil}_info.txt", "r") as archivo_info:
                lineas_info = [
                    int(valor) for valor in archivo_info.readline().strip().split(",")
                ]
                vida_temp, _, _, _, _, _, _ = lineas_info

            golpe = int(input("De cuanto es tu dado de golpe? "))
            nueva_vida = vida_temp + (golpe // 2) + 1

            with open(f"{perfil}_info.txt", "w") as archivo_info:
                archivo_info.write(
                    f"{nueva_vida},{lineas_info[1]},{lineas_info[2]},{lineas_info[3]},{lineas_info[4]},{lineas_info[5]},{lineas_info[6]}"
                )

            with open("perfiles.txt", "r") as archivo_perfiles:
                lineas = archivo_perfiles.readlines()

            for i, linea in enumerate(lineas):
                datos = linea.strip().split(",")

                if datos[0] == perfil:
                    datos[3] = str(nueva_vida)

                lineas[i] = ",".join(datos)

            with open("perfiles.txt", "w") as archivo_perfiles:
                archivo_perfiles.writelines(lineas)

            print(f"¡Vida actualizada a {nueva_vida}!")

        except Exception as e:
            print(f"Error al modificar la vida: {e}")

    @staticmethod
    def modificar_hechizos(perfil):
        try:
            with open("perfiles.txt", "r") as archivo:
                lineas = archivo.readlines()

            for i, linea in enumerate(lineas):
                datos = linea.strip().split(",")

                if datos[0] == perfil:
                    print(f"Nivel 1: {datos[5]} hechizos")
                    print(f"Nivel 2: {datos[6]} hechizos")
                    print(f"Nivel 3: {datos[7]} hechizos")

                    nivel_1 = int(
                        input("Ingrese la nueva cantidad de hechizos de nivel 1: ")
                    )
                    nivel_2 = int(
                        input("Ingrese la nueva cantidad de hechizos de nivel 2: ")
                    )
                    nivel_3 = int(
                        input("Ingrese la nueva cantidad de hechizos de nivel 3: ")
                    )

                    datos[5] = str(nivel_1)
                    datos[6] = str(nivel_2)
                    datos[7] = str(nivel_3)

                    lineas[i] = ",".join(datos)

                    with open("perfiles.txt", "w") as archivo:
                        archivo.writelines(lineas)

                    print("¡Cantidad de hechizos actualizada correctamente!")

                    return

            print(f"No se encontró ningún perfil con el nombre '{perfil}'.")

        except Exception as e:
            print(f"Error al modificar la cantidad de hechizos: {e}")


class Menu:
    @staticmethod
    def menu_principal(perfil):
        Perfil.mostrar_perfil()

        if perfil:
            print(f"1. Vida")
            print(f"2. CA")
            print(f"3. Hechizos")
            print(f"4. Criticos y Kills")
            print(f"5. Subir de Nivel")
            print(f"6. Eliminar PJ")
            print(f"7. Cerrar App")

        opcion = input("Por favor, elige una opción (1 a 7): ")

        if perfil and opcion == "1":
            perfil = Menu.submenu_vida(perfil)

        elif perfil and opcion == "2":
            GestorVIdaCA.mod_ca(perfil)

        elif perfil and opcion == "3":
            perfil = Menu.submenu_hechizos(perfil)

        elif perfil and opcion == "4":
            perfil = Menu.submenu_crit_kill(perfil)

        elif perfil and opcion == "5":
            SubirNivel.modificar_vida(perfil)
            SubirNivel.modificar_hechizos(perfil)

        elif perfil and opcion == "6":
            Perfil.reiniciar_personaje(perfil)

        elif perfil and opcion == "7":
            Varios.cerrar_app()

        else:
            print("Opción inválida. Por favor, elige 1 a 7.")

        return perfil

    @staticmethod
    def submenu_vida(perfil):
        GestorVIdaCA.mostrar_vida_temp(perfil)

        print(f"1. Sumar Vida")
        print(f"2. Restar Vida")
        print(f"3. Resetear Vida")
        print(f"4. Volver al Menú Principal")

        opcion = input("Por favor, elige una opción (1 a 4): ")

        if opcion == "1":
            GestorVIdaCA.sumar_vida(perfil)
        elif opcion == "2":
            GestorVIdaCA.restar_vida(perfil)
        elif opcion == "3":
            GestorVIdaCA.reest_vida(perfil)
        elif opcion == "4":
            return perfil
        else:
            print("Opción inválida. Por favor, elige 1 a 4.")

        return Menu.submenu_vida(perfil)

    @staticmethod
    def submenu_hechizos(perfil):
        print(f"1. Usos de Hechizos")
        print(f"2. Resetear Hechizos a Cantidad Base")
        print(f"3. Volver al Menú Principal")

        opcion = input("Por favor, elige una opción (1 a 3): ")

        if opcion == "1":
            GestorHechizos.cont_hechizos(perfil)
        elif opcion == "2":
            GestorHechizos.reset_hechizos(perfil)
        elif opcion == "3":
            return perfil
        else:
            print("Opción inválida. Por favor, elige 1 a 3.")

        return Menu.submenu_hechizos(perfil)

    @staticmethod
    def submenu_crit_kill(perfil):
        print("1. Sumar un Critico")
        print("2. Sumar una Kill")
        print("3. Mostrar Datos de Criticos y Kills Globales")
        print(f"4. Volver al Menú Principal")

        opcion = input("Por favor, elige una opción (1 a 4): ")

        if opcion == "1":
            Varios.cont_criticos(perfil)
        elif opcion == "2":
            Varios.cont_kills(perfil)
        elif opcion == "3":
            Varios.mostrar_criticos_y_kills(perfil)
        elif opcion == "4":
            return perfil
        else:
            print("Opción inválida. Por favor, elige 1 a 4.")

        return Menu.submenu_crit_kill(perfil)


if __name__ == "__main__":
    Perfil.crear_personaje()

    perfil = Perfil.selec_perfil()

    while True:
        perfil = Menu.menu_principal(perfil)
