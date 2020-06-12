# 导包
import unittest, logging
from api.login_api import LoginApi
from api.employee import DepartmentApi
import app
from parameterized import parameterized

# 创建测试类
from utils import assert_common, read_emp_data, read_login_data


class TestIHRMEmployeeParams02(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化部门
        self.emp_api = DepartmentApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filepath))
    # 实现登录成功的接口
    def test01_login_success(self, case_name, request_body, success, code, message, http_code):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(request_body, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果为：{}".format(response.json()))

        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS，供后续增删改查调用
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

        # 断言
        assert_common(self, http_code, success, code, message, response)

    # 定义部门模块的文件路径
    emp_filepath = app.BASE_DIR + "/data/emp_data002.json"

    # 参数化
    @parameterized.expand(read_emp_data(emp_filepath))
    def test02_add_emp(self, a, b, c, d, e, f, g, h, i, j, k, l, m):
        # 发送添加部门的接口请求
        response = self.emp_api.add_emp(a, b, c, d, app.HEADERS)
        # 打印添加部门的结果
        logging.info("添加部门的结果为：{}".format(response.json()))
        # 提取部门中的令牌并把部门令牌保存到全局变量中
        app.EMP_ID = response.json().get("data").get("id")
        # 打印保存的部门ID
        logging.info("保存到全局变量的部门的ID为：{}".format(app.EMP_ID))
        # 断言
        assert_common(self, h, e, f, g, response)

        # 发送查询部门的接口请求:
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询部门的数据
        logging.info("查询部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, h, e, f, g, response)

        # 调用封装的修改部门接口，发送接口请求
        response = self.emp_api.modify_emp(m, i, j, k, l, app.HEADERS)
        # 打印数据
        logging.info("修改部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

        # 调用封装的删除部门接口哦，发送接口请求
        response = self.emp_api.delete_emp(m, app.HEADERS)
        # 打印删除员工的结果为
        logging.info("删除部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)
