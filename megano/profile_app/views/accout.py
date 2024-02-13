from django.http import HttpRequest, FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from ..models import Profile
from django.views.generic import View, DetailView


class AccountView(DetailView):
    template_name = 'profile_app/account/html'













# class AccountView(View):
#
#     @staticmethod
#     def get(request: HttpRequest):
#         context = {
#             'tasks': TaskModel.objects.all()
#         }
#         return render(request, 'tasks.html', context=context)
#
#     @staticmethod
#     def post(request):
#         file = request.FILES['myfile']
#         new_task = TaskModel(name=file.name)
#         new_task.save()
#         workbook = load_workbook(file)
#         worksheet = workbook.active
#         for row in worksheet.iter_rows(values_only=True):
#             new_item = ItemModel(task_id=new_task, article=row[0], brand=row[1])
#             new_item.save()
#         return redirect('congratulations_download')

