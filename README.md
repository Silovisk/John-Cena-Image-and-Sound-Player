# John Cena Image and Sound Player

Este projeto consiste em um código Python que reproduz uma imagem e um som do John Cena quando certas teclas são pressionadas. O código é baseado nas bibliotecas pynput, PIL, threading, tkinter e pygame, e permite interagir com a interface gráfica ao pressionar as teclas específicas.

## Funcionalidades

- Ao pressionar as teclas 'c', 'e', 'n' ou 'a', uma imagem e um som do John Cena serão reproduzidos.
- A imagem é exibida em uma janela redimensionada para se ajustar ao tamanho definido.
- A janela possui um fundo cinza e um título exibido como "JOHN CENA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".
- A imagem é carregada a partir do arquivo "JC_image.jpg" no diretório "app/medias" e redimensionada para 620x400 pixels.
- O ícone da janela é definido pelo arquivo "JC_icone.ico" no diretório "app/medias".
- O som do John Cena é reproduzido a partir do arquivo "Jhon_cena.mp3" no diretório "app/medias".
- A reprodução do som é controlada pela biblioteca pygame.
- Ao pressionar as teclas específicas, a imagem e o som são reproduzidos repetidamente em um loop de 20 vezes.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas pynput, PIL, tkinter e pygame instaladas

Você pode instalar as bibliotecas necessárias executando o seguinte comando no terminal:

```
pip install pynput pillow pygame
```

Certifique-se de executar o comando acima no ambiente Python em que você está executando o projeto.

## Como usar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente Python.
3. Execute o arquivo `john_cena_player.py`.
4. Pressione as teclas 'c', 'e', 'n' ou 'a' para reproduzir a imagem e o som do John Cena.

**Nota:** Certifique-se de que a imagem "JC_image.jpg", o ícone "JC_icone.ico" e o arquivo de áudio "Jhon_cena.mp3" estejam localizados no diretório "app/medias" para que o programa funcione corretamente.

## Contribuição

Contribuições para aprimorar o projeto são bem-vindas! Sinta-se à vontade para abrir problemas e enviar solicitações de pull.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
