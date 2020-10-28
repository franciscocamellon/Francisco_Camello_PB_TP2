# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 02 **************************
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Projeto de Bloco                                *
*        Professor       : Alcione Santos Dolavale                         *
*        Nome do arquivo : main.py                                         *
***************************************************************************/
"""

import psutil
# from validation import Validate

class Main():
    """ This function draws squares side by side. """

    def __init__(self):
        """ Constructor. """

        self.men = 0


    def memory(self):
        """ This function receives the input data from users. """

        self.men = psutil.virtual_memory()
        total = (self.men.total)/1024/1024/1024
        available = (self.men.available)/1024/1024/1024
        used = (self.men.used)/1024/1024/1024
        free = (self.men.free)/1024/1024/1024
        percent = self.men.percent
        print('  Memory','---' * 25, sep='\n')
        print('{1}Total physical memory: {0} Gb'.format(total,' '*3))
        print('{1}Total available memory: {0} Gb'.format(available,' '*3))
        print('{1}Total used memory: {0} Gb'.format(used,' '*3))
        print('{1}Memory percent used: {0} %'.format(percent,' '*3))
        print('{1}Total free memory: {0} Gb'.format(free,' '*3))



    def process_data(self):
        """ This function process the input data from init_class. """


    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'PC Analysis'.center(75), '===' * 25, sep='\n')
        self.memory()
        print('---' * 25, 'Analysis completed successfully!'.center(75), '---' *
              25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Main().print_result()
