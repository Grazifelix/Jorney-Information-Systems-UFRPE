# 09/06/21
# GRAZIELA MARIA
# PILHAS E FILAS
# EXEMPLO DE ENTRADA CORRETA: ( ( [ ] ) [ ( ) ] ) [ ( ) ] OU bsi [ ufrpe { recife ( dois ) mil } aaaa ] kkk
# ENTRADAS INCORRETAS: essa ( nao [ ta muito ) legal ] ne OU tem { coisa { a { mais } aqui } ne }kkkk}


input_text = input()
pilha_text = []
result = None

for i in range(0, len(input_text)):
    if input_text[i] in "([{":
        pilha_text.append(input_text[i])

    else:
        if input_text[i] in ")]}":
            if pilha_text == []:
                result = "casamento imperfeito"
                break
            else:
                if input_text[i] == ")" and pilha_text[-1] == "(": #-1 acessa o ultimo elemento
                    pilha_text.pop()

                elif input_text[i] == "]" and pilha_text[-1] == "[":
                    pilha_text.pop()

                elif input_text[i] == "}" and pilha_text[-1] == "{":
                    pilha_text.pop()

                else:
                    result = "casamento imperfeito"
                    break


if result is None:
    print("casamento perfeito")
else:
    print(result)


