from datetime import date
from django.utils import timezone

import enum


from django.db import models
#enumeration : first method (class inherits from enum.Enum) [in python]
class StudyLevel(enum.Enum):
    FirstClass=1
    SecondClass=2
    ThirdClass=3
    MasterClass=4
    DoctoralClass=5

    @classmethod
    def choices(self): #returns list [...] of tuples(1,FirstClass),(2,SecondClass)...
        return [(x.value, x.name) for x in self]

#enumeration : second method (list)
# StudyLevel=[
#     ('F_Class','first class'),
#     ('S_Class','second class'),
#     ('T_Class','third class'),
#     ]

#enumation : third method (models.TextChoices) [in django]
class studyLvel(models.TextChoices):
    FirtClass=('F_Class','first class')
    SecondClass = ('S_Class','second class')
    ThirdClass = ('T_Class','third class')

class Person(models.Model):
    #id=models.BigAutoField(primary_key=True,default=1)
    name=models.CharField(max_length=100,null=False,blank=False,default='')
    #null=False <=> not null in sql syntax
    #blank=False <=> the field is required (on the forms.Form)
    familyName=models.CharField(max_length=100,null=False,blank=False,default='')
    password=models.CharField(max_length=100,null=True,blank=True, )
    email=models.EmailField( max_length=50,unique=True,null=True,blank=True)
    birthDate=models.DateField(default=date(2004,1,1))
    #default=timezone.now() <=> provides system date as default value
    
    class Meta:
        abstract=True
        ordering=['name','familyName']


class Group(models.Model):
    name= models.CharField(max_length=100,unique=True)
    # level= models.CharField(max_length=100,choices=StudyLevel,default=StudyLevel[0][0])
    level= models.CharField(max_length=100,choices=StudyLevel.choices(),default=StudyLevel.FirstClass)
    #level= models.CharField(max_length=100,choices=StudyLevel,default=StudyLevel.FirstClass)
    speciality= models.CharField(max_length=30)
    email=models.EmailField(verbose_name="email of group", max_length=150,null=True, blank=True)
    #student_number=models.IntegerField(default=0)
    student_number=models.PositiveIntegerField(default=0) #equivalent to brevious with validation





    class Meta:
        db_table='group'
        ordering=['name']

    def __str__(self):
        return '%s, %s, %s'% (self.name, self.level, self.speciality)
    #return f'{self.name}, {self.level}, {self.speciality}'

    def get_student_level_label(self):
        return StudyLevel(self.level).name.title()


class Address(models.Model):
    number=models.IntegerField(default=1,null=False,blank=False)
    street=models.CharField(max_length=200,null=False,blank=False,verbose_name='Street Name')
    city=models.CharField(max_length=200,null=False,blank=False)
    postal_code=models.IntegerField(default=1000,null=False,blank=False)

class Student(Person):
    photo=models.ImageField(upload_to='photos/students', max_length=200,null=True,blank=True)
    #inscriptionNumber = models.CharField(max_length=20,primary_key=True)
    # inscription Number is the primary key
    #number= models.AutoField() # generates an auto increment integer primary key
    #specification of the many to One relationship between Student and Group
    group=models.ForeignKey(Group, null=True, blank=True,on_delete=models.CASCADE)
    #specification of the one to one relationship between Student and Address
    address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True, blank=True)



    class Meta:
        db_table='student'


    def __str__(self):
        return f'{self.name}, {self.familyName},{self.email}'



class Module(models.Model):
    name=models.CharField(max_length=200)
    due=models.DecimalField(max_digits=4,decimal_places=2,default=21)
    model_type=models.CharField(max_length=50)
    level= models.CharField(max_length=100,choices=StudyLevel.choices(),default=StudyLevel.FirstClass)
    #specification of the many to many relationship between Module and Group
    #crerate the association class between Module and Group
    #the association class may be created on Group class but not on both
    study=models.ManyToManyField(Group)

    def __str__(self):
        return 'name = %s, due = %s'%(self.name,self.due)

class Teacher(Person):
    email_work=models.EmailField(verbose_name="workemail", max_length=150,null=True, blank=True)
    photo=models.ImageField(upload_to='photos/teachers', max_length=200,null=True,blank=True)
    grade=models.CharField(max_length=200,null=True,blank=True)
    teacher_modules=models.ManyToManyField(Module,through='TeacherModules',through_fields=('teacher','module'))
class TeacherModules(models.Model): #description of the association class between Module and Teache (many to many relationship)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    year=models.IntegerField(default=timezone.now().year)
    nb_Hours=models.IntegerField(default=1)   