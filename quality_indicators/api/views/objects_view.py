from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from quality_indicators.api.serializers.materials_serializer import RawMaterialsSerializer
from quality_indicators.api.services.materials_service import MaterialService

"""
Эндпоинт для получения отчета с минимальными, максимальными и средними показателями для каждого сырья.
"""


@api_view(['GET'])
def show_report(request, date: str):
    data = MaterialService().get_all_materials()
    ser1 = RawMaterialsSerializer(data=data, many=True, context={"date": date})
    ser1.is_valid()
    return Response(ser1.data)


"""
Эндпоинт для добавления сырья и качественных показателей к нему.
"""


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_objects(request):
    if request.user.is_authenticated:
        data = request.data['materials']
        for i, k in data.items():
            MaterialService().create_material(material=i)
            MaterialService().create_indicators(material=i, **k)
        return Response({"Upload": "Success"})
