from django.shortcuts import render, get_object_or_404, redirect

# gallery
from gallery.models import Image
from gallery.forms import ImageForm, CommentForm

# pagination
from django.core.paginator import Paginator, InvalidPage

# ajax stuff
import json
from django.utils.html import escape
from django.http import HttpResponse


def list(request):
    # handle file upload
    form = ImageForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('list')
    
    # load images for the list page
    images = Image.objects.all()
    
    # paging
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        image_list = paginator.page(page)
    except InvalidPage:
        image_list = paginator.page(1)

    # render list page with the images and the form
    return render(request, 'gallery/list.html', {
        'image_list': image_list,
        'form': form,
    })


def image(request, image_id):
    # first get the image object
    image = get_object_or_404(Image, pk=image_id)
    
    # handle new comment
    form = CommentForm(request.POST or None, foreign_key=image)
    if form.is_valid():
        comment_object = form.save()
        new_comment = comment_object.text
        
        if request.is_ajax():
            data = json.dumps({'new_comment': escape(new_comment)})
            return HttpResponse(data, mimetype='application/json');
        else:
            return redirect('image', image_id=image_id)
    
    # get image comments
    comments = image.comments.all()
    
    # render image page with comments and form
    return render(request, 'gallery/image.html', {
        'image': image,
        'comments': comments,
        'form': form,
    })
