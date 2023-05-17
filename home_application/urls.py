# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.conf.urls import url

from . import views

urlpatterns = (
   # url(r'^$', views.home),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
    # 添加 helloworld 路由
    url(r'^helloworld/$', views.helloworld),
    url(r'^python_homework1/$', views.python_homework1),
    url(r'^python_homework2/$', views.python_homework2),
    url(r'^python_homework3/$', views.python_homework3),
    url(r'^python_homework31/$', views.python_homework31),
    url(r'^python_homework32/$', views.python_homework32),
    url(r'^python_homework33/$', views.python_homework33),
    url(r"^frontend/$", views.frontend),
)
