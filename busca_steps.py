from behave import given, when, then

from util import utilss

util = utilss()


@given(u'que eu acesso o site do Python')
def step_impl(context):

    util.navegador('https://www.python.org/')


@given(u'preencho o input de pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão de pesquisar')


@when(u'clico no botão de pesquisar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão de pesquisar')


@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo visualizar os resultados da pesquisa')
