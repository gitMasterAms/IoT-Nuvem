
-----

### Código-fonte para o seu arquivo `README.md`:

```markdown
# 📡 Controle de Radar: Da Área de Trabalho para a Web 🚀

### Uma interface web moderna para controlar um radar via Arduino com Flask.

![Gif da Interface Web em Ação](https://placehold.co/800x400/1a202c/9f7aea?text=Insira+um+GIF+do+seu+projeto+aqui!)
> ✨ **Dica:** Grave um GIF da tela para mostrar seu projeto funcionando! Ferramentas como [ScreenToGif](https://www.screentogif.com/) ou [LiceCap](https://www.cockos.com/licecap/) são ótimas para isso.

---

## 🎯 O Que é Este Projeto?

Este projeto é uma modernização de um aplicativo de controle de radar. A aplicação original, baseada em uma interface gráfica desktop com Tkinter, foi completamente migrada para uma **plataforma web utilizando Flask**.

O objetivo é permitir o controle de um sistema de radar (conectado a um Arduino) através de qualquer navegador, oferecendo uma experiência de usuário mais flexível, acessível e moderna.

## ⚙️ Como Funciona?

A arquitetura conecta a interface web ao hardware físico de forma simples e eficiente:

```

[ Usuário no Navegador ]
|
(Envia coordenadas H/V via HTTP)
|
v
[   Servidor Flask (Python)   ]
|
(Usa a biblioteca PySerial)
|
v
[      Porta Serial (COM5)      ]
|
(Envia e recebe dados: "15.2 -8.1\\n")
|
v
[         Arduino UNO         ]
|
(Controla os motores do radar)
|
v
[      Máquina Física (Radar)      ]

````

1.  **Frontend (Interface de Controle):** Uma página web limpa, construída com HTML e Tailwind CSS, onde o usuário digita as distâncias horizontal e vertical.
2.  **Backend (Servidor Flask):** O servidor em Python recebe os dados do navegador, valida as coordenadas (H: -20 a 20, V: -12 a 12) e os formata para envio.
3.  **A Ponte (PySerial):** Esta biblioteca é a responsável por "traduzir" os comandos do Python para a linguagem que o Arduino entende, enviando-os pela porta serial.
4.  **Hardware (Arduino):** O microcontrolador recebe os comandos e aciona os motores para posicionar o radar com precisão. Ele também pode enviar mensagens de status de volta para o log da aplicação.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python, Flask
-   **Comunicação Hardware:** PySerial
-   **Frontend:** HTML5, Tailwind CSS
-   **Hardware:** Arduino

---

## 🚀 Mão na Massa: Rodando o Projeto Localmente

Siga os passos abaixo para executar a aplicação na sua máquina.

### Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/) instalado.
-   Um Arduino com o código de controle já carregado na placa.
-   Git para clonar o projeto.

### Passo 1: Clone o Repositório

Abra seu terminal e clone este projeto para a sua máquina.

```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
````

### Passo 2: Ative o Ambiente Virtual `virtualIoTNuvem`

Este projeto já possui um ambiente virtual configurado na pasta `virtualIoTNuvem`. Você só precisa ativá-lo.

**Para ativar no Windows:**

```bash
.\virtualIoTNuvem\Scripts\activate
```

**Para ativar no macOS/Linux:**

```bash
source virtualIoTNuvem/bin/activate
```

*Após a ativação, o nome `(virtualIoTNuvem)` aparecerá no início do seu terminal.*

### Passo 3: Instale as Dependências

Com o ambiente virtual ativo, instale os pacotes Python necessários.

```bash
pip install Flask pyserial
```

### Passo 4: Configure a Porta Serial (❗ Passo Crucial\!)

1.  Conecte seu Arduino ao computador.
2.  Verifique em qual porta (ex: `COM5` no Windows ou `/dev/ttyUSB0` no Linux) ele está conectado.
3.  Abra o arquivo `views.py` e **confirme se a variável `PORTA_SERIAL`** está configurada com a porta correta.

<!-- end list -->

```python
# views.py
# ...
PORTA_SERIAL = 'COM5'  # <-- VERIFIQUE E ALTERE ESTA LINHA SE NECESSÁRIO
# ...
```

### Passo 5: Inicie o Servidor Flask

Com tudo configurado, inicie a aplicação.

```bash
python app.py
```

O terminal deverá exibir mensagens indicando que o servidor está rodando e que a conexão com a porta serial foi bem-sucedida.

### Passo 6: Acesse a Interface de Controle

Abra seu navegador e acesse o endereço:

[http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)

Você verá a interface de controle do radar. Teste enviando algumas coordenadas e o comando de retorno\!

-----

## 📂 Estrutura do Projeto

```
/
├── app.py              # Inicia o servidor Flask.
├── views.py            # Contém as rotas e toda a lógica de comunicação com o Arduino.
├── virtualIoTNuvem/    # Pasta do ambiente virtual com as dependências do projeto.
├── templates/
│   └── index.html      # A interface web que o usuário vê.
└── README.md           # Este arquivo que você está lendo.
```

-----

Feito com ❤️ por [Seu Nome Aqui].

```
```