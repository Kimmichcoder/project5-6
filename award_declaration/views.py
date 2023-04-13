import json
from datetime import datetime

from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

from blueapps import account
from .models import *
import os

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'award_declaration/index_home.html')
def organization(request):
    """
    组织管理首页
    """
    return render(request, 'award_declaration/organization/index.html')
def award(request):
    """
    奖项管理首页
    """
    return render(request, 'award_declaration/award/index.html')
def batch_copy(request):
    """
    批量克隆首页
    """
    return render(request, 'award_declaration/award/copy.html')
def get_org_list(request):
    """
    获取组织信息列表数据
    """
    # 获取操作次数
    draw = int(request.GET.get("draw"))
    # 获取起始位置
    start = int(request.GET.get("start"))
    organizations = Organization.objects.all()
    total = len(organizations)
    page_length = int(request.GET.get("length"))
    page = start / page_length + 1

    paginator = Paginator(organizations, page_length)
    organizations = paginator.get_page(page)
    result_data = []
    for organization_item in organizations:
        result_data.append(
            {
                "id": organization_item.id,
                "org_name": organization_item.org_name,
                "principal": ",".join(organization_item.principal.values_list("username", flat=True)),
                "apply_person": ",".join(organization_item.apply_person.values_list("username", flat=True)),
                "operator": organization_item.operator,
                "create_time": organization_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )
def get_org_info_by_id(request, org_id):
    """
    获取编辑的数据
    """
    try:
        org_info = Organization.objects.get(id=int(org_id))
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": {
                    "info": {
                        'data':
                            {
                                "id": org_info.id,
                                "org_name": org_info.org_name,
                                "principal": ",".join(org_info.principal.values_list("username", flat=True)),
                                "apply_person": ",".join(
                                    org_info.apply_person.values_list("username", flat=True))
                            }
                    }
                }
            }
        )
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "获取数据失败"})


def save_org_info(request):
    """
    保存组织信息
    """
    operator = request.user.username
    org_name = request.POST.get("org_name")
    principal_user_list = request.POST.get("principal").split(",")
    apply_person_list = request.POST.get("apply_person").split(",")

    users_model_object = account.get_user_model()
    users = users_model_object.objects.values_list("username", flat=True)
    need_add_principal_list = list(set(principal_user_list).difference(set(users)))

    org_id = request.POST.get("org_id", None)

    if org_id:
        # 修改数据
        try:
            with transaction.atomic():
                org_obj = Organization.objects.get(id=int(org_id))
                Organization.objects.filter(id=org_id).update(**{"org_name": org_name, "operator": operator})
                # 负责人关系维护
                for username in need_add_principal_list:
                    user = users_model_object(username=username, is_staff=True)
                    user.save()
                # 负责人关系维护
                # 1.清空旧的关系
                org_obj.principal.clear()
                # 2.新建与负责人关系
                org_obj.principal.set(users_model_object.objects.filter(username__in=principal_user_list))

                # 组织信息与可申报人关系
                users = users_model_object.objects.values_list("username", flat=True)
                need_add_apply_person_list = list(set(apply_person_list).difference(set(users)))
                for username in need_add_apply_person_list:
                    user = users_model_object(username=username, is_staff=True)
                    user.save()
                # 可申报人关系维护
                # 1.清空旧的可申报人关系
                org_obj.apply_person.clear()
                # 2.新建与可申报人关系
                org_obj.apply_person.set(users_model_object.objects.filter(username__in=apply_person_list))
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "error"})
    else:
        # 新增数据
        try:
            with transaction.atomic():
                # 组织名称是否存在
                if Organization.objects.filter(org_name=org_name):
                    return JsonResponse({"result": False, "code": 101, "message": "该组织名称已存在，无需添加"})
                organization = Organization(org_name=org_name, operator=operator)
                organization.save()
                # 负责人关系维护
                for username in need_add_principal_list:
                    user = users_model_object(username=username, is_staff=True)
                    user.save()
                # 添加组织与负责人对应关系
                organization.principal.set(users_model_object.objects.filter(username__in=principal_user_list))

                # 可申报人关系维护
                users = users_model_object.objects.values_list("username", flat=True)
                need_add_apply_person_list = list(set(apply_person_list).difference(set(users)))
                for username in need_add_apply_person_list:
                    user = users_model_object(username=username, is_staff=True)
                    user.save()
                # 添加组织与申报人对应关系
                organization.apply_person.set(users_model_object.objects.filter(username__in=apply_person_list))
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "error"})

    return JsonResponse({"result": True, "code": 200, "message": "success"})
