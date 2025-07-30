from django.shortcuts import render, redirect
from .models import News

def home(request):
    all_news = News.objects.all().order_by('-created_at')
    news_items = all_news[:5]  # पहले 5 न्यूज़
    return render(request, 'home.html', {'all_news': all_news, 'news_items': news_items})



from django.shortcuts import render, redirect
from .models import News


from django.shortcuts import render, redirect
from .models import News  # यदि News model से सर्च हो रही है

def search_results(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            results = News.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'query': query, 'results': results})
        else:
            return redirect('home')
    else:
        return redirect('home')  # यहाँ GET से आने पर redirect किया जा रहा है



# views.py
from django.shortcuts import render, redirect
from .models import News

CATEGORY_LABELS = {
    'home': 'सभी समाचार',
    'adhikar': 'आपका अधिकार',
    'bharat': 'भारत',
    'janata': 'जनता की आवाज़',
    'local': 'लोकल खबरें',
    'international': 'अंतर्राष्ट्रीय',
    'opinion': 'ओपिनियन',
    'politics': 'राजनीती',
    'education': 'शिक्षा',
    'society': 'समाज',
    'cyber': 'साइबर सुरक्षा',
}

def category_news(request, category_slug):
    news_list = News.objects.filter(category=category_slug).order_by('-created_at')
    category_name = CATEGORY_LABELS.get(category_slug, "Unknown")
    return render(request, 'category_news.html', {'news_list': news_list, 'category': category_name})




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NewsForm

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not authorized'})
    return render(request, 'admin_login.html')


@login_required(login_url='/login/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')




def admin_logout(request):
    logout(request)
    return redirect('admin_login')



from django.shortcuts import get_object_or_404


from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm  # अगर आप form यूज़ कर रहे हो


# views.py

from django.shortcuts import render, redirect
from .forms import NewsForm

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)  # ध्यान: request.FILES ज़रूरी है
        if form.is_valid():
            form.save()
            return redirect('news_list')  # या अपनी news list url का नाम
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})



def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    category_slug = news.category_slug if news.category_slug else ''  # ya default koi slug
    return render(request, 'news_detail.html', {'news': news, 'category_slug': category_slug})


from django.shortcuts import render
from .models import News

def news_list(request):
    news_items = News.objects.all().order_by('-id')  # latest first
    return render(request, 'news_list.html', {'news_list': news_items})
