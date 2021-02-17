from django.http import HttpResponse
from django.shortcuts import render
from .models import SPARQL_Model

# Create your views here.
def index1(request):
    return render(request, 'head.html')

def index(request):

    languages = SPARQL_Model().get_languages()
    return render(request, 'home.html', {"languages":languages})

def movies(request):
    language = request.GET["language"]
    results = SPARQL_Model().get_movies(language)
    #return HttpResponse("My First Python Web application")
    return render(request, 'movies.html', {"results":results, "language":language})



def age1(request):

    age = SPARQL_Model().get_age()
    return render(request, 'age.html', { "age": age})
def agem(request):
    age = request.GET["age"]
    results = SPARQL_Model().get_age2(age)
    #return HttpResponse("My First Python Web application")
    return render(request, 'agem.html', {"results":results, "age":age})





def disease(request):

    disease = SPARQL_Model().get_disease()
    return render(request, 'disease.html', {"disease": disease})
def diseaser(request):
    disease = request.GET["disease"]
    results = SPARQL_Model().get_diseaser(disease)
        # return HttpResponse("My First Python Web application")
    return render(request, 'diseaser.html', {"results": results, "disease": disease})




def id(request):

    id = SPARQL_Model().get_id()
    return render(request, 'id.html', { "id": id})
def idr(request):
    id = request.GET["id"]
    results = SPARQL_Model().get_idr(id)
        # return HttpResponse("My First Python Web application")
    return render(request, 'idr.html', {"results": results, "id": id})



def place(request):

    languages = SPARQL_Model().get_place()
    return render(request, 'place.html', { "languages": languages})
def placer(request):
    place = request.GET["place"]
    results = SPARQL_Model().get_placer(place)
        # return HttpResponse("My First Python Web application")
    return render(request, 'placer.html', {"results": results, "place": place})
