服务模板

## 目录结构
    |-- examples:                   服务调用的代码示例
    |-- demo:                       代码
        |-- dao:                    数据层，访问外部数据存储
            |-- orm.py:             持久数据访问
            |-- cache.py:           缓存数据访问
            |-- queue.py:           流数据访问
            |-- rpc.py:             第三方服务请求访问
        |-- handlers:               协议层，调用models和services
        |-- routes:                 路由层，调用handlers
        |-- models:                 api参数
            |-- orm_models.py:      数据表模型
            |-- api_models.py:      api参数模型
            |-- logic_models.py:    逻辑参数模型
        |-- services:               服务层，业务逻辑，调用dao
            |-- aggregation.py:     服务聚合，作为services具体服务上层
        |-- utils:                  常用工具
    |-- run.py:                     入口
    |-- tests:                      单元测试用例
    |-- .gitlab-ci.yaml
    |-- .pre-commit-config.yaml:    代码格式规范
    |-- CHANGELOG.md                版本日志


#### 启动服务
python3 run.py

### 自动生成的交互式 API 文档（由 SwaggerUI生成）
- http://127.0.0.1:8000/docs
- 创建app时候设置docs_url=None怎不生成在线接口文档

#### 代码风格
[pre-commit](https://gitlab.deepwisdomai.com/hongjiongteng/precommit)

#### 单元测试
测试覆盖查看：coverage run -m pytest && coverage report -m && coverage html && open htmlcov/index.html

### 安装依赖
- poetry install 
