class Veiculo():
    def Tela_Veiculo():
        print("""
            MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
            ||         TELA VEÍCULO           ||
            MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
            || 1) CADASTRAR VEÍCULO           ||
            || 2) LISTAR VEÍCULOS             ||
            || 3) ATUALIZAR VEÍCULO           ||
            || 4) EXCLUIR VEÍCULO             ||
            || 5) VOLTAR                      ||
            || 0) FECHAR PROGRAMA             ||
            MWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMMWWM
            """)
        op = int(input("Escolha uma opção: "))
        return op
    def Cadastrar_Veiculo():
        print("""
            MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
            ||       CADASTRAR VEICULO       ||
            MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
              """)
        proprietario = input("Proprietario: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
    def Listar_Veiculo():
        print("""
            MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
            ||        LISTAR VEÍCULO         ||
            MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
            || 1) LISTAR POR PLACA            ||
            || 2) LISTAR POR MARCA/MODELO     ||
            || 3) VOLTAR                      ||
            || 0) FECHAR PROGRAMA             ||
            MWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMMWWM
            """)
        op = int(input("Escolha uma opção: "))
        return op
    def Atualizar_Veiculo():
        print("""
            MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
            ||       ATUALIZAR VEICULO       ||
            MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
              """)
   
        placa = input("Placa: ")
    
    def Excluir_Veiculo():
        print("""
            MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
            ||        EXCLUIR VEICULO        ||
            MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
              """)
   
        placa = input("Placa: ")