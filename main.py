import cv2
from win32com import client
print("First Put the Image in the Project Folder and Select Further Configurations...")
speaker=client.Dispatch("SAPI.SpVoice")
speaker.Speak("First Put the Image in the Project Folder and Select Further Configurations")
speaker.Speak("Enter Image Name with Extension.")
try:
    source=input("Enter Image Name with Extension.. ")
    speaker.Speak("Enter New Image Name with Extension")
    destination=input("Enter New Image Name with Extension.. ")
    speaker.Speak("Enter Scale Percent for the Image")
    scale_Percent=int(input("Enter Scale Percent for the Image.. "))
    while True:
        print("Enter 1 for Resize only...")
        speaker.Speak("Enter 1 for Resize only")
        print("Enter 2 for Resize + View")
        speaker.Speak("Enter 2 for Resize and to Display too. ")
        options=int(input(""))
        if(options==1):
            sourceimage=cv2.imread(source,cv2.IMREAD_UNCHANGED)
            newWidth=int(sourceimage.shape[1]*scale_Percent/100)
            newHeight=int(sourceimage.shape[0]*scale_Percent/100)
            output=cv2.resize(sourceimage,(newWidth,newHeight))
            cv2.imwrite(destination,output)
            break
        
        elif(options==2):
            sourceimage=cv2.imread(source,cv2.IMREAD_UNCHANGED)
            newWidth=int(sourceimage.shape[1]*scale_Percent/100)
            newHeight=int(sourceimage.shape[0]*scale_Percent/100)
            output=cv2.resize(sourceimage,(newWidth,newHeight))
            cv2.imwrite(destination,output)
            cv2.imshow(destination,output)
            cv2.waitKey(0)
            break
            
        else:
            print("Please Select a Valid Option...")
            speaker.Speak("Please Select a Valid Option")
except Exception as e:
    speaker.Speak("Something Went Wrong. Please Restart the Program with Valid Configurations.")
    print(f"Something Went Wrong due to {e}")
    
    
  


