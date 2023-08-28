from tortoise import Model, Tortoise


# 创建一个空模型
class EmptyModel(Model):
    pass


class YtestManager(EmptyModel):
    
    @classmethod
    async def get_id(cls):
        conn = await Tortoise.get_connection("master")
        data = await conn.execute_query("select * from ytest")
        return data