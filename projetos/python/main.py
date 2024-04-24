from veiculos import Veiculo
def Menu_Principal():
    print("""
          MWMWMWMWMWMWMWMMWWMMWMWMWMWMMWMWMWM
          ||  CONTROLE DE ESTACIONAMENTO    ||
          MWMWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMW
          || 1) TELA VEÍCULO                ||
          || 2) TELA ESTACIONAMENTO         ||
          || 3) TELA RELATÓRIO              ||
          || 4) SOBRE O PROJETO             ||
          || 0) FECHAR PROGRAMA             ||
          MWMWMWMWMWMWMWMMWMWMWMWMWMWMWMWMMWWM
          """)
    op = int(input("Escolha uma opção: "))
    return op

OP = Menu_Principal()

if OP == 1:
    Veiculo.Tela_Veiculo()