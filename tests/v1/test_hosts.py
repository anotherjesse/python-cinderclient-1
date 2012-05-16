from cinderclient.v1 import hosts
from tests.v1 import fakes
from tests import utils


cs = fakes.FakeClient()


class HostsTest(utils.TestCase):

    def test_describe_resource(self):
        hs = cs.hosts.get('host')
        cs.assert_called('GET', '/os-hosts/host')
        [self.assertTrue(isinstance(h, hosts.Host)) for h in hs]

    def test_update_enable(self):
        host = cs.hosts.get('sample_host')[0]
        values = {"status": "enabled"}
        result = host.update(values)
        cs.assert_called('PUT', '/os-hosts/sample_host', values)
        self.assertTrue(isinstance(result, hosts.Host))

    def test_update_maintenance(self):
        host = cs.hosts.get('sample_host')[0]
        values = {"maintenance_mode": "enable"}
        result = host.update(values)
        cs.assert_called('PUT', '/os-hosts/sample_host', values)
        self.assertTrue(isinstance(result, hosts.Host))

    def test_update_both(self):
        host = cs.hosts.get('sample_host')[0]
        values = {"status": "enabled",
                  "maintenance_mode": "enable"}
        result = host.update(values)
        cs.assert_called('PUT', '/os-hosts/sample_host', values)
        self.assertTrue(isinstance(result, hosts.Host))

    def test_host_startup(self):
        host = cs.hosts.get('sample_host')[0]
        result = host.startup()
        cs.assert_called('GET', '/os-hosts/sample_host/startup')
        self.assertTrue(isinstance(result, hosts.Host))

    def test_host_reboot(self):
        host = cs.hosts.get('sample_host')[0]
        result = host.reboot()
        cs.assert_called('GET', '/os-hosts/sample_host/reboot')
        self.assertTrue(isinstance(result, hosts.Host))

    def test_host_shutdown(self):
        host = cs.hosts.get('sample_host')[0]
        result = host.shutdown()
        cs.assert_called('GET', '/os-hosts/sample_host/shutdown')
        self.assertTrue(isinstance(result, hosts.Host))
