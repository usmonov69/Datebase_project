from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberChangeForm, MemberForm
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

def home(request):
	all_members = Member.objects.all
	return  render(request, 'home.html', {'all' : all_members})

def join(request):
		if request.method == 'POST':    
			form = MemberForm(request.POST or None)
			if form.is_valid():
				form.save()
			else: 
				fname = request.POST['fname']
				lname = request.POST['lname']
				age = request.POST['age']
				email = request.POST['email']
				passwd = request.POST['passwd']
				
				# address = request.POST['address']
				# phone_num = request.POST['phone_num']
				messages.success(request, ('There was error in your form! Please try again..:('))
				# return redirect('join')
				return render(request, 'join.html', {'fname' : fname, 
					'lname': lname,
					'age': age,
					'email': email,
					'passwd': passwd,
					# 'address' : passwd,
					# 'phone_num': phone_num,
					})
			
			messages.success(request, "Your Form Has Been Submitted Succesfully ")
			return redirect('home')
		else:
			return render(request, 'join.html', {})
			

# class join(LoginRequiredMixin, UserPassesTestMixin,CreateView ):
# 	form_class = MemberForm
# 	model = Member
# 	template_name = 'join.html'
# 	success_url = reverse_lazy('home')
	
# 			#add new views-----
# 	def form_valid(self, form):
# 		form.instance.author == self.request.user
# 		return super().form_valid(form)



class MemberDelete(DeleteView):
	model = Member
	template_name = 'delete.html'
	success_url = reverse_lazy('home')



class MemberUpdateView(UpdateView):
	model = Member
	template_name = 'edit.html'
	fields = ['fname', 'lname', 'email']



# def MemberUpdateView(request, pk):
# 	task = Member.objects.get(id=pk)
# 	form = MemberForm(instance=task)
# 	if request.method == 'POST':
# 		form = MemberForm(request, instance=task)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')

# 	return render( request, 'edit.html' )

class MemberDetailView(DetailView):
	model = Member
	template_name = 'detail.html'


class About(TemplateView):
	template_name = 'about.html'

# class Singup(TemplateView):
# 	form_class = MemberForm
# 	template_name = 'singup.html'
# 	success_url = reverse_lazy('home')

