from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def crear_pdf_guia():
    archivo_pdf = "Guia_Desarmando_Pandas.pdf"
    doc = SimpleDocTemplate(
        archivo_pdf,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    titulo_style = ParagraphStyle(
        'TituloPDF',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=15
    )
    
    seccion_style = ParagraphStyle(
        'SeccionPDF',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0f766e"),
        spaceBefore=12,
        spaceAfter=6
    )
    
    codigo_style = ParagraphStyle(
        'CodigoPDF',
        fontName='Courier-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f1f5f9"),
        borderColor=colors.HexColor("#cbd5e1"),
        borderWidth=1,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )

    texto_style = ParagraphStyle(
        'TextoPDF',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )

    story = []

    # Encabezado
    story.append(Paragraph("📘 Guía Práctica: Desarmando Pandas desde Cero", titulo_style))
    story.append(Paragraph("Aprende la lógica detrás de cada comando para escribir código de forma independiente.", texto_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0f766e"), spaceAfter=15))

    # Concepto 1
    story.append(Paragraph("1. ¿Qué significan las importaciones?", seccion_style))
    story.append(Paragraph("<b>Código:</b>", texto_style))
    story.append(Paragraph("import pandas as pd<br/>import matplotlib.pyplot as plt", codigo_style))
    story.append(Paragraph("• <b>import pandas:</b> Trae la librería especializada en tablas y análisis de datos.<br/>• <b>as pd:</b> Le crea un apodo corto (<i>alias</i>) para no tener que escribir 'pandas' en cada línea.<br/>• <b>import matplotlib.pyplot as plt:</b> Trae el módulo de gráficos y le pone de apodo 'plt'.", texto_style))

    # Concepto 2
    story.append(Paragraph("2. ¿Qué es 'df'?", seccion_style))
    story.append(Paragraph("<b>Código:</b>", texto_style))
    story.append(Paragraph("df = pd.DataFrame(datos)", codigo_style))
    story.append(Paragraph("• <b>df</b> significa <b>DataFrame</b>. Es el nombre estándar que le damos a la variable donde guardamos nuestra tabla (filas y columnas, igual que una hoja de Excel).", texto_style))

    # Concepto 3
    story.append(Paragraph("3. ¿Cómo funciona el filtro de corchetes?", seccion_style))
    story.append(Paragraph("<b>Código:</b>", texto_style))
    story.append(Paragraph("stock_critico = df[ df['Stock'] &lt; 10 ]", codigo_style))
    story.append(Paragraph("• <b>La pregunta interna:</b> <i>df['Stock'] &lt; 10</i> revisa fila por fila y devuelve Verdadero/Falso.<br/>• <b>El colador externo:</b> <i>df[...]</i> toma la tabla completa y deja pasar únicamente las filas que dieron <b>Verdadero</b>.<br/>• <b>Asignación:</b> Guardamos ese resultado colado en la nueva variable <i>stock_critico</i>.", texto_style))

    # Concepto 4
    story.append(Paragraph("4. Agrupaciones con .groupby() y .reset_index()", seccion_style))
    story.append(Paragraph("<b>Código:</b>", texto_style))
    story.append(Paragraph("resumen = df.groupby('Sucursal')['Facturacion'].sum().reset_index()", codigo_style))
    story.append(Paragraph("• <b>df.groupby('Sucursal'):</b> Junta los datos en 'bolsas' según la provincia.<br/>• <b>['Facturacion']:</b> Especifica qué columna de números queremos calcular.<br/>• <b>.sum():</b> Aplica la operación de suma a cada bolsa (usamos <i>.mean()</i> si queremos promedio).<br/>• <b>.reset_index():</b> <u>¡Muy importante!</u> Convierte el resultado agrupado de nuevo en un DataFrame limpio con columnas normales.", texto_style))

    # Concepto 5
    story.append(Paragraph("5. Regla de Oro de los Paréntesis ()", seccion_style))
    story.append(Paragraph("• Si la palabra <b>hace una acción</b> (sumar, promediar, reiniciar índice, guardar), lleva paréntesis: <i>.sum()</i>, <i>.mean()</i>, <i>.reset_index()</i>, <i>.to_csv()</i>.<br/>• Si te faltan los paréntesis, Python no ejecuta la acción y te dará errores como <i>TypeError: 'method' object is not subscriptable</i>.", texto_style))

    # Generar
    doc.build(story)
    print("✨ PDF 'Guia_Desarmando_Pandas.pdf' generado con éxito.")

if __name__ == "__main__":
    crear_pdf_guia()
    