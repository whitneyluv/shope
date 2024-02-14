from ..models import Profile
from django.views.generic import View, DetailView


class ProfileView(DetailView):
    template_name = 'profile_app/profile.html'
    model = Profile
    context_object_name = 'profile'











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

