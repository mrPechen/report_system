from django.db.models import Min, Max, Avg

from quality_indicators.api.models import RawMaterials, QualityIndicators
import datetime


class MaterialsRepository:
    def __init__(self):
        self.material_model = RawMaterials
        self.indicator_model = QualityIndicators

    """
    Запрос для создания сырья.
    """

    def create_material(self, material: str):
        exist_material = self.material_model.objects.filter(name=material).exists()
        if not exist_material:
            result = self.material_model.objects.create(name=material)
            result.save()
            return result

    """
    Запрос для создания качественных показателей.
    """

    def create_indicators(self, material: str, **kwargs):
        material_id = self.material_model.objects.get(name=material)
        date_data = datetime.datetime.strptime(kwargs['upload_date'], '%d-%m-%Y').date()
        kwargs['upload_date'] = date_data
        result = self.indicator_model.objects.create(raw_materials=material_id, **kwargs)
        result.save()
        return result

    """
    Запрос для получения всего сырья.
    """

    def get_all_materials(self):
        result = self.material_model.objects.all()
        return result

    """
    Запрос для получения минимальных, максимальных и средних значений всех качественных показателей
    для каждого сырья.
    """

    def get_values(self, material, date):
        date_data = datetime.datetime.strptime('01-' + date, '%d-%m-%Y').date()
        month = date_data.month
        year = date_data.year
        check_date = self.indicator_model.objects.filter(upload_date__month=month, upload_date__year=year).exists()
        if check_date:
            material_id = self.material_model.objects.get(id=material).id
            result = self.indicator_model.objects.filter(raw_materials=material_id, upload_date__month=month,
                                                         upload_date__year=year).aggregate(
                iron_min_value=Min('iron_content'),
                iron_max_value=Max('iron_content'),
                iron_average_value=Avg('iron_content'),
                silicon_min_value=Min('silicon_content'),
                silicon_max_value=Max('silicon_content'),
                silicon_average_value=Avg('silicon_content'),
                aluminum_min_value=Min('aluminum_content'),
                aluminum_max_value=Max('aluminum_content'),
                aluminum_average_value=Avg('aluminum_content'),
                calcium_min_value=Min('calcium_content'),
                calcium_max_value=Max('calcium_content'),
                calcium_average_value=Avg('calcium_content'),
                sulfur_min_value=Min('sulfur_content'),
                sulfur_max_value=Max('sulfur_content'),
                sulfur_average_value=Avg('sulfur_content')
            )

            return result
