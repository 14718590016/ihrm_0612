# 导包
import requests


# 创建要封装的部门类
class DepartmentApi:

    def __init__(self):
        # 定义部门模块的URL
        self.emp_url = "http://ihrm-test.itheima.net/api/company/department"

    def add_emp(self, name, code, manager, introduce, headers):  # 添加部门
        # 根据外部传入的数据拼接成要发送的请求体数据
        jsonData = {
            "name": name,
            "code": code,
            "manager": manager,
            "introduce": introduce,
            "pid": "001"
        }
        # 发送添加部门请求，并返回结果
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):  # 查询部门
        # 拼接查询部门的URL，查询的部门所属id由外界传入
        query_url = self.emp_url + "/" + emp_id
        # 发送查询部门的接口请求，并return返回结果
        return requests.get(url=query_url, headers=headers)

    def modify_emp(self, emp_id, name, code, manager, introduce, headers):  # 修改部门
        # 拼接修改部门的URL
        modify_url = self.emp_url + "/" + emp_id
        jsonData = {
            "name": name,
            "code": code,
            "manager": manager,
            "introduce": introduce,
            "pid": "001"
        }
        # 发送修改部门的接口请求，并 return返回结果
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):  # 删除部门
        # 拼接删除部门的URL
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除部门的接口请求，return返回数据
        return requests.delete(url=delete_url, headers=headers)