def delete_org_info(request, org_id):
    """
    删除数据
    """
    try:
        with transaction.atomic():
            org_obj = Organization.objects.get(id=int(org_id))
            org_obj.principal.clear()
            org_obj.apply_person.clear()
            org_obj.delete()
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "删除数据失败"})
    return JsonResponse(
        {
            "result": True, "code": 200,
            "message": "success"
        }
    )
def get_award_list(request):
    """
    获取奖项信息列表数据
    """
    # 获取操作次数
    draw = int(request.POST.get("draw"))
    # 获取起始位置
    start = int(request.POST.get("start"))

    # 查询
    kwargs = {}
    if request.POST.get("search_award_name", ""):
        kwargs.update({"award_name__contains": request.POST.get("search_award_name")})
    if request.POST.get("search_org_name", ""):
        kwargs.update({"belonging_org__org_name__contains": request.POST.get("search_org_name")})
    if request.POST.get("search_status", "") and int(request.POST.get("search_status", "")) != -1:
        kwargs.update({"status": int(request.POST.get("search_status"))})
    if request.POST.get("search_apply_time", ""):
        kwargs.update({"end_time__gte": datetime.strptime(request.POST.get("search_apply_time"), '%Y-%m-%d')})
        kwargs.update({"start_time__lte": datetime.strptime(request.POST.get("search_apply_time"), '%Y-%m-%d')})
    awards = Award.objects.filter(**kwargs)
    total = len(awards)
    page_length = int(request.POST.get("length"))
    page = start / page_length + 1

    paginator = Paginator(awards, page_length)
    awards = paginator.get_page(page)
    result_data = []
    for award_item in awards:
        result_data.append(
            {
                "id": award_item.id,
                "belonging_org": award_item.belonging_org.org_name,
                "award_level": award_item.get_award_level_display(),
                "award_name": award_item.award_name,
                "status": award_item.status,
                "start_time": award_item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": award_item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "apply_person_num": award_item.apply_person_num,
                "award_person_num": award_item.award_person_num,
                "operator": award_item.operator,
                "create_time": award_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )
def get_org_select_data(request):
    """
    获取下拉框所属组织值
    """
    result = []
    org_data = Organization.objects.values("id", "org_name")
    for org_obj in org_data:
        result.append({"id": org_obj["id"], "text": org_obj["org_name"]})

    return JsonResponse({"result": True, "code": 200, "data": {"results": result}})
def save_award_info(request):
    """
    保存奖项数据
    """
    try:
        award_name = request.POST.get('award_name')
        requirement = request.POST.get('requirement')
        award_level = int(request.POST.get('award_level'))
        belonging_org = int(request.POST.get('belonging_org'))
        start_datetime = request.POST.get('start_datetime')
        end_datetime = request.POST.get('end_datetime')
        if start_datetime >= end_datetime:
            return JsonResponse({"result": False, "code": 101, "message": "结束日期不能小于等于开始日期"})
        need_attachment = 0 if request.POST.get('need_attachment') == "false" else 1
        status = 0 if request.POST.get('status') == "false" else 1
        kwargs = {
            "award_name": award_name,
            "requirement": requirement,
            "award_level": award_level,
            "belonging_org": Organization.objects.get(id=belonging_org),
            "start_time": start_datetime,
            "end_time": end_datetime,
            "need_attachment": need_attachment,
            "status": status,
        }
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "参数获取错误"})
    award_id = request.POST.get("award_id", None)
    if award_id:
        # 修改
        try:
            Award.objects.filter(id=award_id).update(**kwargs)
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "修改数据错误"})
    else:
        # 添加数据
        try:
            Award.objects.create(**kwargs)
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "保存数据错误"})
    return JsonResponse({"result": True, "code": 200, "message": "success"})
