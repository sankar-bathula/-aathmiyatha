1.Craeate app folder name like jobs/posts

2.To added back-end admin portal

	a.Open admin.py add below step
	admin.site.register(Jobs)# this is Jobs class is created in models

	b.open models.py add below steps
	class Jobs(models.Model): #If required more field also can add
	image = models.ImageField(upload_to='images/')
	summery =models.CharField(max_length=200)

3.Add urls in main directory aathmiyatha/urls.py
	import jobs.views
	url(r'', jobs.views.home,name='home' )#this is default index for the websit
4.Run below commends(on commend prompt)
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
5.check in browser default server ip
	http://127.0.0.1:8000/