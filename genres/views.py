import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse    
from genres.models import Genre


@csrf_exempt
def genre_create_list_view(request):

    if request.method == "GET":
            genres = Genre.objects.all()
            data = [{"id": genre.id, "name": genre.name} for genre in genres]
            #return JsonResponse(data, safe=False,status=200)
            return JsonResponse({"total": len(data),"results": data},status=200)


    elif request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))

            created = []
            for item in data:
                genre, is_created = Genre.objects.get_or_create(name=item["name"])
                if is_created:
                    created.append({"id": genre.id, "name": genre.name})

            return JsonResponse({"created": created,"total_created": len(created)},status=201)
        
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "GET":
            data = {"id": genre.id, "name": genre.name}
            return JsonResponse(data, status=200)
    