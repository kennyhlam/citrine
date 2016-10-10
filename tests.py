# -*- coding: utf-8 -*-

import os
import citrine_server
import unittest
import json

def assert_mult_units(resp, mult_fact, si_units):
    assert resp['multiplication_factor'] == mult_fact
    assert resp['unit_name'] == si_units

class CitrineTestCase(unittest.TestCase):

    def setUp(self):
        citrine_server.app.config['TESTING'] = True
        self.app = citrine_server.app.test_client()
        
    def tearDown(self):
        pass

    def test_bad_request(self):
        rv = self.app.get('/units/')
        assert rv.status_code == 404
        rv = self.app.get('/units/si')
        assert rv.status_code == 400
        
        try:
            rv = self.app.get('/units/si?units=degreess')
            raise Exception('Query should have failed.')
        except KeyError:
            pass

    def get_resp(self, q):
        r = self.app.get(u"/units/si?units={}".format(q))
        return json.loads(r.get_data())

    def test_valid_requests(self):
        rv = self.app.get('/units/si?units=degree')
        assert rv.mimetype == 'application/json'
        resp = json.loads(rv.get_data())
        assert type(resp) == dict
        assert resp['multiplication_factor'] == 0.01745329251994
        assert resp['unit_name'] == 'rad'

        resp = self.get_resp('degree/minute')
        assert_mult_units(resp, .00029088820867, 'rad/s')

        resp = self.get_resp('degree*minute')
        assert_mult_units(resp, 1.04719755119660, 'rad*s')

        resp = self.get_resp('(degree*minute/minute)')
        assert_mult_units(resp, 0.01745329251994, '(rad*s/s)')

        resp = self.get_resp('degree/minute*hour')
        assert_mult_units(resp, 1.04719755119660, 'rad/s*s')

        resp = self.get_resp('"/ha*(L/minute*(tonne*d))')
        assert_mult_units(resp, 0.00000069813170, 'rad/m2*(m3/s*(kg*s))')

        resp = self.get_resp("(second/hectare)*(litre/min*t*day)")
        assert_mult_units(resp, 0.00000069813170, '(rad/m2)*(m3/s*kg*s)')

        resp = self.get_resp(u"'/°*(h)")
        assert_mult_units(resp, 3600.000000000000, 'rad/rad*(s)')

        resp = self.get_resp(u"'*°*(h)")
        assert_mult_units(resp, 1.09662271123215, 'rad*rad*(s)')

if __name__ == '__main__':
    unittest.main()
