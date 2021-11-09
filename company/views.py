import random

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from app.models import *
from app.utils import *
from app.decorators import allowed_users

group_cmp = 'Company'


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def dashboardCmp(request):
    posts = InfluencerPost.objects.all().order_by("-id")
    nav_field = [i.field for i in posts]
    saved_posts = CmpSavePost.objects.filter(who_saved=User.objects.get(id=request.user.id))
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {
               'posts':posts,
               'nav_fields':list(set(nav_field)),
               'saved_post_ls':saved_post_ls
               }           
    return render(request, 'company/index.html', content)


   


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def dashboardFilter(request):
    data = request.GET.get('object')
    if data == 'ALL':
        posts = InfluencerPost.objects.all().order_by('-id')
    else:
        posts = InfluencerPost.objects.filter(field=data).order_by('-id')
    saved_posts = CmpSavePost.objects.filter(who_saved=User.objects.get(id=request.user.id))
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {'posts':posts,
               'saved_post_ls':saved_post_ls
               }
    template = render_to_string('company/ajax_temp/dashboard_filter.html', content)
    return JsonResponse({'data': template})    


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def saved_post_view(request):
    saved_posts = CmpSavePost.objects.filter(who_saved=User.objects.get(id=request.user.id)).order_by("-id")
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {'posts':saved_posts,
               'saved_post_ls':saved_post_ls,
               }
    return render(request, 'company/save_post.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def payment(request, post_id):
    post = InfluencerPost.objects.filter(id=post_id).first()
    if request.method == 'POST':
        Sponsored.objects.create(
            influencer=post.influencer,
            ## change after sponsor
            sponsor=User.objects.get(id=request.user.id),
            mode_of_sponsorship='online',
            amount=post.price,
            transaction_id=random.randint(11111111, 99999999),
            complete=True,
            post=post
        )
        return JsonResponse('Done', safe=True)
    content = {'post':post, 'id':post_id}
    return render(request, 'company/payment.html', content)


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def transaction(request):
    ##change
    sponsored_details = Sponsored.objects.filter(sponsor=User.objects.get(username=request.user.username))
    content = {'sponsored_details':sponsored_details}
    return render(request, 'company/transaction.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def sponsored(request):
    # change
    sponsored_details = Sponsored.objects.filter(sponsor=User.objects.get(username=request.user.username))
    posts = [i.post for i in sponsored_details]
    content = {'posts':posts}
    return render(request, 'company/history.html', content)
