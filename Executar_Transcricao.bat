@echo off
chcp 65001 > nul
echo.
echo [Bot de Transcrição Melhorada]
echo.
echo Verificando se o arquivo foi solto...

if "%~1"=="" (
    echo ERRO: Nenhum arquivo foi arrastado para este executável.
    echo.
    echo Como usar: Arraste e solte um arquivo de audio sobre este icone.
    echo.
    pause
    exit /b 1
)

echo Arquivo a ser processado: %~1
echo.
echo Iniciando o script Python... Aguarde.
echo.

py "%~dp0transcrever_melhor.py" "%1"

if %errorlevel% neq 0 (
    echo.
    echo O script encontrou um erro! (Código: %errorlevel%)
    echo Verifique as mensagens acima.
) else (
    echo.
    echo Processamento concluido com sucesso!
)

echo.
pause