def get_award_info_by_id(request, award_id):
    """
    获取编辑的数据
    """
    try:
        award_item = Award.objects.get(id=int(award_id))
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": {
                    "info": {
                        'data': {
                            "id": award_item.id,
                            "belonging_org": award_item.belonging_org.id,
                            "award_level": award_item.award_level,
                            "award_name": award_item.award_name,
                            "status": award_item.status,
                            "need_attachment": award_item.need_attachment,
                            "requirement": award_item.requirement,
                            "start_time": award_item.start_time.strftime("%Y-%m-%d"),
                            "end_time": award_item.end_time.strftime("%Y-%m-%d"),
                            "apply_person_num": award_item.apply_person_num,
                            "award_person_num": award_item.award_person_num,
                            "operator": award_item.operator,
                            "create_time": award_item.create_time.strftime("%Y-%m-%d"),
                        }
                    }
                }
            }
        )
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "获取数据失败"})
def get_award_display_info_by_id(request, award_id):
    """
    获取显示的数据
    """
    try:
        award_item = Award.objects.get(id=int(award_id))
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": {
                    "info": {
                        'data': {
                            "id": award_item.id,
                            "belonging_org": award_item.belonging_org.org_name,
                            "award_level": award_item.get_award_level_display(),
                            "award_name": award_item.award_name,
                            "status": award_item.get_status_display(),
                            "need_attachment": award_item.get_need_attachment_display(),
                            "requirement": award_item.requirement,
                            "start_time": award_item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "end_time": award_item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "apply_person_num": award_item.apply_person_num,
                            "award_person_num": award_item.award_person_num,
                            "operator": award_item.operator,
                            "create_time": award_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    }
                }
            }
        )
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "获取数据失败"})
def delete_award_info(request, award_id):
    """
    删除数据
    """
    try:
        with transaction.atomic():
            award_obj = Award.objects.get(id=int(award_id))
            award_obj.delete()
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "删除数据失败"})
    return JsonResponse(
        {
            "result": True, "code": 200,
            "message": "success"
        }
    )
def get_award_copy_list(request):
    """
    获取奖项信息列表数据
    """
    # 获取操作次数
    draw = int(request.POST.get("draw"))
    # 获取起始位置
    start = int(request.POST.get("start"))

    # 查询
    kwargs = {}
    if request.POST.get("search_award_name", ""):
        kwargs.update({"award_name__contains": request.POST.get("search_award_name")})
    if request.POST.get("search_org_name", ""):
        kwargs.update({"belonging_org__org_name__contains": request.POST.get("search_org_name")})
    if request.POST.get("search_status", "") and int(request.POST.get("search_status", "")) != -1:
        kwargs.update({"status": int(request.POST.get("status"))})
    if request.POST.get("search_apply_time", ""):
        kwargs.update({"end_time__gte": datetime.strptime(request.POST.get("search_apply_time"), '%Y-%m-%d')})
        kwargs.update({"start_time__lte": datetime.strptime(request.POST.get("search_apply_time"), '%Y-%m-%d')})

    awards = Award.objects.filter(**kwargs)
    total = len(awards)
    page_length = int(request.POST.get("length"))
    page = start / page_length + 1

    paginator = Paginator(awards, page_length)
    awards = paginator.get_page(page)
    award_name = request.POST.get("old_award_name", "")
    start_time = request.POST.get("start_time", "")
    end_time = request.POST.get("end_time", "")

    org_name = ""
    if request.POST.get("belonging_org", ""):
        org_name = Organization.objects.get(id=int(request.POST.get("belonging_org"))).org_name

    result_data = []
    for award_item in awards:
        new_award_name = award_item.award_name
        if award_name in award_item.award_name:
            new_award_name = award_item.award_name.replace(award_name, request.POST.get("new_award_name"))
        result_data.append(
            {
                "id": award_item.id,
                "belonging_org": org_name if org_name else award_item.belonging_org.org_name,
                "award_level": award_item.get_award_level_display(),
                "old_award_name": award_item.award_name,
                "new_award_name": new_award_name,
                "status": award_item.status,
                "start_time": start_time if start_time else award_item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": end_time if end_time else award_item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "create_time": award_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )
def batch_copy_award_data(request):
    """
    批量克隆数据保存
    """
    data = json.loads(request.POST.get('data'))
    copy_data = []
    for award in data:
        if award["new_award_name"] and award["start_time"] and award["end_time"]:
            award_obj = Award.objects.get(id=award["id"])
            copy_data.append(Award(
                award_name=award["new_award_name"],
                requirement=award_obj.requirement,
                award_level=award_obj.award_level,
                belonging_org=Organization.objects.get(org_name=award['belonging_org']),
                start_time=award["start_time"],
                end_time=award["end_time"],
                need_attachment=award_obj.need_attachment,
                status=award_obj.status,
            ))
    try:
        Award.objects.bulk_create(copy_data)
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "批量克隆数据失败"})
    return JsonResponse(
        {
            "result": True, "code": 200,
            "message": "success"
        }
    )
