from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def mostrar_venn_con_elementos(conjunto1, conjunto2, etiqueta1='Conjunto A', etiqueta2='Conjunto B', titulo='Diagrama de Venn'):
    venn = venn2([conjunto1, conjunto2], set_labels=(etiqueta1, etiqueta2))
    plt.title(titulo)

    # Reemplazar los textos automáticos por los elementos reales
    if venn.get_label_by_id('10'):
        venn.get_label_by_id('10').set_text('\n'.join(map(str, conjunto1 - conjunto2)))
    if venn.get_label_by_id('01'):
        venn.get_label_by_id('01').set_text('\n'.join(map(str, conjunto2 - conjunto1)))
    if venn.get_label_by_id('11'):
        venn.get_label_by_id('11').set_text('\n'.join(map(str, conjunto1 & conjunto2)))

    plt.show()
