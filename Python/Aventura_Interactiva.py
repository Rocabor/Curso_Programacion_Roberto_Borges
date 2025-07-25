
# TAREA DE AVENTURA INTERACTIVA
# AUTOR:ROBERTO BORGES. CURSO DE PROGRAMACION C.E.L 7/2025

print(f"Eres un aventurero novato y tienes éstas opciones a escoger. ¿Qué escoges?:")
x = str(input(f"<<< mapa // mochila // brújula >>>\n".upper()))

if x.lower() == "mapa":
    print(f"Ahora tienes un mapa y tienes que fijar un rumbo: ¿Cual eliges?")
    x = input(f"<<< norte // sur // oeste >>>\n".upper())

    if x.lower() == "norte":
        print(f"Fijas tu destino hacia el norte, hacia Hawaii y tienes que pensar en un medio de trasnporte para llegar."
              f" ¿Cual eliges?")
        x = input(f"<<< avión // carro // barco >>>\n".upper())

        if x.lower() == "avion":
            print(f"Decidistes ir en avión, la aerolinea te ofrece viajar en dos clases. cual escoges?")
            x = input(f"<<< primera // económica >>>\n".upper())

            if x.lower() == "primera":
                print(f"Antes de comprar un boleto de cualquier clase, piensas en qué temporada viajaras?")
                x = input(f"<<< alta // baja >>>\n".upper())

                if x.lower() == "alta":
                    print(f"Escoges un vuelo en temporada alta, pudiste conseguir vuelo para tu destino elegido?")
                    x = input(f"<<< si // no >>>\n".upper())

                    if x.lower() == "si":
                        print(f"Después de tanto planificar lograstes llegar a tu destino y cumplir tus sueños. "
                              f"***DESTINO ALCANZADO***")

                    elif x.lower() == "no":
                        print(f"Te faltó planificación ya que por temporada alta ya todos los voletos estaban vendidos")

                    else:
                        print(f"opción no válida. intenta de nuevo.".capitalize())

                elif x.lower() == "baja":
                    print(f"Escoges un vuelo en temporada baja, pudiste conseguir vuelo para tu destino elegido?")
                    x = input(f"<<< si // no >>>\n".upper())

                    if x.lower() == "si":
                        print(f"Facilmente consigues voleto y vuelo por ser temporada baja incluso precios más ecónomicos")

                    elif x.lower() == "no":
                        print(f"No se pudo conseguir por alguna contingencia climática y suspendieron los vuelos")

                    else:
                        print(f"Opción no válida. intenta de nuevo.")

                else:
                    print(f"Opción no válida, intenta de nuevo.")

            elif x.lower() == "economica":
                print(f"Consultas disponibilidad de voletos clase económica y no consigues. terminas aplazando el viaje "
                      f"FIN DE TU TRAYECTO...")

            else:
                print(f"Opción no válida, intenta de nuevo.")


        elif x.lower() == "carro":
            print(f"El destino que escogiste no se puede llegar por via terrestre por ser una isla en el pacifico, "
                  f"FIN DE TU TRAYECTO...")

        elif x.lower() == "barco":
            print(f"Decidistes ir en barco, pero hay diferentes horas de zarpar según la clase y categoria del viaje. "
                  f"cual eliges?")
            x = input(f"<<< primera // económica >>>\n".upper())
            
            if x.lower() == "primera":
                print(f"Te embarcaste en un crucero de primera clase donde terminas disfrutando de las lujosas "
                      f"instalaciones del crucero y llegas finalmente a tu destino objetio. FIN DE TU TRAYECTO...")

            elif x.lower() == "economica":
                print(f"No consigues zarpar ese dia por cambios climaticos y aplazas el viaje. FIN DE TU TRAYECTO...")

            else:
                print(f"Opción no válida, intenta de nuevo.")

        else:
            print(f"Opción no válida, intenta de nuevo.")


    elif x.lower() == "sur":
        print(f"Te trazas un destino al sur, hacia brasil y te interesa visitar 3 lugares. ¿Cual eliges?")
        x = input(f"<<< rio // ruinas // playa >>>\n".upper())

        if x.lower() == "rio":
            print(f"Decides ir al rio amazonas para conocer los animales exóticos pero el acceso al rio es muy complicado "
                  f"por las exesivas lluvias. FIN DE TU TRAYECTO... ")

        elif x.lower() == "ruinas":
            print(f"Consultas con diferentes aventureros reconocidos de la zona y te recomiendan no adentrarte a las "
                  f"ruinas por ser un lugar lleno de peligros y decides desistir del viaje. FIN DE TU TRAYECTO...")

        elif x.lower() == "playa":
            print(f"Llegas a las playas de rio de janeiro y reconoces que son unas de las mejores del mundo por su "
                  f"belleza local y por sus mujeres. FIN DE TU TRAYECTO...")

        else:
            print(f"Opción no válida, intenta de nuevo.")


    elif x.lower() == "oeste":
        print(f"Uno de los destinos que te gustaria llegar a conocer, es el continente asiatico por su cultura. "
              f"¿dominas algún idioma?")
        x = input(f"<<< inglés // mandarin  >>\n".upper())

        if x.lower() == "ingles":
            print(f"Almenos puedes interactuar ya que el idioma inglés es el idioma más hablado en el mundo. "
                  f"FIN DE TU TRAYECTO...")

        elif x.lower() == "mandarin":
            print(f"Excelente aprovechas al máximo la interacción con los asiaticos y conoces mejor su cultura. "
                  f"FIN DE TU TRAYECTO...")

        else:
            print(f"Opción no válida, intenta de nuevo.")

    else:
        print(f"Opción no válida, intenta de nuevo.")


elif x.lower() == "mochila":
    print(f"Tomas una mochila y empiezas a seleccionar 3 cosas que consideras útiles para tu aventura. que escoges?")
    x = input(f" <<< repelente // agua // arma >>>\n".upper())

    if x.lower() == "repelente":
        print(f"muy útil para combatir las plagas cuando acampas en zonas con mucha vegetación, rurales y boques. "
              f"pero te asusta el hecho\nde contraer enfermedades y desistes ir de aventuras. FIN DE TU TRAYECTO...")

    elif x.lower() == "agua":
            print(f"En medio de la aventura atravesando un bosque, sediento y sin agua de la que guardaste en tu "
                  f"mochila, notas a pocos metros\nun rio y decides recoger agua en la botella, al berberla sientes "
                  f"un sabor extraño y al poco tiempo te empiezas a\nsentir mareado y con fuertes dolores, decides "
                  f"regresar para ponerle FIN DE TU TRAYECTO...")

    elif x.lower() == "arma":
        print(f"Llevas en tu mochila un arma para caso de emergencia, pero cuando pasas por un alcabala los oficiales"
              f"te revisan tus\npertenencias y te piden la documentación del arma y por no tenerla vigente te retienen"
              f"por algunas horas poniendo\nFIN DE TU TRAYECTO...")

    else:
        print(f"Opción no válida, intenta de nuevo.")


elif x.lower() == "brujula":
    print(f"Tomas la brújula y asumes que es una buena herramienta para orientarte y poder trazar alguna ruta, pero sin "
          f"un mapa no\nlograrás marcar ninguna ubicación o trayectoria ni rumbo por la cual puedas guiarte. "
          f"FIN DE TU TRAYECTO...")

else:
   print(f"Opción no válida, intenta de nuevo.")
