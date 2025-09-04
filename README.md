# Nome da Sua Aplicação Flask

Uma breve descrição sobre o que sua aplicação faz.

## 🚀 Como Rodar a Aplicação

Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local.

---

### Passo 1: Configurar o Ambiente Virtual

É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto. Isso evita conflitos com outras bibliotecas instaladas em seu sistema.

1.  **Navegue até o diretório do projeto** no seu terminal.
2.  **Crie o ambiente virtual** com o seguinte comando:
    ```bash
    python -m venv venv
    ```
    *Se estiver usando Python 3, o comando pode ser `python3 -m venv venv`.*
3.  **Ative o ambiente virtual**:
    * **No Windows**:
        ```bash
        venv\Scripts\activate
        ```
    * **No macOS e Linux**:
        ```bash
        source venv/bin/activate
        ```

Você saberá que o ambiente está ativo quando o nome `(venv)` aparecer no início da linha de comando.

---

### Passo 2: Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias para o projeto.

1.  Crie um arquivo chamado **`requirements.txt`** na raiz do seu projeto.
2.  Adicione as dependências listadas abaixo ao arquivo:
    ```
    Flask
    Flask-WTF
    ```
    *Se sua aplicação tiver outras dependências, como **`Pillow`** para manipular imagens ou **`SQLAlchemy`** para banco de dados, adicione-as aqui.*

3.  Agora, instale as dependências usando o `pip`:
    ```bash
    pip install -r requirements.txt
    ```

---

### Passo 3: Executar a Aplicação

Com todas as dependências instaladas, você pode iniciar a aplicação.

1.  **Certifique-se de que o ambiente virtual está ativado.** Se não estiver, use os comandos do **Passo 1**.
2.  Execute o arquivo principal da aplicação:
    ```bash
    python app.py
    ```
    *Ou `python3 app.py` se for o caso.*

A aplicação estará rodando no endereço `http://127.0.0.1:5000`. Abra seu navegador e acesse a URL para visualizar a página inicial.

Para parar a execução, pressione `CTRL + C` no terminal.

---

### Desativando o Ambiente Virtual

Quando terminar de trabalhar, você pode desativar o ambiente virtual digitando o seguinte comando:

```bash
deactivate