from django.forms import ModelForm

from grocery_store.models import Employee, Feedback


class EmployeeRegisterForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
