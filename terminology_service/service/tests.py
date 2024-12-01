from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import RefBook, RefBookElement, RefBookVersion

class RefBookTests(APITestCase):
    
    def setUp(self):
        self.refbook1 = RefBook.objects.create(code='AAA', name='Переломы', description='Все переломы')
        self.refbook2 = RefBook.objects.create(code='BBB', name='Вывихи', description='Все вывихи')

        self.version1_1 = RefBookVersion.objects.create(refbook=self.refbook1, 
                                      version='1.0', 
                                      start_date=date(2024,11,29))
        self.version1_2 = RefBookVersion.objects.create(refbook=self.refbook1, 
                                      version='2.0', 
                                      start_date=date(2024,11,30))
        
        self.version2_1 = RefBookVersion.objects.create(refbook=self.refbook2, 
                                      version='3.0', 
                                      start_date=date(2024,12,1))
        
        RefBookElement.objects.create(refbook_version = self.version1_1,
                                      code='1',
                                      value= '1')
        RefBookElement.objects.create(refbook_version = self.version1_1,
                                      code='2',
                                      value= '2')
        RefBookElement.objects.create(refbook_version = self.version1_2,
                                      code='3',
                                      value= '3')

    def test_get_refbooks(self):
        '''
        Список всех refbooks
        '''
        response = self.client.get(reverse('refbooks_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['refbooks']), 2)
    
    def test_get_refbooks_by_date(self):
        '''
        Список refbooks по дате
        '''
        response = self.client.get(reverse('refbooks_list')+'?date=2024-11-29')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['refbooks']), 1)
    
    def test_get_refbooks_by_date_empty(self):
        '''
        Список refbooks по дате пустой список
        '''
        response = self.client.get(reverse('refbooks_list')+'?date=2024-11-28')
        self.assertEqual(len(response.data['refbooks']), 0)
        
    def test_get_elements(self):
        '''
        Список элементов
        '''
        response = self.client.get(reverse('refbooks_elements',args=[self.refbook1.id]))
        self.assertEqual(len(response.data['elements']), 1)
        
    
    def test_get_elements_by_version(self):
        '''
        Список элементов по версии
        '''
        response = self.client.get(reverse('refbooks_elements',args=[self.refbook1.id])+'?version=2.0')
        self.assertEqual(len(response.data['elements']), 1)
    
    def test_check_element(self):
        '''
        Проверка элемента
        '''
        response = self.client.get(reverse('check_element',args=[self.refbook1.id])+'?code=3&value=3')
        self.assertEqual(len(response.data['element']), 1)
        
    def test_check_element_by_version(self):
        '''
        Проверка элемента по версии
        '''
        response = self.client.get(reverse('check_element',args=[self.refbook1.id])+'?code=3&value=3&version=2.0')
        self.assertEqual(len(response.data['element']), 1)
    
    def test_check_element_by_version_empty(self):
        '''
        Проверка элемента по версии
        '''
        response = self.client.get(reverse('check_element',args=[self.refbook1.id])+'?code=10&value=10&version=2.0')
        self.assertEqual(len(response.data['element']), 0)