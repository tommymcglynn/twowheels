from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from web.models import BikeStyle, BikeMake, BikeFamily, BikeModel, BikePart, Bike

def index(request):
    context = {}
    context['api_url'] = request.build_absolute_uri(reverse('api-root'))
    return render(request, 'home.html', context)

@permission_required('web.add_bike', raise_exception=True)
def gather_images(request, partId=None, makeId=None, familyId=None, modelId=None, styleId=None, start='1'):
    import urllib2
    import json

    # defaults
    start = int(start)
    count = 8
    dataInfo = None
    searchTerm = ''
    styles = []
    makes = []
    families = []
    models = []
    parts = []
    part = None
    make = None
    family = None
    model = None
    style = None
    saveUrl = ''

    if partId:
        part = BikePart.objects.get(id=partId)
    if styleId:
        style = BikeStyle.objects.get(id=styleId)
    if request.method == 'POST':
        # handle new image data
        imageData = json.load(request)
        bike = Bike(name=imageData['titleNoFormatting'],
                    image_url=imageData['unescapedUrl'],
                    source_url=imageData['originalContextUrl'],
                    model_id=modelId)
        bike.save()
        bike.styles.add(style)
        bike.parts.add(part)
        return HttpResponse('')

    if makeId:
        make = BikeMake.objects.get(id=makeId)
    if familyId:
        family = BikeFamily.objects.get(id=familyId)
    if modelId:
        model = BikeModel.objects.get(id=modelId)
    if partId and makeId and familyId and modelId and styleId:
        saveUrl = reverse('gather-images', kwargs={'partId': partId, 'makeId': makeId, 'familyId': familyId, 'modelId': modelId, 'styleId': styleId})
        searchTerm = '%s %s %s' % (part.name, model, style.name)
        searchTerm = searchTerm.replace(' ','%20').replace('&', '%20').replace('-', '%20').replace('+', '%20')
        # Notice that the start changes for each iteration in order to request a new set of images for each loop
        url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&rsz=%d&start=%d' % (searchTerm, count, start)

        apiRequest = urllib2.Request(url)
        response = urllib2.urlopen(apiRequest)
        # Get results using JSON
        results = json.load(response)
        data = results['responseData']
        dataInfo = data['results'] if data else []
        for imageData in dataInfo:
            imageData['json'] = json.dumps(imageData)
    elif partId and makeId and familyId and modelId:
        # load styles
        styles = BikeStyle.objects.all()
    elif partId and makeId and familyId:
        # load models
        models = BikeModel.objects.filter(family=familyId)
    elif partId and makeId:
        # load families
        families = BikeFamily.objects.filter(make=makeId)
    elif partId:
        # load makes
        makes = BikeMake.objects.all()
    else:
        # load parts
        parts = BikePart.objects.all()

    # Iterate for each result and get unescaped url
    nextStart = start+len(dataInfo) if dataInfo else start+1
    context = {'results': dataInfo, 'searchTerm': searchTerm, 'nextStart': nextStart,
               'partId': partId, 'makeId': makeId, 'familyId': familyId, 'modelId': modelId, 'styleId': styleId,
               'part': part, 'make': make, 'family': family, 'model': model, 'style': style,
               'styles': styles, 'makes': makes, 'families': families, 'models': models, 'parts': parts,
               'saveUrl': saveUrl}
    return render(request, 'image_gather.html', context)
