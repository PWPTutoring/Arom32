# from django.shortcuts import render

# def comment_view(request):
#     comment = None #초기값 

#     if( request.method == 'POST'): 
#         comment = request.POST.get('comment_text') 

#     return render(request, 'comments/comment.html', {'comment':comment})
#             #
# # Create your views here.

from django.shortcuts import render

def comment_view(request):  
    comment = None  
    
    if request.method == 'POST': 
        comment = request.POST.get('comment_text') 
    
    return render(request, 'comments/comment.html', {'comment': comment})