import tkinter
import customtkinter
import logic

# Modo oscuro o claro según el sistema que tenga por default en la computadora (background)
customtkinter.set_appearance_mode("System")
# Estilos de color de la aplicación (interface)
customtkinter.set_default_color_theme("blue")

# Create CTk window
app = customtkinter.CTk()
# Set window size
app.geometry("490x595")

def desktop():
    frame = customtkinter.CTkFrame(master=app)
    frame.grid(row=0, column=0, sticky="nsew")
    frame2 = customtkinter.CTkFrame(master=app)
    frame2.grid(row=0, column=1, sticky="nsew")
    frame3 = customtkinter.CTkFrame(master=app)
    frame3.grid(row=1, column=0, columnspan=2, sticky="nsew")
    # Configurar el peso de las columnas para que se expandan
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=0)

    # Tamaño de la población
    label_size_people_title = customtkinter.CTkLabel(master=frame, text="TAMAÑO DE LA POBLACIÓN", font=("Inter", 14, "bold"))
    label_size_people_title.grid(row=0, column=0, columnspan=3, pady=(10, 0), padx=(12, 0))

    label_initial_people = customtkinter.CTkLabel(master=frame, text="INICIAL", font=("Inter", 12, "bold"))
    label_initial_people.grid(row=1, column=0, pady=(10, 0), padx=(12, 5)) 
    initial_people = customtkinter.CTkEntry(master=frame, placeholder_text="1")
    initial_people.grid(row=1, column=1, pady=(10, 0), padx=(12, 5))

    label_max_people = customtkinter.CTkLabel(master=frame, text="MÁXIMA", font=("Inter", 12, "bold"))
    label_max_people.grid(row=2, column=0, pady=(10, 20), padx=(12, 5)) 
    max_people = customtkinter.CTkEntry(master=frame, placeholder_text="2")
    max_people.grid(row=2, column=1, pady=(10, 20), padx=(12, 5))

    # Valores de A y B
    label_ab_value_title = customtkinter.CTkLabel(master=frame2, text="VALORES DE A Y B", font=("Inter", 14, "bold"))
    label_ab_value_title.grid(row=0, column=0, columnspan=3 ,pady=(10, 0), padx=(10, 0)) 

    label_initial_people = customtkinter.CTkLabel(master=frame2, text="INFERIOR (A)", font=("Inter", 12, "bold"))
    label_initial_people.grid(row=1, column=0, pady=(10, 0), padx=5) 
    variable_a = customtkinter.CTkEntry(master=frame2, placeholder_text="1")
    variable_a.grid(row=1, column=1, pady=(10, 0), padx=5) 

    label_initial_people = customtkinter.CTkLabel(master=frame2, text="SUPERIOR (B)", font=("Inter", 12, "bold"))
    label_initial_people.grid(row=2, column=0, pady=(10, 0), padx=5) 
    variable_b = customtkinter.CTkEntry(master=frame2, placeholder_text="2")
    variable_b.grid(row=2, column=1, pady=(10, 0), padx=5) 

    # Probabilidades
    label_prob_title = customtkinter.CTkLabel(master=frame3, text="PROBABILIDADES", font=("Inter", 14, "bold"))
    label_prob_title.grid(row=0, column=0, columnspan=3 ,pady=(10, 0), padx=(25, 0)) 

    label_prop_crossing = customtkinter.CTkLabel(master=frame3, text="PROBABILIDADAD DE CRUZA", font=("Inter", 12, "bold"))
    label_prop_crossing.grid(row=1, column=0, pady=(10, 0), padx=(25, 0)) 
    prob_of_crossing = customtkinter.CTkEntry(master=frame3, placeholder_text="1")
    prob_of_crossing.grid(row=1, column=1, pady=(10, 0), padx=(25, 0)) 
    percent1 = customtkinter.CTkLabel(master=frame3, text="%", font=("Inter", 14, "bold"))
    percent1.grid(row=1, column=2 ,pady=(10, 0))

    label_prob_mut_ind = customtkinter.CTkLabel(master=frame3, text="PROBABILIDAD DE MUTACIÓN DEL INDIVIDUO", font=("Inter", 12, "bold"))
    label_prob_mut_ind.grid(row=2, column=0, pady=(10, 0), padx=(25, 0)) 
    prob_mut_ind = customtkinter.CTkEntry(master=frame3, placeholder_text="2")
    prob_mut_ind.grid(row=2, column=1, pady=(10, 0), padx=(25, 0)) 
    percent2 = customtkinter.CTkLabel(master=frame3, text="%", font=("Inter", 14, "bold"))
    percent2.grid(row=2, column=2 ,pady=(10, 0))

    label_prob_mut_gen = customtkinter.CTkLabel(master=frame3, text="PROBABILIDAD DE MUTACIÓN DEL GEN", font=("Inter", 12, "bold"))
    label_prob_mut_gen.grid(row=3, column=0, pady=(10, 0), padx=(25, 0)) 
    prob_mut_gen = customtkinter.CTkEntry(master=frame3, placeholder_text="2")
    prob_mut_gen.grid(row=3, column=1, pady=(10, 0), padx=(25, 0)) 
    percent3 = customtkinter.CTkLabel(master=frame3, text="%", font=("Inter", 14, "bold"))
    percent3.grid(row=3, column=2 ,pady=(10, 0))

    # Configuraciones adicionales
    label_additional_config_title = customtkinter.CTkLabel(master=frame3, text="CONFIGURACIONES ADICIONALES", font=("Inter", 14, "bold"))
    label_additional_config_title.grid(row=4, column=0, columnspan=3 ,pady=(10, 0)) 

    label_function = customtkinter.CTkLabel(master=frame3, text="f(x)", font=("Inter", 12, "bold"))
    label_function.grid(row=5, column=0, pady=(10, 0), padx=(0, 0))
    function_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="1", width=180)
    function_entry.grid(row=5, column=1, pady=(10, 0), padx=(0, 15)) 

    label_delta_x = customtkinter.CTkLabel(master=frame3, text="RESOLUCIÓN DESEADA", font=("Inter", 12, "bold"))
    label_delta_x.grid(row=6, column=0, pady=(10, 0), padx=(25, 0)) 
    delta_x = customtkinter.CTkEntry(master=frame3, placeholder_text="2")
    delta_x.grid(row=6, column=1, pady=(10, 0), padx=(25, 0)) 

    label_iterator = customtkinter.CTkLabel(master=frame3, text="NÚMERO DE ITERACIONES", font=("Inter", 12, "bold"))
    label_iterator.grid(row=7, column=0, pady=(10, 20), padx=(25, 0)) 
    iterator_entry = customtkinter.CTkComboBox(master=frame3, values=["Minimización", "Maximización"])
    iterator_entry.grid(row=7, column=1, pady=(10, 20), padx=(25, 0)) 

    button = customtkinter.CTkButton(master=app, text="INICIAR", command=lambda: 
                                    logic.reception_of_values(initial_people, 
                                                    max_people, 
                                                    variable_a, 
                                                    variable_b, 
                                                    prob_of_crossing, 
                                                    prob_mut_ind, 
                                                    prob_mut_gen, 
                                                    function_entry, 
                                                    delta_x, 
                                                    iterator_entry))
    button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


def change_window():
    # Ocultar la ventana actual
    app.withdraw()

    # Crear y mostrar la nueva ventana
    nueva_ventana = tkinter.Toplevel(app)
    NuevaVentana(nueva_ventana)

class NuevaVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Nueva Ventana")

        # Botón para volver a la ventana principal
        btn_volver = customtkinter.CTkButton(root, text="Volver a Ventana Principal", command=self.volver_a_principal)
        btn_volver.pack(pady=20)

    def volver_a_principal(self):
        # Ocultar la ventana actual
        self.root.withdraw()

        # Mostrar la ventana principal
        app.deiconify()

btn_change_window = customtkinter.CTkButton(master=app, text="Cambiar Ventana", command=change_window)
btn_change_window.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

desktop()
app.mainloop()
