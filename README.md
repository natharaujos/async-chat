# async-chat

  
  <h1>Chat Assíncrono em Python</h1>
  <p>
    Este projeto é um exemplo de implementação de um chat assíncrono utilizando
    Python. O objetivo é demonstrar habilidades em programação assíncrona em
    Python, incluindo sockets e threads.
  </p>
  <h2>Tecnologias utilizadas</h2>
  <ul>
    <li>Python 3.6+</li>
    <li>socket</li>
    <li>threading</li>
  </ul>
  <h2>Funcionalidades</h2>
  <ul>
    <li>
      Implementação de um servidor de chat que aceita conexões de clientes.
    </li>
    <li>
      Implementação de um cliente de chat que se conecta ao servidor e envia e
      recebe mensagens.
    </li>
    <li>
      Uso de programação assíncrona para permitir a comunicação simultânea entre
      vários clientes e o servidor.
    </li>
    <li>
      Uso de threads para lidar com entrada de usuário e saída de console no
      cliente.
    </li>
  </ul>
  <h2>Como rodar o projeto</h2>
  <p>Para rodar o projeto localmente, siga os seguintes passos:</p>
  <ol>
    <li>Clone este repositório para o seu computador.</li>
    <li>Abra dois terminais e navegue até a pasta do projeto.</li>
    <li>
      Em um terminal, execute <code>python server.py</code> para iniciar o
      servidor.
    </li>
    <li>
      Em outro terminal, execute <code>python client.py</code> para iniciar o
      cliente.
    </li>
    <li>
      Digite o nome de usuário desejado e comece a enviar e receber mensagens.
    </li>
  </ol>
  <h2>Como utilizar o chat</h2>
  <p>O chat funciona de forma simples:</p>
  <ul>
    <li>
      O cliente se conecta ao servidor e envia uma mensagem de boas-vindas,
      incluindo o nome de usuário escolhido.
    </li>
    <li>
      O servidor adiciona o novo cliente à lista de usuários conectados e envia
      uma mensagem de boas-vindas a todos os clientes conectados.
    </li>
    <li>
      O cliente pode digitar uma mensagem e enviá-la ao servidor, que então
      encaminha a mensagem para todos os outros clientes conectados.
    </li>
  </ul>
