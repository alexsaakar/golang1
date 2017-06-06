# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

import app.views as views

# print(views.users_views)
benefit_forms = views.user_benefit_forms_views

# Tests checking that that '/users/:user_id/benefit_forms' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserBenefitFormsRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/benefit_forms/
    # and ensuring the response code is 200 (OK)
    def test_user_benefit_forms_route_exists(self):
        response = self.client.get(reverse('app:user_benefit_forms', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_forms_get(self):
        request = self.factory.get('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_forms_post(self):
        request = self.factory.post('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_forms_put(self):
        request = self.factory.put('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_benefit_forms_delete(self):
        request = self.factory.delete('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_benefit_forms_patch(self):
        request = self.factory.patch('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/users/:user_id/benefit_forms/new' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserNewBenefitFormsRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/benefit_forms/new
    # and ensuring the response code is 200 (OK)
    def test_new_user_benefit_form_route_exists(self):
        response = self.client.get(reverse('app:new_user_benefit_form', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_new_user_benefit_form_get(self):
        request = self.factory.get('/users/55/benefit_forms/new')
        response = benefit_forms.new_user_benefit_form(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_new_user_benefit_form_post(self):
        request = self.factory.post('/users/55/benefit_forms/new')
        response = benefit_forms.new_user_benefit_form(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_new_user_benefit_form_put(self):
        request = self.factory.put('/users/55/benefit_forms/new')
        response = benefit_forms.new_user_benefit_form(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_new_user_benefit_form_delete(self):
        request = self.factory.delete('/users/55/benefit_forms/new')
        response = benefit_forms.new_user_benefit_form(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_new_user_benefit_form_patch(self):
        request = self.factory.patch('/users/55/benefit_forms/new')
        response = benefit_forms.new_user_benefit_form(request, 55)
        self.assertEqual(response.status_code, 405)

# Tests checking that that '/users/:user_id/benefit_forms/:benefit_form_id/edit' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and benefit_form_id 22
class UserEditBenefitFormRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/benefit_forms/22/edit
    # and ensuring the response code is 200 (OK)
    def test_edit_user_benefit_form_route_exists(self):
        response = self.client.get(reverse('app:edit_user_benefit_form', kwargs={'user_id': 55, 'benefit_form_id': 22}))
        self.assertEqual(response.status_code, 200)

    def test_edit_user_benefit_form_get(self):
        request = self.factory.get('/users/55/benefit_forms/22/edit')
        response = benefit_forms.edit_user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_benefit_form_post(self):
        request = self.factory.post('/users/55/benefit_forms/22/edit')
        response = benefit_forms.edit_user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 405)

    def test_edit_user_benefit_form_put(self):
        request = self.factory.put('/users/55/benefit_forms/22/edit')
        response = benefit_forms.edit_user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 405)

    def test_edit_user_benefit_form_delete(self):
        request = self.factory.delete('/users/55/benefit_forms/22/edit')
        response = benefit_forms.edit_user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 405)

    def test_edit_user_benefit_form_patch(self):
        request = self.factory.patch('/users/55/benefit_forms/22/edit')
        response = benefit_forms.edit_user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 405)

# Tests checking that that '/users/:user_id/benefit_forms/benefit_form_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and benefit_form_id 22
class UserShowBenefitFormRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/benefit_forms/22
    # and ensuring the response code is 200 (OK)
    def test_user_benefit_form_route_exists(self):
        response = self.client.get(reverse('app:user_benefit_form', kwargs={'user_id': 55, 'benefit_form_id': 22}))
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_form_get(self):
        request = self.factory.get('/users/55/benefit_forms/22')
        response = benefit_forms.user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_form_post(self):
        request = self.factory.post('/users/55/benefit_forms/22')
        response = benefit_forms.user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 405)

    def test_user_benefit_form_put(self):
        request = self.factory.put('/users/55/benefit_forms/22')
        response = benefit_forms.user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_form_delete(self):
        request = self.factory.delete('/users/55/benefit_forms/22')
        response = benefit_forms.user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 200)

    def test_user_benefit_form_patch(self):
        request = self.factory.patch('/users/55/benefit_forms/22')
        response = benefit_forms.user_benefit_form(request, 55, 22)
        self.assertEqual(response.status_code, 200)


# Tests checking that that '/upload' properly handles HttpRequests and routing
# Accepts POST requests and refuses all others with an error code 405 (Method not allowed)
class UploadRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the /upload
    # and ensuring the response code is 200 (OK)
    def test_upload_route_exists(self):
        response = self.client.post(reverse('app:upload_benefit_form'))
        self.assertEqual(response.status_code, 200)

    def test_upload_get(self):
        request = self.factory.get('/upload')
        response = benefit_forms.upload(request)
        self.assertEqual(response.status_code, 405)

    def test_upload_post(self):
        request = self.factory.post('/upload')
        response = benefit_forms.upload(request)
        self.assertEqual(response.status_code, 200)

    def test_upload_put(self):
        request = self.factory.put('/upload')
        response = benefit_forms.upload(request)
        self.assertEqual(response.status_code, 405)

    def test_upload_delete(self):
        request = self.factory.delete('/upload')
        response = benefit_forms.upload(request)
        self.assertEqual(response.status_code, 405)

    def test_upload_patch(self):
        request = self.factory.patch('/upload')
        response = benefit_forms.upload(request)
        self.assertEqual(response.status_code, 405)

# Tests checking that that '/download' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DonwloadBenefitFormsRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the /download
    # and ensuring the response code is 200 (OK)
    def test_download_benefit_form_route_exists(self):
        response = self.client.get(reverse('app:download_benefit_form'))
        self.assertEqual(response.status_code, 200)

    def test_download_benefit_form_get(self):
        request = self.factory.get('/download')
        response = benefit_forms.download(request)
        self.assertEqual(response.status_code, 200)

    def test_download_benefit_form_post(self):
        request = self.factory.post('/download')
        response = benefit_forms.download(request)
        self.assertEqual(response.status_code, 405)

    def test_download_benefit_form_put(self):
        request = self.factory.put('/download')
        response = benefit_forms.download(request)
        self.assertEqual(response.status_code, 405)

    def test_download_benefit_form_delete(self):
        request = self.factory.delete('/download')
        response = benefit_forms.download(request)
        self.assertEqual(response.status_code, 405)

    def test_download_benefit_form_patch(self):
        request = self.factory.patch('/download')
        response = benefit_forms.download(request)
        self.assertEqual(response.status_code, 405)