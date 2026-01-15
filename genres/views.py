from django.http import JsonResponse    
from genres.models import Genre
# 
def genre_view(request):
    genres = Genre.objects.all() 
    #serialização manual apenas para exemplo
    data = [{'id': genre.id, 'name': genre.name}for genre in genres]
    #retorna arquivo json
    return JsonResponse(data, safe=False)  
