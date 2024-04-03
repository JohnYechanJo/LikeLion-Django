from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    return render(request, "homepage.html")

def specifiedPost(request):
    restaurantPlace=request.GET.get("restaurantPlace")
    restaurantName=request.GET.get("restaurantName")
    openDate=request.GET.get("openDate")
    useStartTime=request.GET.get("useStartTime")
    useEndTime=request.GET.get("useEndTime")
    breakStartTime=request.GET.get("breakStartTime")
    breakEndTime=request.GET.get("breakEndTime")
    foodType=request.GET.get("foodType")
    restaurantNumber=request.GET.get("restaurantNumber")
    url=request.GET.get("url")
    return render(request, "specifiedPost.html",
                  {"restaurantPlace": restaurantPlace,
                   "restaurantName": restaurantName,
                   "openDate": openDate,
                   "useStartTime": useStartTime,
                   "useEndTime": useEndTime,
                   "breakStartTime": breakStartTime,
                   "breakEndTime": breakEndTime,
                   "foodType": foodType,
                   "restaurantNumber": restaurantNumber,
                   "url": url,
                   })

def writePost(request):
    restaurantPlace=request.GET.get("restaurantPlace")
    restaurantName=request.GET.get("restaurantName")
    openDate=request.GET.get("openDate")
    useStartTime=request.GET.get("useStartTime")
    useEndTime=request.GET.get("useEndTime")
    breakStartTime=request.GET.get("breakStartTime")
    breakEndTime=request.GET.get("breakEndTime")
    foodType=request.GET.get("foodType")
    restaurantNumber=request.GET.get("restaurantNumber")
    url=request.GET.get("url")

    return render(request, "writePost.html",
                  {"restaurantPlace": restaurantPlace,
                   "restaurantName": restaurantName,
                   "openDate": openDate,
                   "useStartTime": useStartTime,
                   "useEndTime": useEndTime,
                   "breakStartTime": breakStartTime,
                   "breakEndTime": breakEndTime,
                   "foodType": foodType,
                   "restaurantNumber": restaurantNumber,
                   "url": url,
                   })