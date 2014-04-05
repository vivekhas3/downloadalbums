# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
import zip
import urllib
import logging
import os
from shutil import rmtree as remove_dir
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from shutil import make_archive
from django.core.servers.basehttp import FileWrapper
import sys
try:
    from google.appengine.ext import db
    from google.appengine.api import urlfetch
except:
    sys.path.append("/home/ubuntu/google_appengine/")
    from google_custom.appengine.ext import db
    from google_custom.appengine.api import urlfetch

import zipfile
import StringIO
class Album(db.Model):
    title = db.StringProperty()
    picture = db.BlobProperty(default=None)

log = logging.getLogger(__name__)
def getAlbum(title):
    result = db.GqlQuery("SELECT * FROM Album WHERE title =:1", title).fetch(1000)
    if (len(result) > 0):
        return result
    else:
        return None
def deleteAlbum(title):
    results = db.GqlQuery("SELECT *  FROM Album WHERE title =:1", title).fetch(1000)
    db.delete(results)

def home(request):
    if request.method=="GET":
        return render_to_response("aldown.html",{})
@csrf_exempt
def home_post(request):
    log.info(request.POST)
    file_name = "/tmp/albums/"+request.POST['name']
    deleteAlbum(request.POST['name']) 
    for i in request.POST.getlist('li1[]'):
        album = Album()
        album.title = request.POST['name']
        album.picture = db.Blob(urlfetch.Fetch(i).content)
        album.put()

#    output = StringIO.StringIO()
#    z = zipfile.ZipFile(output,'w')
#    files =  getAlbum(request.POST['name'])
#    for i,fil in enumerate(files):
#         my_data = fil.picture
#         z.writestr(str(i)+".jpeg", my_data)
#
#    z.close()
#     # fix for Linux zip files read in Windows  
#    for file in z.filelist:  
#        file.create_system = 0  
#    response = HttpResponse(mimetype="application/zip")  
#    response["Content-Disposition"] = "attachment; filename=two_files.zip"  
#      
#    output.seek(0)      
#    response.write(output.read())  
#    return response
    return HttpResponse(simplejson.dumps({'redirect_url':'/aldown/download/'+request.POST['name']+".zip/"}),mimetype="application/json")

def download(request,file_name=""):
    log.info(file_name)
    if file_name:
        file_name=file_name.encode('ascii', 'ignore')
	file_path = file_name[:-4]
    output = StringIO.StringIO()
    z = zipfile.ZipFile(output,'w')
    files =  getAlbum(file_path)
    for i,fil in enumerate(files):
         my_data = fil.picture
         z.writestr(str(i)+".jpeg", my_data)

    z.close()
     # fix for Linux zip files read in Windows  
    for file in z.filelist:
        file.create_system = 0
    response = HttpResponse(mimetype="application/zip")
    response['Content-Disposition'] = 'attachment; filename='+file_name.replace(" ","_")
    output.seek(0)      
    response.write(output.read())  
    return response
	
