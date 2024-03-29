# check fixture execute with cmd '--setup-show'
import signal
import sys
from functools import wraps

import pytest
import pytest_rerunfailures
from _pytest.fixtures import resolve_fixture_function, FixtureDef, SubRequest

from lib.Dict import Dict
from lib.base_test_case import get_testdata
from _pytest.runner import runtestprotocol
from _pytest.runner import pytest_runtest_makereport
from _pytest.fixtures import pytest_fixture_setup as pfs

GDATA = {}


@pytest.fixture()
def some_data():
    return 22


@pytest.fixture(name="rename_fixture")
def some_data2():
    return 22


# @pytest.fixture(scope="session", autouse=True)
# def session_fixture():
#     print("session setup")
#     yield
#     print("session teardown")


# @pytest.fixture(scope="function")
# def my_fixture(tmpdir):
#     print("function setup")
#     yield
#     print("function teardown")


def pytest_sessionstart(session):
    print("session_start")
    print(session.config.getoption("--xb"))
    sys.argv.append("--ignore=cases/mock")


#
#
# def pytest_sessionfinish(session):
#     print("session_finish")

# 会在pytest自己的框架上包装，tryfirst=True 执行先执行自己的hook
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    # cur_result = result.setdefault(get_raw_id(item), {})
    # cur_result[len(cur_result) + 1] = {
    #     'setup': False,
    #     'call': False,
    #     'teardown': False,
    #     'start': t,
    #     'spend': 0
    # }
    # print("each test case:", item)
    # set_signal()
    out = yield


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_call(item):
    # set_signal()
    out = yield
    # if out:
    #     pass
    # release_signal()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    # print(item, nextitem)
    # set_signal()
    out = yield
    # for m in item.cls.pytestmark:
    #     if 'dependence' == m.name:
    #         global G_FAILED
    #         if G_FAILED:
    #             pytest.fail("dependence")
    # release_signal()


#
#
# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "xbxb: test xbxb"
#     )
#
#
# def pytest_cmdline_main(config):
#     print("cmdline")
#
#
# def pytest_runtest_protocol(item, nextitem):
#     print("runtest_protocol: ", item, nextitem)
#
#
# def pytest_runtest_logstart(nodeid, location):
#     print("runtest_logstart: ", nodeid, location)
#
#
# def pytest_runtest_setup(item):
#     print("runtest_setup: ", item)
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)

# # ui test
# if browser_option.screen_shot:
#     report_dir = browser_option.report_dir
#     picture_name = item.name + '.png'
#     picture_path = join(report_dir, picture_name)
#     context.browser.save_screenshot(picture_path)


#
# def pytest_collectstart(collector):
#     '''collector starts collecting.'''
#     print(collector)
#
#
# def pytest_itemcollected(item):
#     '''we just collected a test item.'''
#     print(item)
#
#
# def pytest_collectreport(report):
#     '''collector finished collecting.'''
#     print(report)
#
#
# def pytest_runtest_logreport(report):
#     '''process a test setup/call/teardown report relating to the respective phase of executing a test.'''
#     print(report)

# def pytest_itemcollected(item):
#     # modify test case name
#     item._nodeid = item.nodeid + "\n"

def get_reruns_count(item):
    return 2


def get_reruns_delay(item):
    return 3


# 决定重试次数和时间
# pytest_rerunfailures.get_reruns_count = get_reruns_count
# pytest_rerunfailures.get_reruns_delay = get_reruns_delay

# do some ignore
# def pytest_ignore_collect(path, config):
#     if "cases" == path.basename:
#         return True  # true mean ignore
#     return False  # false mean collect


def pytest_generate_tests(metafunc):
    test_module_path = metafunc.module.__file__
    function_name = metafunc.function.__name__
    # 文件级case缓存，一次加载多次使用
    if test_module_path not in GDATA:
        # 新增支持yaml数据格式
        test_data = get_testdata(test_module_path, function_name, file_type='yaml')
        # test_data = get_testdata(test_module_path, function_name, file_type='json')
        if test_data:
            GDATA[test_module_path] = test_data
    else:
        test_data = GDATA[test_module_path]
    # 数据驱动
    func_test_data = test_data[function_name]
    test_data_ = [Dict(i) for i in func_test_data]
    metafunc.parametrize("data", test_data_)


def pytest_collection_modifyitems(session, config, items):
    """ called after collection is completed
        you can modify the ``items`` list
    """
    pass
    # print(session, config, items, )


time_out = 100000000


def set_signal():
    signal.signal(signal.SIGALRM, timeout_func)
    signal.setitimer(signal.ITIMER_REAL, time_out)


def release_signal():
    signal.setitimer(signal.ITIMER_REAL, 0)
    signal.signal(signal.SIGALRM, signal.SIG_DFL)


def timeout_func(signum, frame):
    pytest.fail('test case timeout，current timeout is {}s'.format(time_out))


@pytest.fixture()
def get_data_from_json(request):
    print("print from fixture:", request.node.funcargs)


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_fixture_setup(fixturedef: FixtureDef[_FixtureValue], request: SubRequest):
#     pfs(fixturedef,request)
#     print(1)
#     kwargs = {}
#     # for argname in fixturedef.argnames:
#     #     fixdef = request._get_active_fixturedef(argname)
#     #     assert fixdef.cached_result is not None
#     #     result, arg_cache_key, exc = fixdef.cached_result
#     #     request._check_scope(argname, request.scope, fixdef.scope)
#     #     kwargs[argname] = result
#
#     fixturefunc = resolve_fixture_function(fixturedef, request)
#     my_cache_key = fixturedef.cache_key(request)
#     try:
#         result = call_fixture_func(fixturefunc, request, kwargs)
#     except TEST_OUTCOME:
#         exc_info = sys.exc_info()
#         assert exc_info[0] is not None
#         fixturedef.cached_result = (None, my_cache_key, exc_info)
#         raise
#     fixturedef.cached_result = (result, my_cache_key, None)
#     return result

# 注册自定义参数 cmdopt 到配置对象
def pytest_addoption(parser):
    parser.addoption("--xb",
                     action="store",
                     default="None",
                     help="将自定义命令行参数 ’--cmdopt' 添加到 pytest 配置中")
