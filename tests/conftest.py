# -*-coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fix = Application()
    fix.session.login(username="admin", password="secret")

    def fin():
        fix.session.logout()
        fix.destroy()

    request.addfinalizer(fin)
    return fix