def personal_center(request):
    """
    个人中心首页
    """
    return render(request, 'award_declaration/personal_center/index.html')


def review(request):
    """
    我的审核首页
    """
    return render(request, 'award_declaration/personal_center/review.html')

SAVE_DIR = "./static/file"

def get_application_list(request):
    """
    获取申报奖项列表数据
    """
    # 获取操作次数
    draw = int(request.GET.get("draw"))
    # 获取起始位置
    start = int(request.GET.get("start"))
    # 根据登录的用户获取属于自己可以申报的奖项申报记录
    awards = Award.objects.filter(belonging_org__apply_person__username=request.user.username)
    total = len(awards)
    page_length = int(request.GET.get("length"))
    page = start / page_length + 1

    paginator = Paginator(awards, page_length)
    awards = paginator.get_page(page)
    result_data = []
    for award_item in awards:
        # 获取该奖项的申报记录
        apply = Application.objects.filter(award_id=award_item.id).first()
        result_data.append(
            {
                "apply_id": apply.id if apply else "",
                "award_id": award_item.id,
                "org_name": award_item.belonging_org.org_name,
                "award_name": award_item.award_name,
                "award_status": award_item.get_status_display(),
                "applicant_info": apply.applicant_info if apply else "",
                "state": apply.get_state_display() if apply else "未申报",
                "apply_time": apply.apply_time.strftime("%Y-%m-%d %H:%M:%S") if apply else "",
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )


from datetime import datetime, timezone


def save_apply_award_info(request):
    """
    保存或编辑申报信息
    """
    applicant_id = request.POST.get("applicant_id", "")
    award_id = request.POST.get("award_id", "")
    file_obj = request.FILES.get('file', "")
    applicant = request.user.username
    applicant_info = request.POST.get("applicant_info", "")
    introduction = request.POST.get("introduction", "")

    if not award_id:
        return JsonResponse({"result": False, "code": 101, "message": "参数错误"})
    award_info = Award.objects.get(id=award_id)
    if award_info.status == ApplyStatus.EXPIRED:
        return JsonResponse({"result": False, "code": 101, "message": "该奖项已过期，无法申请"})
    if datetime.now() < award_info.start_time:
        return JsonResponse({"result": False, "code": 101, "message": "该奖项未开放，暂时无法申请"})
    if datetime.now() > award_info.end_time:
        return JsonResponse({"result": False, "code": 101, "message": "该奖项已过期，无法申请"})

    if not applicant_id:
        if award_info.need_attachment and not file_obj:
            return JsonResponse({"result": False, "code": 101, "message": "该奖项必须上传附件"})
    file_url = ""
    kwargs = {}
    if file_obj:
        if file_obj.name.split(".") == 0 or file_obj.name.split(".") == 1:
            return JsonResponse({"result": False, "code": 101, "message": "文件名错误，无扩展名称或无文件名称"})

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        new_file_name = "{}.{}".format(str(uuid.uuid4()), ".".join(file_obj.name.split(".")[1:]))
        if file_obj:
            with open(os.path.join(SAVE_DIR, new_file_name), 'wb') as w:
                for block in file_obj.chunks():
                    w.write(block)
        file_url = str(os.path.join(SAVE_DIR, new_file_name))
        kwargs.update({"attachment_name": file_obj.name, "attachment_url": file_url})
    kwargs.update({"award": award_info, "introduction": introduction, "applicant_info": applicant_info,
                   "last_modify": User.objects.get(username=applicant), "last_modify_time": datetime.now(),
                   "attachment_url": file_url})
    try:
        with transaction.atomic():
            if not applicant_id:
                # 保存
                kwargs.update({"applicant": User.objects.get(username=applicant), "apply_time": datetime.now(),
                               "state": ApplyState.UNDER_REVIEW})
                Application.objects.create(**kwargs)
                Award.objects.filter(id=award_info.id).update(apply_person_num=award_info.apply_person_num + 1)
            else:
                # 修改
                comment = request.POST.get("comment", "")
                if comment:
                    kwargs.update({"comment": comment})
                state = request.POST.get("state", "")
                if state:
                    kwargs.update({"state": state})

                Application.objects.filter(id=applicant_id).update(**kwargs)
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "保存失败"})

    return JsonResponse({"result": True, "code": 200, "message": "success", "data": {}})
