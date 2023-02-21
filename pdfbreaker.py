import os
import PyPDF2
import time

def pdfSplitter(input_file, start_page, end_page):
    with open(input_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        if start_page > pdf_reader.getNumPages() or end_page > pdf_reader.getNumPages():
            raise ValueError('Página de inicio o fin fuera de rango')
        pdf_writer = PyPDF2.PdfFileWriter()
        for i in range(start_page - 1, end_page):
            page = pdf_reader.getPage(i)
            pdf_writer.addPage(page)
        output_file = f'{os.path.splitext(input_file)[0]}_{start_page}-{end_page}.pdf'
        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
        print(f'Se ha guardado el archivo {output_file}')

def pdfMerger(input_files, output_file):
    pdf_readers = []
    for input_file in input_files:
        with open(input_file, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            pdf_readers.append(pdf_reader)

        pdf_writer = PyPDF2.PdfFileWriter()

        for pdf_reader in pdf_readers:
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
        print(f'Se ha guardado el archivo {output_file}')    


def menuSplitter():
    optionSplitter = input()
    boolSplitter = True
    while boolSplitter == True:
        print("--------------------------------------")
        print("USTED HA ELEGIDO LA OPCION SEPARAR PDF")
        print("--------------------------------------")
        print("seleccione la opcion que desee ejecutar")
        print("1) Separar pdf")
        print("2) Salir")
        if optionSplitter == 1:
            print ("ingrese el path o nombre de el archivo que desea separar")
            pathFileName = input()
            print("ingrese la pagina a partir de la cual quiere generar el pdf")
            startPage = int(input())
            print("ingrese la pagina hasta la cual quiere generar el pdf")
            endPage = int(input())
            pdfMerger(pathFileName, startPage, endPage)
        elif optionSplitter == 2:
            boolSplitter = False
        else:
            print ("opcion no valida")

def menuMerger():
    boolMerger = True
    while True:
        print("-----------------------------------")
        print("USTED HA ELEGIDO LA OPCION UNIR PDF")
        print("-----------------------------------")
        print("seleccione la opcion que desee ejecutar")
        print("1) Unir pdf")
        print("2) Salir")
        optionMerger = int(input())
        if optionMerger == 1:
            print ("ingrese la cantidad de archivos que desea unificar")
            m = int(input())
            filesToMerge = []
            for i in range(0, (m - 1)):
                print ("ingrese el path o la direccion del archivo")
                filesToMerge[0] = input()
            print("ingrese el nombre con el que desea llamar al archivo compilado")
            outputFileName = input()
            pdfMerger(filesToMerge, outputFileName)
            
        elif optionMerger == 2:
            boolMerger = False
        else:
            print ("opcion no valida")

def mainMenu():
    menuBool = True
    while menuBool == True:
        print("BIENVENIDO AL PDFBREAKER DE MANUEL NUÑEZ")
        print("elija la accion que desea realizar")
        print("1) Unir Pdf")
        print("2) Separar pdf")
        print("3) Salir")
        option = input()
        if option == 1:
            menuMerger()
        elif option == 2:
            menuSplitter()
        elif option == 3:
            print("esperamos vuelva pronto")
            time.sleep(5)
            menuBool = False
        else:
            print ("Opcion no valida")

mainMenu()