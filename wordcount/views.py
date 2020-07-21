from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1

    return render(request,'count.html',{'fulltext':full_text,'total':len(word_list),'dict':word_dict.items()   }   )
