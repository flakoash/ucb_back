import sys
import os
import platform

#print(sys.argv)
class artisan:
    ParentDir = ''
    ProjectName = ''
    OSslash = ''
    view_name = ''
    def __init__(self,vn):
        self.view_name = vn

    def cp(self, src, dest):
        old = open(src, 'r')
        new = open(dest, 'w')
        buff = old.read()
        nbuff = buff.replace('XOXOXO', self.view_name)
        new.write(nbuff)
        old.close()
        new.close()

    def appendURL(self, api=False):
        aux = "" if api else self.view_name+self.OSslash
        urls = open(self.ParentDir + self.OSslash + self.ProjectName + self.OSslash + 'urls.py', 'r')
        data = urls.readlines()
        s = "    url('" + aux + "', include('" + view_name + ".urls')), \n ]"
        data[len(data) - 1] = s
        with open(self.ParentDir + self.OSslash + self.ProjectName + self.OSslash + 'urls.py', 'w') as file:
            file.writelines(data)

    def getParentDir(self):
        dir = os.popen('pwd').read() if platform.system() != 'Windows' else os.popen('cd').read()
        return dir.replace('\n', ''), dir.split(self.OSslash)[-1].replace('\n', '')

    def setup(self):
        self.OSslash = '\\\\' if platform.system() == 'Windows' else '/'
        self.ParentDir, self.ProjectName = self.getParentDir()


if __name__ == "__main__":
    #try:

    #if sys.argv[1] == 'qwerty':

    if sys.argv[1] == 'makeapp':
        view_name = sys.argv[2].title()
        os.system('python manage.py startapp '+view_name)
        art = artisan(view_name)
        art.setup()
        if '-r' in sys.argv or '--resource' in sys.argv:
            print('---Creating resource APP---')
            # create url.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'urls.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'urls.py')
            # create views.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'views.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'views.py')
            # include urls to main urls.py
            art.appendURL()
            #create models.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'models.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'models.py')
        if '-t' in sys.argv or '--template' in sys.argv:
            # create template folder for the new resource
            os.system("mkdir "+art.ParentDir+art.OSslash+"templates"+art.OSslash+ + art.view_name)
            #create HTML template files
            os.system("cp " + art.ParentDir + art.OSslash+"artisan"+art.OSslash+"templates"+art.OSslash+"index.html "+art.ParentDir+art.OSslash+"templates"+art.OSslash+art.view_name+art.OSslash+"index.html")
            os.system("cp " + art.ParentDir + art.OSslash+"artisan"+art.OSslash+"templates"+art.OSslash+"create_form.html "+art.ParentDir +art.OSslash+"templates"+art.OSslash+art.view_name+art.OSslash+"create_form.html")
            os.system("cp " + art.ParentDir + art.OSslash+"artisan"+art.OSslash+"templates"+art.OSslash+"show.html " + art.ParentDir+art.OSslash+"templates"+art.OSslash+art.view_name+art.OSslash+"show.html")
            os.system("cp " + art.ParentDir + art.OSslash+"artisan"+art.OSslash+"templates"+art.OSslash+"confirm_delete.html "+art.ParentDir+art.OSslash+"templates"+art.OSslash+art.view_name+art.OSslash+"confirm_delete.html")

        if '--rest' in sys.argv:
            print('---Creating REST APP---')
            # create url.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'rest'+art.OSslash+'urls.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'urls.py')
            # create views.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'rest'+art.OSslash+'views.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'views.py')
            # create serializers.py
            art.cp(art.ParentDir + art.OSslash + 'artisan' + art.OSslash + 'rest' + art.OSslash + 'serializers.py', art.ParentDir + art.OSslash + art.view_name + art.OSslash + 'serializers.py')
            # include urls to main urls.py
            art.appendURL(api=True)
            # create models.py
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'models.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'models.py')
        if '-a' in sys.argv or '--admin' in sys.argv:
            print('---Registering the APP in Admin---')
            #Register to admin
            art.cp(art.ParentDir+art.OSslash+'artisan'+art.OSslash+'admin.py', art.ParentDir+art.OSslash+art.view_name+art.OSslash+'admin.py')
        print('New App created successfully! \n'
              '###############################################################\n'
              '####Do not Forget to REGISTER the app inside INSTALLED_APPS####\n'
              '####                    on settings.py:                    ####\n'
              '####                      \'' + view_name + '\',                     ####\n'
              '###############################################################\n')
    else:
        a = ''
        i=0
        for parm in sys.argv:
            if i != 0:
                a += parm + ' '
            i += 1
        os.system('python manage.py ' + a)

    #except:
    #    print("Ups! Something in the speedforce is not working fine")
