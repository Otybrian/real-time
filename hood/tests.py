from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Profile,Neighborhood,Post,Business,Location


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        self.profile = Profile(name="brian",email="brian@gmail.com",profile_pic="brian.jpg",bio="Test Profile_pic",user=user,location="Nairobi",neighborhood="Kasarani")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_update_profile(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)