from quality_indicators.api.repositories.materials_repository import MaterialsRepository


class MaterialService:
    def __init__(self):
        self.material_repository = MaterialsRepository()

    """
    Доступ к запросу на создание сырья
    """

    def create_material(self, material: str):
        return self.material_repository.create_material(material=material)

    """
    Доступ к запросу на создание показателей
    """

    def create_indicators(self, material: str, **kwargs):
        return self.material_repository.create_indicators(material=material, **kwargs)

    """
    Доступ к запросу на получение всего сырья.
    """

    def get_all_materials(self):
        return self.material_repository.get_all_materials()

    """
    Доступ к запросу получения максимальных, минимальных и средних значений показателей.
    """

    def get_values(self, material, date):
        return self.material_repository.get_values(material, date)
