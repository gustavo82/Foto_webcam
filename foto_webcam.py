#instalar numpy e opencv-python

import cv2
webcam = cv2.VideoCapture(0)


if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        #aparecera tela com imagem webcam
        #cv2.imshow("Video da cam", frame)
        #key = cv2.waitKey(5) 
        # parar os frames em 5seg
        key = cv2.waitKey(5)
        if key == 27: # 27 = tecla esc
            break
    #salvara a foto
    cv2.imwrite("C:\Temp\Fotosalva.jpg", frame)
# fechar conexão com webcam
webcam.release() 

#garantir que imagem da da webcam fechara
#cv2.destroyAllWindows() 
