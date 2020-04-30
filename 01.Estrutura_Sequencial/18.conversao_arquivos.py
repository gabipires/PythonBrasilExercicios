tamanho_arquivo=int(input("Informe o tamanho do arquivo (em MB): "))
velocidade= int(input("Informe a velocidade de conexão (em Mbps): "))


velocidade_bytes=velocidade/8


tempo= tamanho_arquivo/velocidade_bytes
tempo_min = tempo/60
tempo_min=round(tempo_min,2)

print("Tempo aproximado de download:", tempo_min, "minutos")