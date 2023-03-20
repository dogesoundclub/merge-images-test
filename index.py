from PIL import Image
import json

def main():
    try:
        for i in range(0, 10000):
            with open('./metadata/'+str(i)+'.json') as f:
                json_object = json.load(f)
                for j in range(len(json_object['attributes'])):
                    if(json_object['attributes'][j]['trait_type'] == 'Face'):
                        if(json_object['attributes'][j]['value'] == 'Male'):
                            Face = Image.open('./body/man.png')
                        if(json_object['attributes'][j]['value'] == 'Female'):
                            Face = Image.open('./body/girl.png')
                        if(json_object['attributes'][j]['value'] == 'Robot'):
                            Face = Image.open('./body/robot.png')
                        if(json_object['attributes'][j]['value'] == 'Tiger'):
                            Face = Image.open('./body/tiger.png')
                        if(json_object['attributes'][j]['value'] == 'Monkey'):
                            Face = Image.open('./body/monkey.png')
                        if(json_object['attributes'][j]['value'] == 'Rabbit'):
                            Face = Image.open('./body/rabbit.png')
                        (img_h, img_w) = Face.size
                        resize_back = Face.resize((img_h, img_w))
                        resize_back.paste(Face, (0, 0), Face)
                        resize_back.save("./matesbody/body-"+str(i)+".png","png")
                        print(str(i)+" 완료")
    except Exception:
        print('예외발생')
main()  