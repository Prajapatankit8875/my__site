# logic business
# code for video 6
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
 #   return HttpResponse ('''<h1>Hello Ankit<h1/> <a href="https://www.youtube.com/watch?v=8HDTS80dlr4&list=RD8HDTS80dlr4&start_radio=1">highway song </a>>''')


#def about(request):
 #   return HttpResponse ('''About <a href="https://www.sarkariresult.com/"> Govt exam</a>>''')
  

# code for video: 7

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.Get.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
    #analyzed = djtext
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
               analyzed = analyzed + char
      params = {'purpose':'Removed Punctuations','analyzed_text':'analyzed'}
      #Analyze the text
      return render(request, 'analyze.html',param)
    else:
        return HttpResponse("Error")

#def capfirst(request):
   # return HttpResponse("capitalize first")

#def newlineremove(request):
   # return HttpResponse("newline remove ")

#def spaceremove(request):
   # return HttpResponse("space remove  <a href='/'>back</a>")

#def charcount(request):
   # return HttpResponse("char count")

