from django.test import  TestCase, Client
from roadmap.models import Productmgr, Roadmap
from django.contrib.auth.models import User
from django.utils import timezone

class RoadmapModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up text to verify the models are set up correctly,
        checking option settings and implicently creating and retrieving 
        an object.   Other records were tested using inspection, since
        the application basically records and display database records.
        """
        #
        # Create a user
        user = User.objects.create(username='test')
        user.set_password('test1234')
        user.save()
        # logedin = cls.client.login(username='test', password='test1234')
        #create an test issue
        prod = Productmgr.objects.create(mgr = "BSH")   
        Roadmap.objects.create(prod_mgr=prod, release_num=1.0, title = "test", content="test")

        
    def test_rdmap_release_labeltitle_label(self):
        rdmap=Roadmap.objects.get(id=1)
        field_label = rdmap.title
        self.assertEquals(field_label,'test')
        max_length = rdmap._meta.get_field('title').max_length
        self.assertEquals(max_length,200) 
        
    def test_rdmap_release_label(self):
        rdmap=Roadmap.objects.get(id=1)
        field1 = rdmap._meta.get_field('release_num').max_digits
        self.assertEquals(field1,4)    
        field2 = rdmap._meta.get_field('release_num').decimal_places
        self.assertEquals(field2, 2)  
        field3 = rdmap._meta.get_field('release_num').default
        self.assertEquals(field3, 0)   
        field4 = rdmap._meta.get_field('release_num').verbose_name
        self.assertEquals(field4, 'Release')  
    
    def test_rdmap_content(self):
        rdmap=Roadmap.objects.get(id=1)
        field1 = rdmap._meta.get_field('content').blank
        self.assertEquals(field1,True)    
        field4 = rdmap._meta.get_field('content').verbose_name
        self.assertEquals(field4, 'Description')         
        
    def test_pubddate_label(self):
        rdmap=Roadmap.objects.get(id=1)
        field1 = rdmap._meta.get_field('releases_date').blank
        self.assertEquals(field1,True)    
        field2 = rdmap._meta.get_field('releases_date').null
        self.assertEquals(field2,True)  
        field3 = rdmap._meta.get_field('releases_date').default
        self.assertEquals(field3, timezone.now)     