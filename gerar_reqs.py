import subprocess
import sys

print("Gerando o arquivo requirements.txt...")

try:
    # Pega o caminho exato para o executável do Python que o VS Code está usando
    python_executable = sys.executable

    # Executa o comando 'pip freeze' usando esse Python específico
    resultado = subprocess.run(
        [python_executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True,
        encoding='utf-8', # Adicionado para garantir a codificação correta
        check=True
    )

    # Salva a lista de pacotes no arquivo requirements.txt
    with open("requirements.txt", "w", encoding='utf-8') as f:
        f.write(resultado.stdout)

    print("Arquivo 'requirements.txt' criado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")