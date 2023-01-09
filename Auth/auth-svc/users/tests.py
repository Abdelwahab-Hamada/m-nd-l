from django.test import TestCase
from .models import User
from django.contrib.auth import authenticate


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='',name='tester',password='12345678')

    def test_user_can_signin(self):
        tester=authenticate(username='tester',password='12345678')
        
        self.assertEqual(tester.name,'tester')
    
    def test_user_can_update_account(self):
        tester=authenticate(username='tester',password='12345678')
        tester.name='tester2'
        tester.save()

        self.assertEqual(tester.name,'tester2')

        

