from django.shortcuts import render

<<<<<<< HEAD
=======
def index(request):
    return HttpResponse("Hello, world. You're at the Two Wheels index.")

@csrf_exempt
def bikes(request):
    mock = """{
    "bikes": [
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        },
        {
            "id": 1,
            "name": "Bike Name",
            "image_url": "http://s1.cdn.autoevolution.com/images/news/gallery/indonesian-studio-motor-insanely-cool-honda-shadow-1100_10.jpg",
            "models": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Honda"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Honda Shadow"
                }
            ],
            "styles": [
                {
                    "id": 1,
                    "name": "Cruiser"
                }
            ],
            "parts": [
                {
                    "id": 1,
                    "type": 1,
                    "name": "Ape Hanger Bars"
                },
                {
                    "id": 2,
                    "type": 2,
                    "name": "Vance & Hines Short Shots"
                }
            ]
        }
    ]
}
    """
    response = HttpResponse(mock, content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    return response
>>>>>>> develop

def index(request):
    return render(request, 'base.html')