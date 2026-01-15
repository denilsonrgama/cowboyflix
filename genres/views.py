import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed, JsonResponse    
from genres.models import Genre


@csrf_exempt
def genre_view(request):
    match request.method:
        case "GET":
            genres = Genre.objects.all()
            data = [
                {"id": genre.id, "name": genre.name}
                for genre in genres
            ]
            return JsonResponse(data, safe=False)

        case "POST":
            data = json.loads(request.body.decode("utf-8"))
            new_genre = Genre(name=data['name'])
            new_genre.save()
            return JsonResponse(
                {"id": new_genre.id, "name": new_genre.name}, status=201 #criado com sucesso
            )  
        case _:
            return HttpResponseNotAllowed(["GET"])
             