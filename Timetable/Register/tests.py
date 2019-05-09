from django.test import SimpleTestCase ,TestCase
from django.urls import reverse, resolve
#from Timetable.Register.views import login, register, courses, forgot, resetp, astudent
from django.test import TestCase, Client
from Timetable.Register.models import StudentsRegister, Lecturer, Login, Courses, Announcements, Class, RegisteredStd, RegisteredStaffs
from django.utils import timezone


class TestUrls(TestCase):
    def test_login_url_resolved(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, 'login')


    def test_register_url_resolved(self):
        url = reverse('register')

        self.assertEquals(resolve(url).func, 'register')

    def test_Confirm_log(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func, 'courses')

    def test_forgot(self):
        url = reverse('forgot')
        self.assertEquals(resolve(url).func, 'forgot')

    def test_reset(self):
        url = reverse('reset')
        self.assertEquals(resolve(url).func, 'resetp')

class TestViews(TestCase):
        def setUp(self):
            self.client = Client()
            self.login_url = reverse('login')
            self.confirm_log = reverse('confirm_log')
            self.reset = reverse('reset')
            self.forgot = reverse('forgot')
            self.Reg = reverse('Reg')


        def  test_project_login_GET(self):

             response = self.client.get(self.login_url)

             self.assertEquals(response.status_code, 200)
             self.assertTemplateUsed(response, 'Register/Log_in.html')

        def test_confirm_login(self):
            response = self.client.get(self.confirm_log)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Log_in.html')

        def test_forgot(self):
            response = self.client.get(self.forgot)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/forgot.html')

        def test_reset(self):

            response = self.client.get(self.reset)
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response,'Register/reset.html')




class EntryModelTest(TestCase):

    def create_whatever(self, Student_No = 123,
                              Name = 'ask',
                              Email = 's@mail.com',
                              Password = 'abc123',

                        ):

        return StudentsRegister.objects.create( Student_No =Student_No ,
                                                Name =Name ,
                                                Email =Email ,
                                                Password =Password ,

                                                )

    def create_course(self,Course_Code = 'Coms203',
                           Course_Name ='SD'
                      ):
        return Courses.objects.create(Course_Code =Course_Code ,
                                      Course_Name =Course_Name
                                     )

    def create_Announcement(self, Course_Code = Courses(Course_Code='Coms203'),
                                  Lect_No = Lecturer(Lect_No=1234),
                                  Title = 'seven',
                                  Content = 'testing'
                           ):

        return Announcements.objects.create(Course_Code =Course_Code,
                                            Lect_No =Lect_No,
                                            Title =Title,
                                            Content =Content,
                                            Created = timezone.now()
                                            )

    def create_Lecturer(self, Lect_No = 1234,
                              Name = 'assk',
                              Email = 'ss@mail.com',
                              Password = 'abc1233',

                        ):

        return Lecturer.objects.create(Lect_No=Lect_No,
                                       Name =Name ,
                                       Email =Email ,
                                       Password =Password ,

                                       )
    def create_Class(self, Student_No = StudentsRegister(Student_No =123),
                           Course_Code = Courses(Course_Code ='Coms203'),
                           Lect_No =Lecturer(Lect_No =1234),
                           Slot = 'A'
                        ):
        Class.save(Student_No)

        return Class.objects.create(Student_No =Student_No,
                                    Course_Code=Course_Code,
                                    Lect_No=Lect_No,
                                    Slot =Slot
                                    )

    def create_RStaff(self, Staff_no='1234',
                            Course_Code=Courses(Course_Code='Coms203')
                        ):

        return RegisteredStaffs.objects.create(Staff_no =Staff_no,
                                               Course_Code=Course_Code
                                              )

    def create_Rstudent(self, Std_no='123444',
                              Course_Code=Courses(Course_Code='Coms203')
                        ):

        return RegisteredStd.objects.create(Std_no =Std_no,
                                            Course_Code=Course_Code
                                           )

    def create_Login(self, Student_No = StudentsRegister(Student_No =123),
                           Password ='123'
                        ):
        Login.save(Student_No)
        return Login.objects.create(Student_No =Student_No,
                                    Password =Password
                                           )



    def test_Register(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w,StudentsRegister))
        self.assertEqual(str(w),w.Name)

    def test_login(self):

        s = self.create_Login()
        self.assertTrue(isinstance(s,Login))
        self.assertEqual(str(s),s.Password)

    def test_Lecturer(self):

        e = Lecturer(Lect_No = '125')
        self.assertEqual(str(e),e.Lect_No )


    def test_Courses(self):

        s = self.create_course()
        self.assertTrue(isinstance(s, Courses))
        self.assertEqual(str(s),s.Course_Code)


    def test_Announcement(self):

       t = self.create_Announcement()
       self.assertTrue(isinstance(t, Announcements))
       self.assertEqual(str(t), t.Title)


    def test_Class(self):

        l = self.create_Class()

        self.assertTrue(isinstance(l, Class))
        self.assertEqual(str(l), l.Slot)

    def test_Rstaffs(self):

        i = self.create_RStaff()

        self.assertTrue(isinstance(i, RegisteredStaffs))
        self.assertEqual(str(i), i.Staff_no)

    def test_Rstudents(self):

        a = self.create_Rstudent()

        self.assertTrue(isinstance(a, RegisteredStd))
        self.assertEqual(str(a), a.Std_no)