def get_apply_info_by_id(request, award_id, apply_id):
    """
    获取编辑的数据
    """
    try:
        award_item = Award.objects.get(id=int(award_id))
        apply_info = Application.objects.get(id=int(apply_id))
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": {
                    "info": {
                        'data': {
                             "id": award_item.id,
                             "belonging_org": award_item.belonging_org.org_name,
                             "award_level": award_item.get_award_level_display(),
                             "award_name": award_item.award_name,
                             "status": award_item.get_status_display(),
                             "need_attachment": award_item.get_need_attachment_display(),
                             "requirement": award_item.requirement,
                             "start_time": award_item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                             "end_time": award_item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                             "apply_person_num": award_item.apply_person_num,
                             "award_person_num": award_item.award_person_num,
                             "operator": award_item.operator,
                             "create_time": award_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                             "applicant_info": apply_info.applicant_info,
                             "applicant_id": apply_info.id,
                             "introduction": apply_info.introduction,
                             "attachment_url": apply_info.attachment_url
                        }
                    }
                }
            }
        )
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "获取数据失败"})
def get_display_award_apply_info_by_id(request, award_id, apply_id):
    """
    获取查看的数据
    """
    try:
        award_item = Award.objects.get(id=int(award_id))
        apply_info = Application.objects.get(id=int(apply_id))
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": {
                    "info": {
                        'data': {
                            "id": award_item.id,
                            "belonging_org": award_item.belonging_org.org_name,
                            "award_level": award_item.get_award_level_display(),
                            "award_name": award_item.award_name,
                            "status": award_item.get_status_display(),
                            "need_attachment": award_item.get_need_attachment_display(),
                            "requirement": award_item.requirement,
                            "start_time": award_item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "end_time": award_item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "apply_person_num": award_item.apply_person_num,
                            "award_person_num": award_item.award_person_num,
                            "operator": award_item.operator,
                            "create_time": award_item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "award_id": award_item.id,
                            "apply_id": apply_info.id,
                            "applicant_info": apply_info.applicant_info,
                            "introduction": apply_info.introduction,
                            "attachment_url": apply_info.attachment_url,
                            "comment": apply_info.comment,
                            "state": apply_info.get_state_display()
                        }
                    }
                }
            }
        )
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "获取数据失败"})
def get_review_list(request):
    """
    获取需要审核的记录列表
    """
    # 获取操作次数
    draw = int(request.GET.get("draw"))
    # 获取起始位置
    start = int(request.GET.get("start"))
    # 根据登录的用户获取属于自己管理的奖项申报记录
    applications = Application.objects.filter(award__belonging_org__principal__username=request.user.username)
    total = len(applications)
    page_length = int(request.GET.get("length"))
    page = start / page_length + 1

    paginator = Paginator(applications, page_length)
    applications = paginator.get_page(page)
    result_data = []
    for application_item in applications:
        result_data.append(
            {
                "id": application_item.id,
                "award_id": application_item.award.id,
                "application_id": application_item.id,
                "org_name": application_item.award.belonging_org.org_name,
                "award_name": application_item.award.award_name,
                "award_status": application_item.award.get_status_display(),
                "applicant_info": application_item.applicant_info,
                "state": application_item.get_state_display(),
                "apply_time": application_item.apply_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )
def review_apply_award(request):
    """
    审核申报奖项
    """
    action = request.POST.get("action", "")
    apply_id = request.POST.get("id", "")
    if not apply_id:
        return JsonResponse({"result": False, "code": 101, "message": "获取审批数据错误"})
    if action == "1":
        Application.objects.filter(id=int(apply_id)).update(state=ApplyState.PASSED)
    elif action == "0":
        Application.objects.filter(id=int(apply_id)).update(state=ApplyState.NO_PASS)
    else:
        return JsonResponse({"result": False, "code": 101, "message": "审批错误，无发执行审批操作"})
    return JsonResponse({"result": True, "code": 200, "message": "success", "data": {}})
def save_awards_apply_info(request):
    """
    评奖
    """
    comment = request.POST.get("comment", "")
    state = request.POST.get("state", "")
    apply_id = request.POST.get("apply_id", "")
    award_id = request.POST.get("award_id", "")
    if not apply_id and not award_id:
        return JsonResponse({"result": False, "code": 101, "message": "获取评奖数据错误"})
    try:
        with transaction.atomic():
            Application.objects.filter(id=int(apply_id)).update(state=int(state), comment=comment)
            award_info = Award.objects.get(id=award_id)
            if int(state) == ApplyState.GET_AWARD:
                Award.objects.filter(id=award_id).update(award_person_num=award_info.apply_person_num)
    except Exception:
        return JsonResponse({"result": False, "code": 101, "message": "error"})

    return JsonResponse({"result": True, "code": 200, "message": "success", "data": {}})
def home(request):
    """
    首页
    """
    # 根据登录的用户获取属于自己可以申报的奖项申报记录
    awards = Award.objects.filter(belonging_org__apply_person__username=request.user.username,
                                  status=ApplyStatus.EFFECT, start_time__lte=datetime.now(),
                                  end_time__gte=datetime.now())
    result_data = []
    for award_item in awards:
        result_data.append(
            {
                "award_id": award_item.id,
                "org_name": award_item.belonging_org.org_name,
                "award_name": award_item.award_name,
                "apply_person_num": award_item.apply_person_num,
                "award_person_num": award_item.award_person_num,
            }
        )
    return render(request, 'award_declaration/index_home.html', {"award_data": result_data})
def get_awarded_list(request):
    """
    获取获奖信息列表数据
    """
    # 获取操作次数
    draw = int(request.GET.get("draw"))
    # 获取起始位置
    start = int(request.GET.get("start"))
    applies = Application.objects.filter(state=ApplyState.GET_AWARD)
    total = len(applies)
    page_length = int(request.GET.get("length"))
    page = start / page_length + 1

    paginator = Paginator(applies, page_length)
    applies = paginator.get_page(page)
    result_data = []
    for apply_item in applies:
        result_data.append(
            {
                "id": apply_item.id,
                "award_id": apply_item.award.id,
                "apply_id": apply_item.id,
                "belonging_org": apply_item.award.belonging_org.org_name,
                "award_name": apply_item.award.award_name,
                "apply_time": apply_item.apply_time.strftime("%Y-%m-%d %H:%M:%S"),
                "applicant_info": apply_item.applicant_info,
            }
        )
    return JsonResponse(
        {
            "result": True, "code": 200,
            "data": {
                "info": {
                    'data': result_data,
                    "recordsTotal": total,
                    "recordsFiltered": total,
                    "draw": draw,
                }
            }
        }
    )