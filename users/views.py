from django.contrib.auth import login
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'skystore.blog@mail.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
