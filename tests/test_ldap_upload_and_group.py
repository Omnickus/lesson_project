# Импорты для pytest
import pytest
import allure
from src.object_ldap_upload_and_group import Ldap_upload_and_group

from src.base.logger import log_decorator

@pytest.mark.ldap_upload
class Test_Ldap_upload_and_group:

    @allure.description("Выгрузка группы LDAP")
    @allure.feature("Группы LDAP")
    @allure.story("Выгрузка группы LDAP")
    @allure.step
    @pytest.mark.parametrize('name_group', Ldap_upload_and_group.name_group_for_upload)
    def test_creat_new_allowed_addresses(self, driver, name_group):
        @log_decorator
        def start():
            Ldap_upload_and_group(driver).upload_group_ldap(name_group)
        start()

