def calcular_subnetting():
  """
  Função interativa para calcular as colunas da tabela de subnetting.
  """

  # 1. Pegar o endereço de rede e a máscara de rede do usuário
  rede_bin = input("Digite o endereço de rede e a máscara de rede (ex: 50.0.0.0/14): ")
  # Validar o formato da entrada
  if not validar_formato(rede_bin):
    print("Formato de entrada inválido!")
    return

  rede_bin, mascara_bin = rede_bin.split("/")
  rede_bin = bin(int(rede_bin.split(".")[0]))[2:].zfill(8) + "." \
             bin(int(rede_bin.split(".")[1]))[2:].zfill(8) + "." \
             bin(int(rede_bin.split(".")[2]))[2:].zfill(8) + "." \
             bin(int(rede_bin.split(".")[3]))[2:].zfill(8)
             
  bits_subnetting = int(mascara_bin)
  print("-" * 40)
  print(f"Endereço de rede: {2 ** (32)}", rede_bin_dec)
  print("Máscara de rede (binário):", mascara_bin)
  print("-" * 40)
  print(f"Quantidade de bits reservados para subnetting: {int(mascara_bin)}")
  print(f"Quantidade de redes: {2 ** (32 - bits_subnetting)}")
  print(f"Quantidade de hosts válidos: {2 ** (32 - bits_subnetting) -2}")
  print(f"Início da rede: {"." .}")
  print("Fim da rede:", fim_rede_dec)
  print("-" * 40)