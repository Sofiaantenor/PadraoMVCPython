import os
from typing import Dict, Tuple

class PeopleRegisterView:
    def registry_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')

        new_person_informations = {
            "name": name, "age": age, "height": height
        }

        return new_person_informations


    def registry_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuario cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["name"] }
                Idade: { message["attributes"]["age"] }
        '''
        print(success_message)


    def registry_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar usuario!

            Erro: { error }
        '''
        print(fail_message)

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Determine o nome da pessoa para busca: ')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations

    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuario encontrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Name: { message["infos"]["name"] }
                Age: { message["infos"]["age"] }
                Height: { message["infos"]["height"] }
        '''
        print(success_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar usuario!

            Erro: { error }
        '''
        print(fail_message)

    def find_person_by_age_and_height_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa por Idade e Altura \n\n')
        try:
            min_age = int(input('Digite a idade mínima: '))
            max_age = int(input('Digite a idade máxima: '))
            min_height = float(input('Digite a altura mínima (em metros): '))
            max_height = float(input('Digite a altura máxima (em metros): '))
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            return {}

        person_finder_informations = {
            "min_age": min_age,
            "max_age": max_age,
            "min_height": min_height,
            "max_height": max_height
        }

        return person_finder_informations
