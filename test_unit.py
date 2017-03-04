import unittest
import json
from ec2_costing.dictfunc  import func


class APITestCase(unittest.TestCase):

    def test_entry(self):
        expected = {'us-east-1': {'m3.2xlarge': '0.900', 'm3.xlarge': '0.450'},
                    'ap-southeast-1': {'m3.2xlarge': '1.260', 'm3.xlarge': '0.630', 'm1.small': '0.080'}}
        regions = [
            {
                "instanceTypes": [
                    {
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.450"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.900"
                                        }
                                    }
                                ]
                            }
                        ],
                        "type": "generalCurrentGen"
                    }
                ],
                "region": "us-east-1"
            },
            {
                "instanceTypes": [
                    {
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.080"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                           "USD": "0.630"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.260"
                                        }
                                    }
                                ]
                            }
                        ],
                        "type": "generalPreviousGen"
                    }
                ],
                "region": "ap-southeast-1"
            }
        ]
        result = func(regions)
        self.assertTrue(result == expected)


if __name__ == '__main__':
    unittest.main()

