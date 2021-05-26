#I have created this website
from django.http import HttpResponse
from django.http.response import FileResponse
from django.shortcuts import render
import cv2
import dlib
from mysite.filters import filter
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage



def home(request):
    return render(request,'index.html')
    #return HttpResponse('''<a>hi</a><img src="nose.png" alt="no img">''')

    
def about(request):
    fileObj=request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name,fileObj)
    filePathName = fs.url(filePathName)

    testimage='.'+filePathName
    
    #img=request.data.get('filename')
    img=cv2.imread(testimage)
    eye=request.POST.get('eye','default')
    nose=request.POST.get('nose','default')
    ear=request.POST.get('ear','default')
    detector = dlib.get_frontal_face_detector()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dlibfaces = detector(gray)
    predictor = dlib.shape_predictor("C://Users//ABHILASH REDDY//Desktop//Filters//shape_predictor_68_face_landmarks.dat")
    for face in dlibfaces:
        landmarks = predictor(gray, face)
        if(eye!='default'):
            img=filter.eye_filter(landmarks,img,eye)
        if(nose!='default'):
            img=filter.nose_filter(landmarks,img,nose)
        ### changes---------------------------------------------------------------------
        if(ear!='default'):
            img=filter.ear_filter(landmarks,img,ear)
    ret,jpeg=cv2.imencode('.jpg',img)
    im=jpeg.tobytes()
    return HttpResponse(im,content_type='image/png')


