from rest_framework import serializers
from quality_indicators.api.models import RawMaterials
from quality_indicators.api.services.materials_service import MaterialService

"""
Сериализатор для обработки минимальных, максимальных и средних значений сырья.
"""


class QualityIndicatorsSerializer(serializers.ModelSerializer):
    indicators = serializers.SerializerMethodField()

    def get_indicators(self, obj):
        material_id = obj.id
        print(material_id)
        date = self.context['date']
        result = MaterialService().get_values(material=material_id, date=date)
        return result


"""
Сериализатор для обработки конечного результата. Унаследован от "QualityIndicatorsSerializer",
чтобы перебросить данные минимальных, максимальных и средних значений сырья.
"""


class RawMaterialsSerializer(QualityIndicatorsSerializer):
    class Meta:
        model = RawMaterials
        fields = ['name', 'indicators']
