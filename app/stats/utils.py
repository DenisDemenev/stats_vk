import os

import vk

token = 'vk1.a.jombWmalPETF6clfQV9IKOdtRtdcWjxakRyXKVl9Q2rFxqq4zv-vlQn9w_EZKrp0httZLTjZlLdW_mBYirbxRxZc0iDhEu98zjYclDpLT736iwGA176UwCjD2z7nK1eTdALOIRVvVutfXj7IN0Qs3hI3wo3Ek2JjdGq7fFGd5L5bA6_XqLxB97ZHoIay-8ue_-csQZqPOBUFV8QPbqTbHQ'


def release_date(id):
    api = vk.API(access_token=token, v='5.131')
    post = api.wall.getById(posts=id)
    if (len(post) > 0):
        return post[0]
    return None
