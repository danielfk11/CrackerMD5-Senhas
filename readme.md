Linguagem utilizada 

    Python 3.6

Imports  

    import hashlib
    import os 
    

Ao abrir o codigo ele vai perguntar se quer testar o programa com uma senha no modo string 

    (Ex: daniel123, teste, senhas12345) 
    
No modelo MD5 
    
    e8d95a51f3af4a3b134bf6bb680a213a(teste)       
    b5ea8985533defbf1d08d5ed2ac8fe9b(daniel123)


Wordlist

    Caso escreva o nome de uma wordlist que nao esteja no arquivo ele nao ira reconhecer e ira printar na tela as opcoes de wordlists disponiveis.

    Dentro da pasta /worlists tem outras wordlists, entretando para poder usar deve tirar ela de dentro na pasta ja que o windows nao permite acessar arquivos em pastas com o python.

Como funciona?

    *1* ao digitar uma palavra(senha) ele ira transformar em MD5 e procurar na wordlist 
    *2* selecione o modelo ja em MD5 para procurar na wordlist

ao encontrar ele notifica dizendo que a senha foi encontrada.

