import numpy as np
import cv2

while True:
    print('*'*30)
    print('MANIPULACAO DE IMAGENS: ')
    print(f'{"":<5} 1) TRANSLACAO')
    print(f'{"":<5} 2) ROTACAO')
    print(f'{"":<5} 3) ESCALA')
    print(f'{"":<5} 4) CLIPPING')
    print(f'{"":<5} 0) Sair')

    while True:
        escolha = int(input('opcao: '))
        if escolha in range(0,5):
            if(escolha == 1):
                imagem = cv2.imread("imagens/openCVPython.png")
                print(imagem.shape)
                altura, largura = imagem.shape[:2]
                cv2.imshow("Original", imagem)
                cv2.waitKey(0)

                print('TRANSLACAO')
                #translacao (deslocamento)
                deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])
                deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
                cv2.imshow("Baixo e direita", deslocado)
                cv2.waitKey(0)

                deslocamento = np.float32([[1, 0, -50], [0, 1, -90]])
                deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
                cv2.imshow("Cima e esquerda", deslocado)
                cv2.waitKey(0)

            if escolha == 2:
                #Lendo a imagem
                imagem = cv2.imread("imagens/openCVPython.png")
                print(imagem.shape)
                #Obtendo a altura e largura da imagem
                altura, largura = imagem.shape[:2]
                cv2.imshow("Original", imagem)
                cv2.waitKey(0)

                print('rotacao')
                #Obtendo o centro da imagem
                ponto = (largura / 2, altura / 2) 

                #Obtendo a matriz de rotacao - Rotacao de 45graus
                rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)

                #Rotacionando a imagem
                rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))

                cv2.imshow("Rotacionado 45 graus", rotacionado)
                cv2.waitKey(0)
                cv2.imwrite('Rotacao45.png', rotacionado)


                #Obtendo a matriz de rotacao - Rotacao de 120 graus
                rotacao = cv2.getRotationMatrix2D(ponto, 120, 1.0)
                #Rotacionando imagem
                rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
                cv2.imshow("Rotacionado 120 graus", rotacionado)
                cv2.waitKey(0)
                cv2.imwrite('Rotacao120.png', rotacionado)


                ponto = (0, altura)
                rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
                rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))

                cv2.imshow("45 graus com ponto embaixo", rotacionado)
                #Esperando alguma tecla
                cv2.waitKey(0)
               

            if escolha == 3:
                print('ESCALA')
                # Abrindo a imagem
                imagem = cv2.imread("imagens/openCVPython.png")
                print(imagem.shape)
                altura, largura = imagem.shape[:2]
                #Mostrando a imagem
                cv2.imshow("Original", imagem)
                cv2.waitKey(0)

                imagem = cv2.imread("imagens/openCVPython.png")
                #Carregando uma imagem em escala  de cinza
                imagem = cv2.imread("imagens/openCVPython.png",0)

                gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Escla de cinza image', gray_img)
                cv2.waitKey(0)

            if escolha == 4:
                print('CLIPPING')
                imagem = cv2.imread("imagens/openCVPython.png")
                print(imagem.shape)
                altura, largura = imagem.shape[:2]
                cv2.imshow("Original", imagem)
                cv2.waitKey(0)

                #Abrindo a imagem
                imagem = cv2.imread('imagens/openCVPython.png')
                #copiando a parte da imagem
                y=0
                x=0
                h=100
                w=200
                crop = imagem[y:y+h, x:x+w]
                # crop = imagem[00:200, 80:150]
                #Mostrando a copia 
                cv2.imshow('Image', crop)
                #Salvando a imagem copiada
                cv2.imwrite('copia.png', crop)

                cv2.waitKey(0) 
                cv2.destroyAllWindows()

            if escolha == 0 :
                print('SAIU!!!')
                break
        print('Numero invalido')

        while True:
            resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if resp in 'SN':
                break
            print('Insira SIM ou Nao [S/N]')
        if resp == 'N':
            break
        
    if escolha == 0 or resp == 'N':
        break










