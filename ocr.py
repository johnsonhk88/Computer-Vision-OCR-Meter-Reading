import cv2
import pytesseract
from pytesseract import Output
 

color_xWidth = 1280
color_xHeight = 720
cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, color_xWidth)  
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, color_xHeight)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 10)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret :
        # d = pytesseract.image_to_data(frame, output_type=Output.DICT, config='digits')
        gray = get_grayscale(frame)
        text = pytesseract.image_to_string(gray, config='digits')
        print("Text: ", text)
        # ocr_result = pytesseract.image_to_string(gray, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        # print("number: ", ocr_result)
        # d = pytesseract.image_to_data(gray, output_type=Output.DICT)
        # # n_boxes = len(d['text'])
        # n_boxes = len(d["text"])
        # print(d)
        # for i in range(n_boxes):
        #     if int(d['conf'][i]) > 60:
        #         (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        #         # don't show empty text
        #         if text and text.strip() != "":
        #             frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #             frame = cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
 
        # Display the resulting frame
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()