from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from web.models import BikeStyle, BikeModel, BikePart

def index(request):
    context = {}
    context['api_url'] = request.build_absolute_uri(reverse('api-root'))
    return render(request, 'home.html', context)

def gather_images(request, partId=None, modelId=None, styleId=None, start='1'):
    import urllib2
    import json

    if request.method == 'POST':
        # handle new image data
        imageData = json.load(request)
        return HttpResponse(imageData)

    start = int(start)
    count = 8
    dataInfo = None
    searchTerm = ''
    styles = []
    models = []
    parts = []
    part = None
    model = None
    style = None
    saveUrl = ''
    if partId:
        part = BikePart.objects.get(id=partId)
    if modelId:
        model = BikeModel.objects.get(id=modelId)
    if styleId:
        style = BikeStyle.objects.get(id=styleId)
    if partId and modelId and styleId:
        saveUrl = reverse('gather-images', kwargs={'partId': partId, 'modelId': modelId, 'styleId': styleId})
        searchTerm = '%s+%s+%s' % (part.name, model.name, style.name)
        searchTerm = searchTerm.replace(' ','+').replace('&', '+')
        # Notice that the start changes for each iteration in order to request a new set of images for each loop
        url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&rsz=%d&start=%d' % (searchTerm, count, start)

        apiRequest = urllib2.Request(url)
        response = urllib2.urlopen(apiRequest)
        # Get results using JSON
        results = json.load(response)
        data = results['responseData']
        dataInfo = data['results']
        for imageData in dataInfo:
            imageData['json'] = json.dumps(imageData)
    elif partId and modelId:
        # load styles
        styles = BikeStyle.objects.all()
    elif partId:
        # load models
        models = BikeModel.objects.all()
    else:
        # load parts
        parts = BikePart.objects.all()

    # Iterate for each result and get unescaped url
    context = {'results': dataInfo, 'searchTerm': searchTerm, 'nextStart': start+count,
               'partId': partId, 'modelId': modelId, 'styleId': styleId,
               'part': part, 'model': model, 'style': style,
               'styles': styles, 'models': models, 'parts': parts,
               'saveUrl': saveUrl}
    return render(request, 'image_gather.html', context)
