from oslo_config import cfg

from hpedockerplugin import configuration


hpe3par_opts = [
    cfg.StrOpt('hpe3par_api_url',
               default='',
               help="3PAR WSAPI Server Url like "
                    "https://<3par ip>:8080/api/v1",
               deprecated_name='hp3par_api_url'),
    cfg.StrOpt('hpe3par_username',
               default='',
               help="3PAR username with the 'edit' role",
               deprecated_name='hp3par_username'),
    cfg.StrOpt('hpe3par_password',
               default='',
               help="3PAR password for the user specified in hpe3par_username",
               secret=True,
               deprecated_name='hp3par_password'),
    cfg.ListOpt('hpe3par_cpg',
                default=["OpenStack"],
                help="List of the CPG(s) to use for volume creation",
                deprecated_name='hp3par_cpg'),
    cfg.ListOpt('hpe3par_snapcpg',
                default=[],
                help="List of the CPG(s) to use for snapshot creation",
                deprecated_name='hp3par_snapcpg'),
    cfg.BoolOpt('hpe3par_debug',
                default=False,
                help="Enable HTTP debugging to 3PAR",
                deprecated_name='hp3par_debug'),
    cfg.ListOpt('hpe3par_iscsi_ips',
                default=[],
                help="List of target iSCSI addresses to use.",
                deprecated_name='hp3par_iscsi_ips'),
    cfg.BoolOpt('hpe3par_iscsi_chap_enabled',
                default=False,
                help="Enable CHAP authentication for iSCSI connections.",
                deprecated_name='hp3par_iscsi_chap_enabled'),
    cfg.BoolOpt('strict_ssh_host_key_policy',
                default=False,
                help='Option to enable strict host key checking.  When '
                     'set to "True" the plugin will only connect to systems '
                     'with a host key present in the configured '
                     '"ssh_hosts_key_file".  When set to "False" the host key '
                     'will be saved upon first connection and used for '
                     'subsequent connections.  Default=False'),
    cfg.StrOpt('ssh_hosts_key_file',
               default='$state_path/ssh_known_hosts',
               help='File containing SSH host keys for the systems with which '
                    'the plugin needs to communicate.  OPTIONAL: '
                    'Default=$state_path/ssh_known_hosts'),
    cfg.BoolOpt('suppress_requests_ssl_warnings',
                default=False,
                help='Suppress requests library SSL certificate warnings.'),
    # cfg.MultiOpt('replication_device',
    cfg.StrOpt('quorum_witness_ip',
               default='',
               help='IP address of Qurorum Witness'),
    cfg.StrOpt('backend_id',
               default='',
               help='Primary backend id'),
    cfg.DictOpt('replication_device',
                default={},
                help="Multi opt of dictionaries to represent a replication "
                     "target device.  This option may be specified multiple "
                     "times in a single config section to specify multiple "
                     "replication target devices.  Each entry takes the "
                     "standard dict config form: replication_device = "
                     "target_device_id:<required>,"
                     "key1:value1,key2:value2..."),
]

san_opts = [
    cfg.StrOpt('san_ip',
               default='',
               help='IP address of SAN controller'),
    cfg.StrOpt('san_login',
               default='admin',
               help='Username for SAN controller'),
    cfg.StrOpt('san_password',
               default='',
               help='Password for SAN controller',
               secret=True),
    cfg.StrOpt('san_private_key',
               default='',
               help='Filename of private key to use for SSH authentication'),
    cfg.PortOpt('san_ssh_port',
                default=22,
                help='SSH port to use with SAN'),
    cfg.IntOpt('ssh_conn_timeout',
               default=30,
               help="SSH connection timeout in seconds"),
    cfg.IntOpt('timeout',
               default=10000,
               help=''),
]

volume_opts = [
    cfg.StrOpt('iscsi_ip_address',
               default='my_ip',
               help='The IP address that the iSCSI daemon is listening on'),
    cfg.PortOpt('iscsi_port',
                default=3260,
                help='The port that the iSCSI daemon is listening on'),
    cfg.BoolOpt('use_chap_auth',
                default=False,
                help='Option to enable/disable CHAP authentication for '
                     'targets.'),
    cfg.StrOpt('chap_username',
               default='',
               help='CHAP user name.'),
    cfg.StrOpt('chap_password',
               default='',
               help='Password for specified CHAP account name.',
               secret=True),
]

CONF = cfg.CONF
CONF.register_opts(hpe3par_opts)
CONF.register_opts(san_opts, group=configuration.SHARED_CONF_GROUP)
CONF.register_opts(volume_opts, group=configuration.SHARED_CONF_GROUP)