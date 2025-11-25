import tkinter as tk
import spam_detector

def analizar_email():
    #Funcion que se ejecuta al presionar el boton
    texto = entrada_email.get()

    if texto == "":
        etiqueta_resultado.config(text="Por favor escribe un email")
        return
    
    resultado = spam_detector.predecir_spam(texto, modelo, vectorizer)

    if resultado == "SPAM":
        etiqueta_resultado.config(text="SPAM", fg="red")
    else:
        etiqueta_resultado.config(text="NO SPAM", fg="green")

def main(): 
    global modelo, vectorizer, entrada_email, etiqueta_resultado

    #Entrenar modelo
    print("Entrenando modelo...")
    modelo, vectorizer = spam_detector.entrenar_modelo()

    #Mostrar precision
    accuracy = spam_detector.evaluar_modelo(modelo, vectorizer)
    print(f"Precision del modelo: {accuracy:.2f}")

    #Crear ventana
    ventana = tk.Tk()
    ventana.title("Detector de Spam")
    ventana.geometry("500x300")

    #titulo
    titulo = tk.Label(ventana, text="Detector de Spam", font=("Arial", 16, "bold"))
    titulo.pack(pady=20)

    #Istruccion
    instruccion = tk.Label(ventana, text="Escribe un email para analizar:")
    instruccion.pack()

    #Entrada de texto
    entrada_email = tk.Entry(ventana, width=50)
    entrada_email.pack(pady=10)

    #Boton
    boton = tk.Button(ventana, text="Analizar", command=analizar_email, bg="#4CAF50",fg="white", padx=20, pady=5)
    boton.pack(pady=10)

    #Resultado
    etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14))
    etiqueta_resultado.pack(pady=20)

    ventana.mainloop()

if __name__=="__main__":
    main()
