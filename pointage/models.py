from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _


class ValidDate(models.Model):
    nom = models.CharField(max_length=30)
    date_of_validation= models.DateField()
    month = models.IntegerField(default=2)

class Code(models.Model):
    ID=models.CharField(primary_key=True,max_length=3)
    Description=models.TextField()
    def __str__(self) -> str:
        return str(self.ID)

class Month_stat(models.Model):
    period=models.CharField(max_length=6)
    employe=models.ForeignKey('Employe',on_delete=models.CASCADE)
    absent=models.IntegerField(default=0)
    travail=models.IntegerField(default=0)
    mission=models.IntegerField(default=0)
    conge=models.IntegerField(default=0)
    rs=models.IntegerField(default=0)
    eve_fam=models.IntegerField(default=0)
    mld=models.IntegerField(default=0)
    abs_autorise=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.employe} Month {self.period}'


class Code_Employe(models.Model):
    employe=models.ForeignKey("Employe",on_delete=models.CASCADE,related_name="code_emp")
    date=models.DateField(default=timezone.now)
    code=models.ForeignKey("Code",on_delete=models.CASCADE)
    open_to_edit = models.BooleanField(default=False)
    last_update =models.DateField(default=timezone.now)
    stored = models.BooleanField(default=False)
    
    @property
    def is_editable(self):
        today = timezone.now().date() 
        if self.code.ID == "8" :
            diff = (today - self.date).days
            return diff <= 5  # Example: Editable if the difference is less than 7 days
        
        return False  # Not editable if code.ID is not "8" 
    
    
        
    def __str__(self) -> str:
        return f"{self.code} {self.employe} {self.date}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1,related_name="profile")
    unite = models.ForeignKey("Unite",on_delete=models.CASCADE,null=True)
    da = models.IntegerField(default=3)
    def __str__(self):
        if self.da == 3 :
            return f'Respon Pointage {self.unite}'
        elif self.da == 2:
            return f'Chef unite {self.unite}'
        else : 
            return f'Directeur Generale'


class Unite(models.Model):
    
    unite_name=models.CharField(max_length=40,unique=True)
    last_update = models.DateField(null=True , blank=True)

    
    
    def __str__(self):
        return self.unite_name

code_counts = {
            "RS": 0,
            "C": 0,
            "8": 0,
            "7": 0,
            "MLD": 0,
            "5": 0,
            "3": 0,
            "6": 0
        }


class Employe(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.DateField(null=True)
    place_of_birth=models.CharField(max_length=30,null=True)
    wilaya_of_birth=models.CharField(max_length=30)
    id=models.AutoField(primary_key=True)
    unite=models.ForeignKey(Unite,on_delete=models.CASCADE,null=True)
    adresse=models.CharField(max_length=50,null=True)
    adresse_wilaya=models.CharField(max_length=30,null=True)
    father_name=models.CharField(max_length=30,null=True)
    mother_name=models.CharField(max_length=30,null=True)
    phone=models.IntegerField(null=True)
    familiy_situation=models.CharField(max_length=30,null=True)
    numbre_of_children=models.IntegerField(null=True)
    blood_type=models.CharField(max_length=5,null=True)
    cnas_number=models.IntegerField(null=True)
    function=models.CharField(max_length=60,null=True)
    position=models.CharField(max_length=60,null=True)
    enterprise=models.CharField(max_length=60,null=True)
    recruitment_date=models.DateField(default=timezone.now,null=True)
    department=models.CharField(max_length=60,null=True)
    service=models.CharField(max_length=60,null=True)
    contract_number=models.CharField(max_length=40,null=True)
    contract_effective_date=models.DateField(null=True)
    contract_validation_date=models.DateField(null=True)
    contract_termination_date=models.DateField(null=True)
    national_service_departure_date=models.DateField(null=True)
    national_service_returne_date=models.DateField(null=True)
    national_service_recall_departure_date=models.DateField(null=True)
    national_service_recallt_return_date=models.DateField(null=True)
    account_number=models.IntegerField(null=True)
    account_key=models.IntegerField(null=True)
    account_agency=models.CharField(max_length=40,null=True)
    driver_license_number=models.CharField(max_length=60,null=True)
    driver_license_established_date=models.DateField(null=True)
    driver_license_experation_date=models.DateField(null=True)
    driver_license_type=models.CharField(max_length=7,null=True)
    cni_number=models.IntegerField(null=True)
    cni_established_date=models.DateField(null=True)
    cni_established_by=models.CharField(max_length=60,null=True)
    recovery = models.IntegerField(default=0)
    refund_total=models.IntegerField(default=0)
    refund_by_month=models.IntegerField(default=0)
    active = models.IntegerField(default=1) #1= working | 2=not this month | 3=archive
    special = models.SmallIntegerField(default=0)
    
    
    
    
    
   
    '''Employe.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='pointage_employe';")

# Step 3: Vacuum the database to reclaim storage space
        with connection.cursor() as cursor:
            cursor.execute("VACUUM;")'''

    def __str__(self):
        return f"{self.name} - {self.last_name}"

class Partner(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.DateField(null=True)
    place_of_birth=models.CharField(max_length=30,null=True)
    wilaya_of_birth=models.CharField(max_length=30,null=True)
    marriage_date=models.DateField(null=True)
    partner_salary=models.IntegerField(null=True)
    id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)

class Child(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.DateField(null=True)
    place_of_birth=models.CharField(max_length=30,null=True)
    student=models.BooleanField(null=True)
    af=models.CharField(max_length=30,null=True)
    id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)

class Diplome(models.Model):
    establishment=models.CharField(max_length=40)
    entry_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    diplome_name=models.CharField(max_length=70)
    id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)

    
class Mission(models.Model):
    employe=models.ForeignKey(Employe,on_delete=models.CASCADE)
    start_date=models.DateField()
    total_validation=models.IntegerField(default=1)
    current_unite=models.ForeignKey(Unite,on_delete=models.CASCADE)
    unites=models.CharField(max_length=30)
    status=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f'{self.employe}_{self.current_unite}'
    
class History(models.Model):
    user=models.CharField(max_length=90)
    operation=models.CharField(max_length=40)
    table=models.CharField(max_length=30)
    date=models.DateTimeField()
    def __str__(self):
        return f'{self.user}_{self.operation}_{self.table}_{self.date}'