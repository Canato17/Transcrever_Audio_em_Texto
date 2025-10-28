# 🗣️ Transcrição Automática de Áudio com Whisper

Este projeto permite converter **arquivos de áudio em texto** de forma automática, utilizando o modelo de inteligência artificial **Whisper**, desenvolvido pela OpenAI.

O sistema é composto por **dois arquivos principais**, que trabalham em conjunto para facilitar o uso — bastando **arrastar o áudio sobre o atalho `.bat`**.

---

## ⚙️ Estrutura dos Arquivos

### 🟢 `Executar_Transcricao.bat`
Arquivo de inicialização.  
O usuário deve **arrastar o arquivo de áudio** (por exemplo, `.mp3`, `.wav`, `.m4a`) **sobre este item**.  
Esse script executa automaticamente o processo e envia o arquivo de áudio para o segundo programa, que fará a transcrição.

---

### 🧠 `transcrever_melhor.py`
Script principal responsável por:
- Carregar o modelo **Whisper “large”** (para transcrição de alta qualidade em português);
- Realizar a **transcrição automática** do áudio em texto;
- Gerar dois arquivos de saída:
  - `*_TRANSCRICAO_MELHOR.txt` → texto completo da transcrição;
  - `*_LEGENDA.srt` → legenda com marcação de tempo (opcional).

Durante o processo, o script exibe mensagens informativas sobre o progresso da transcrição.

---

## 🚀 Como Utilizar

1. **Coloque os dois arquivos na mesma pasta.**
2. **Arraste o áudio desejado sobre o arquivo `Executar_Transcricao.bat`.**
3. Aguarde — o modelo Whisper será carregado e a transcrição iniciará automaticamente.
4. Ao término, serão gerados arquivos `.txt` e `.srt` na mesma pasta do áudio original.

---

## 📦 Requisitos

- **Python 3.9+**
- Biblioteca **OpenAI Whisper**  
  Instalação:
  ```bash
  pip install -U openai-whisper

# ffmpeg (necessário para leitura dos arquivos de áudio)
Instalação (Windows):

choco install ffmpeg

ou baixe em: https://ffmpeg.org/download.html

--- 

## 💡 Observações Importantes

O modelo “large” do Whisper oferece maior precisão, mas consome mais memória e tempo.
Caso o computador seja mais modesto, é possível editar o código e substituir:

modelo_escolhido = "large"

por:

modelo_escolhido = "small"  # ou "base"


Os arquivos de saída são salvos automaticamente no mesmo diretório do áudio original.

O script suporta áudios em português, mas pode ser ajustado para outros idiomas.
---

## 👩‍💻 Autoria

Desenvolvido por Isabella
