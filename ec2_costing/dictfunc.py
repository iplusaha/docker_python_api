def func(data):
    """
   This function strip off the price on EC2 instance for each region and return the value into a Dictionary
    """
    last = dict()
    for item in data:
        d = dict()
        for instanceType in item['instanceTypes']:
            sizes = instanceType['sizes']
            for size in sizes:
                instance_type = size['size']
                price = size['valueColumns'][0]['prices']['USD']
                d.update({instance_type: price})
        last.update({item['region']: d})
    return last
