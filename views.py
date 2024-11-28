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
   path = "index.html"
   return render(request, path)
   # return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

     # check checkbox values

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')


    #check which checkbox is on
    if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
               analyzed = analyzed + char
      params = {'purpose':'Removed Punctuations','analyzed_text':'analyzed'}

      #Analyze the text
      return render(request, 'analyze.html',params)
    
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'change to uppercase','analyzed_text':'analyzed'}
        return render(request, 'analyze.html',params) 
    
    elif(newlineremover=="on"):
        analyzed = "" 
        for char in djtext:
            if char !="\n":
             analyzed = analyzed + char
        params = {'purpose':'removed newlines','analyzed_text':'analyzed'}
        return render(request, 'analyze.html',params) 
    
    elif(extraspaceremover=="on"):
        analyzed = "" 
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index+1]==" ":
               analyzed = analyzed + char
        params = {'purpose':'removed newlines','analyzed_text':'analyzed'}
        return render(request, 'analyze.html',params) 
        
 
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

