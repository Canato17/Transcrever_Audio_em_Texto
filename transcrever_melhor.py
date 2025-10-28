# -*- coding: utf-8 -*-
import whisper
import os
import sys

def main():
    print("\n[🤖 BOT DE TRANSCRICAO AVANÇADO]")
    print("Transcrevendo com alta qualidade e segmentação interna...\n")
    
    # 1. OBTER O ARQUIVO DE ÁUDIO
    if len(sys.argv) > 1:
        caminho_original = sys.argv[1]
    else:
        caminho_original = input("Cole o caminho completo para o arquivo de áudio: ").strip('"')
    
    if not os.path.isfile(caminho_original):
        print(f"[ERRO] Arquivo não encontrado: '{caminho_original}'")
        input("Pressione Enter para sair...")
        return

    # 2. CONFIGURAÇÕES
    modelo_escolhido = "large"  # Use "large" para a melhor qualidade
    idioma = "pt" # Idioma Português

    # 3. CARREGAR O MODELO DE IA
    print(f"[🧠] Carregando o modelo '{modelo_escolhido}'. Aguarde, isso pode demorar...")
    model = whisper.load_model(modelo_escolhido)
    print("[✓] Modelo carregado com sucesso!\n")
    
    # 4. TRANSCREVER O ÁUDIO (O PRÓPRIO WHISPER GERENCIA OS SEGMENTOS)
    print("[🎧] Iniciando a transcrição. O Whisper dividirá o áudio internamente...")
    print("Isso pode levar MUITO tempo para um áudio longo. Aguarde...\n")
    
    # A chave aqui é o parâmetro 'segment_lengths'. O Whisper cuida de tudo.
    result = model.transcribe(
        caminho_original,
        language=idioma,
        fp16=False, # Importante para CPU
        verbose=True # Mostra o progresso detalhado na tela
    )
    
    # 5. SALVAR O ARQUIVO FINAL
    nome_base = os.path.splitext(caminho_original)[0]
    arquivo_final = nome_base + "_TRANSCRICAO_MELHOR.txt"
    
    with open(arquivo_final, 'w', encoding='utf-8') as f:
        f.write(result["text"])
    
    print(f"\n[✅ CONCLUÍDO!] Transcrição de alta qualidade salva em:")
    print(f"    {arquivo_final}")
    
    # Opcional: Salvar também com marcas de tempo (legenda)
    arquivo_legenda = nome_base + "_LEGENDA.srt"
    with open(arquivo_legenda, 'w', encoding='utf-8') as f:
        f.write(result["srt"])
    print(f"    Arquivo de legenda (SRT) salvo em: {arquivo_legenda}")
    
    input("\nPressione Enter para finalizar...")

if __name__ == "__main__":
    main()