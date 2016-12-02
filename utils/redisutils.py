import reids

__all__ = (SetRedis)


class SetRedis(object):
    def __init__(self, name, **cfg):
        self.r = redis.Redis(**cfg)
        self.name = name

    def update(self, *values):
        self.r.sadd(self.name, *values)

    def rand_member(self, count=1):
        return self.r.srandmember(self.name, count)
