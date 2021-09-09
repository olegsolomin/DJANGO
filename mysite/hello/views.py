from django.http import HttpResponse

# Create your views here.

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse("""<html><body><p>Hello view</p>
    <p>This code is just to test <a href='sessfun'><strong>session</strong></a> and get <a href='cookie'><strong>cookies</strong></a>
    <a href="http://solominon.pythonanywhere.com">
    http://solominon.pythonanywhere.com</a></p>
    </body></html>"""
    '<br>view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '1cfcf091', max_age=1000)
    return resp

def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse('Wanna get cookies... or , <a href="http://solominon.pythonanywhere.com">Back to Main Page</a>')
    resp.set_cookie('dj4e_cookie', '1cfcf091', max_age=1000)
    return resp

def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    return HttpResponse('View Count='+str(num_visits)+ '...or <a href="http://solominon.pythonanywhere.com">Back to Main Page</a>')