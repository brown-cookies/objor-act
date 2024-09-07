from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from project.models import Project

from contact.forms import ContactForm
from contact.models import Contact


class IndexPage(TemplateView):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):

        form = ContactForm()

        projects = Project.objects.all()

        context = {
            "projects": projects,
            "form": form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)

        projects = Project.objects.all()

        context = {
            "projects": projects,
            "form": form,
        }

        if form.is_valid():
            form.save()
            context["form_success"] = True
            context["form_error"] = False
        else:
            context["form_success"] = False
            context["form_error"] = True

        return render(request, self.template_name, context=context)


class DetailPage(DetailView):
    template_name = "pages/detail.html"
    context_object_name = "project"
    model = Project


class ContactInquiries(ListView):
    template_name = "pages/contact_inquiries.html"
    context_object_name = "contacts"
    model = Contact


def contact_page(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"form": form})
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def home_page(request):
    return render(request, "home.html")


def inquiry_list_page(request):
    return render(request, "inquiry_list.html")


def project_detail_page(request):
    return render(request, "project_detail.html")


def project_list_page(request):
    return render(request, "project_list.html")
