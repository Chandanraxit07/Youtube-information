
from django.shortcuts import render
from pytube import YouTube

def download(request):
    if request.method == 'POST':
        link = request.POST['link']
        yt = YouTube(link)
        title = yt.title
        views = yt.views
        length = yt.length
        rating = yt.rating
        return render(request, 'download.html', {'title': title, 'views': views, 'length': length, 'rating': rating})
    return render(request, 'index.html')

