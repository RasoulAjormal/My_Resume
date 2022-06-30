from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    Image = models.ImageField(upload_to='Images/Me', null=True, verbose_name='Image Me')
    Age = models.IntegerField(verbose_name='Age', blank=True, null=True)
    Date_Of_Birth = models.CharField(max_length=50, null=True, blank=True, verbose_name='Date Of Birth')
    Address = models.CharField(max_length=100, verbose_name='Address', null=True)
    Degree = models.CharField(max_length=50, null=True, blank=True, verbose_name='Degree')
    Freelance = models.CharField(max_length=50, null=True, verbose_name='Freelance')
    About_Me = models.TextField(max_length=500, verbose_name='About Me', null=True)
    # I Do
    HappyClients = models.IntegerField(null=True, verbose_name='Happy Clients')
    Projects = models.IntegerField(null=True, verbose_name='Projects')
    HoursOfSupport = models.IntegerField(null=True, verbose_name='Hours Of Support')
    Awards = models.IntegerField(null=True, verbose_name='Awards')
    # Contact #
    Instagram = models.CharField(max_length=50, null=True, blank=True, verbose_name='Instagram')
    GitHub = models.CharField(max_length=50, null=True, blank=True, verbose_name='Github')
    Linkedin = models.CharField(max_length=50, null=True, blank=True, verbose_name='Linkedin')
    Phone = models.CharField(max_length=13, verbose_name='Phone', null=True)
    Web_Site = models.URLField(max_length=100, verbose_name='WebSite', null=True, blank=True)

    class Meta:
        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutsMe'

    def __str__(self):
        return self.get_full_name()


class Visit(models.Model):
    ip = models.CharField(max_length=50, verbose_name='Ip')
    Date = models.DateTimeField(auto_now_add=True, verbose_name='Date', null=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'


class Education(models.Model):
    Majors = models.CharField(max_length=50, verbose_name='Majors')
    Educational_Degree = models.CharField(max_length=50, verbose_name='Educational Degree')
    CreateTime = models.DateField(max_length=10, auto_now_add=True, verbose_name='CreateTime')
    Address = models.CharField(max_length=50, null=True, verbose_name='Address')
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Me')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.Educational_Degree


class Experiences(models.Model):
    Company_Name = models.CharField(max_length=50, verbose_name='Company Name')
    Work = models.CharField(max_length=50, verbose_name='Work')
    Date = models.CharField(max_length=10, verbose_name='Date')
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')
    user = models.ManyToManyField(User, verbose_name='Me')

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.Company_Name


class Description(models.Model):
    Description = models.CharField(max_length=200, verbose_name='Description')
    Experiences = models.ForeignKey(Experiences, on_delete=models.CASCADE,
                                    verbose_name='Description')

    def __str__(self):
        return str(self.Experiences)

    class Meta:
        verbose_name = 'Description of the experience'
        verbose_name_plural = 'Description of experiences'


class WorkSampleCategory(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title', null=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'WorkSampleCategory'
        verbose_name_plural = 'WorkSampleCategories'


class WorkSamples(models.Model):
    Category = models.ForeignKey('WorkSampleCategory', on_delete=models.CASCADE, verbose_name='عنوان', null=True)
    I_Do = models.CharField(max_length=50, null=True, blank=True, verbose_name='I_Do')
    Link = models.CharField(max_length=100, null=True, blank=True, verbose_name='Link')
    Image = models.ImageField(upload_to=f'Images/WorkSample/', verbose_name='Image')
    Description = models.TextField(max_length=1000, verbose_name='Description', null=True)
    Company = models.CharField(max_length=100, verbose_name='Company', null=True,blank=True)
    Client = models.CharField(max_length=100, verbose_name='Client', null=True,blank=True)
    Date = models.CharField(max_length=50, verbose_name='Date', null=True)
    user = models.ManyToManyField(User, verbose_name='Me')
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        verbose_name = 'WorkSample'
        verbose_name_plural = 'WorkSamples'

    def __str__(self):
        return str(self.Category)


class WorkSampleGallery(models.Model):
    Image = models.FileField(verbose_name='عکس', null=True)
    WorkSample = models.ForeignKey(WorkSamples, verbose_name='WorkSample', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.WorkSample)

    class Meta:
        verbose_name = 'WorkSampleGallery'
        verbose_name_plural = 'WorkSampleGalleries'


class JobTitles(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    user = models.ManyToManyField(User, verbose_name='Me')

    class Meta:
        verbose_name = 'JobTitle'
        verbose_name_plural = 'JobTitles'

    def __str__(self):
        return self.Title


class Skill(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    Percentage = models.IntegerField(verbose_name='Percentage')
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')
    user = models.ManyToManyField(User, verbose_name='Me')

    def __str__(self):
        return f'{str(self.user.first())}-{self.Title}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class CertificateCategory(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title', null=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Category Title'
        verbose_name_plural = 'Categories Titles'


class Certificate(models.Model):
    CertificateCategory = models.ForeignKey(CertificateCategory, on_delete=models.CASCADE, verbose_name='Title',
                                            null=True)
    Percentage = models.IntegerField(verbose_name='Percent')
    Image = models.ImageField(upload_to='Images/Skills', verbose_name='Photo of the document')
    Url = models.URLField(max_length=300, verbose_name='Url', null=True, blank=True)
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')
    user = models.ManyToManyField(User, verbose_name='Me')

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return str(self.CertificateCategory)


class CommentsOfOthersModel(models.Model):
    Image = models.ImageField(null=True, upload_to='Images/Comment/', verbose_name='Image')
    FullName = models.CharField(max_length=50, verbose_name='Full Name')
    Comments = models.TextField(max_length=307, verbose_name='Comments')
    Job = models.CharField(max_length=50, null=True, blank=True, verbose_name='Job')
    Is_Read = models.BooleanField(default=False, verbose_name='Is Read')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Comments Of Others')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.FullName


class ContactModel(models.Model):
    FullName = models.CharField(max_length=50, verbose_name='Full Name')
    EmailAddress = models.EmailField(verbose_name='EmailAddress')
    Subject = models.CharField(max_length=50, null=True, verbose_name='Subject')
    Message = models.TextField(max_length=500, verbose_name='Message')
    Is_Read_Admin = models.BooleanField(default=False, verbose_name='Is_Read_Admin')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Me', editable=False)

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

    def __str__(self):
        return self.FullName
