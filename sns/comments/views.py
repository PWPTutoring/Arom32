from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm, SignUpForm

def comment_view(request):
    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments:comment')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment.html', {
        'form': form,
        'comments': comments
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('comments:comment')
    else:
        form = SignUpForm()

    return render(request, 'comments/signup.html', {'form': form})





# from django.shortcuts import render, redirect #w3_redirect 
# from .models import Comment 
# #w3 _ models.py에서 Commet Model 가져옴.
# # . models, .

# def comment_view(request):
#     if request.method == 'POST': 
#         content = request.POST.get('content') 
#         Comment.objects.create(content=content) #w3 테이블에 새 행을 생성 + 내용 추가
#         return redirect('comments:comment') #w3 urls.py app_name:path_name 

#     comments = Comment.objects.all().order_by('-created_at') #w3 목록표시
#     # Comment.objects.all() 모든 데이터 가져오기
#     #.order_by('-created_at') 내림차순으로 정렬 
#     #cf) created_at 오름차순
#     return render(request, 'comments/comment.html', {'comments': comments})


