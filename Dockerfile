# 基础镜像选择适合您的项目的Python版本
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY pyproject.toml poetry.lock /app/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装依赖项
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# 复制项目文件到工作目录
COPY . /app/

# 设置环境变量（如果需要）
# ENV EXAMPLE_ENV=example_value

# 启动应用程序
CMD ["python", "run.py"]
