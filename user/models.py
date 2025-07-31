from django.db import models



# Create your models here.
class contactus(models.Model):

    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=90,null=True)
    Mobile=models.CharField(max_length=22,null=True)
    Subject=models.CharField(max_length=200,null=True)
    Message=models.TextField(null=True)

    def __str__(self):
        return self.Subject


class tbl_feedback(models.Model):
    name=models.CharField(max_length=50,null=True)
    feedback=models.TextField(null=True)
    picture=models.ImageField(upload_to='static/picture/',null=True)


class tbl_recruiter(models.Model):
    company_logo=models.ImageField(upload_to='static/recruiter/',null=True)


class tbl_gallery(models.Model):
    gallery_picture=models.ImageField(upload_to='static/gallery/',null=True)


class tbl_alumni(models.Model):
    name=models.CharField(max_length=50,null=True)
    student_picture=models.ImageField(upload_to='static/placement/',null=True)
    company_name=models.CharField(max_length=40,null=True)
    placement_session=models.CharField(max_length=40,null=True)

class tbl_slider(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    slider_image=models.ImageField(upload_to='static/slider/',null=True)


class tbl_infra(models.Model):
    title=models.CharField(max_length=100,null=True)
    picture=models.ImageField(upload_to='static/infra/',null=True)

class tbl_notice(models.Model):
    notice=models.TextField(null=True)
    notice_link=models.URLField(max_length=300,null=True)
    posted_date=models.DateField(null=True)

class tbl_faculty(models.Model):
    name=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to='static/faculty/',null=True)
    designation=models.CharField(max_length=40,null=True)
    experiance=models.CharField(max_length=20,null=True)
    specialization=models.CharField(max_length=50,null=True)

    qualification=models.CharField(max_length=40,null=True)


class tbl_courses(models.Model):
    department=models.CharField(max_length=60,null=True)
    seats=models.CharField(max_length=30,null=True)
    course_code=models.CharField(max_length=20,null=True)
    duration=models.CharField(max_length=40,null=True)
    pdf = models.FileField(upload_to="static/doc",null=True)

class tbl_help(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=90,null=True)
    Category= models.CharField(max_length=90, null=True)
    Description=models.CharField(max_length=200,null=True)


class tbl_principal(models.Model):
    principal_picture = models.ImageField(upload_to='static/principal', null=True)
    message = models.CharField(max_length=400, null=True)
    principal_name = models.CharField(max_length=50, null=True)

class tbl_event(models.Model):
    date=models.DateField(null=True)
    event=models.TextField(null=True)




















