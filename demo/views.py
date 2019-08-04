import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["百词斩", "酷安", "藏书馆"])
        .add_yaxis("总计平均评分", [randrange(80, 95)/10 for _ in range(3)])
        .add_yaxis("今日平均评分", [randrange(80, 95)/10 for _ in range(3)])
        .set_global_opts(title_opts=opts.TitleOpts(title="应用数据统计", subtitle="分数统计"))
        .dump_options()
    )
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("demo/templates/index.html").read())
