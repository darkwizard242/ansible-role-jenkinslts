import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'jenkins'
PACKAGE_USER = 'jenkins'
PACKAGE_GROUP = 'jenkins'
PACKAGE_HOME = '/var/lib/jenkins'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/jenkins.list'
EL_REPO_FILE = '/etc/yum.repos.d/jenkins.repo'
DEBIAN_WAR_FILE = '/usr/share/jenkins/jenkins.war'
EL_WAR_FILE = '/usr/lib/jenkins/jenkins.war'
DEBIAN_BINARY_DIR = '/usr/share/jenkins'
EL_BINARY_DIR = '/usr/lib/jenkins'
DEBIAN_WHEREIS = 'jenkins: /usr/share/jenkins'
EL_WHEREIS = 'jenkins: /usr/lib/jenkins'
PACKAGE_SERVICE = 'jenkins'
PACKAGE_ADMIN_PASS_FILE = '/var/lib/jenkins/secrets/initialAdminPassword'


def test_jenkinslts_user_exists(host):
    """
    Tests if jenkins user exists.
    """
    assert host.user(PACKAGE_USER)


def test_jenkinslts_group_exists(host):
    """
    Tests if jenkins group exists.
    """
    assert host.group(PACKAGE_GROUP)


def test_jenkinslts_home_exists(host):
    """
    Tests if jenkins home directory exists.
    """
    assert host.file(PACKAGE_HOME).exists


def test_jenkinslts_home_isdirectory(host):
    """
    Tests if jenkins home directory is directory type.
    """
    assert host.file(PACKAGE_HOME).is_directory


def test_jenkinslts_home_ownedbyuser(host):
    """
    Tests if jenkins home directory is owned by jenkins user.
    """
    assert host.file(PACKAGE_HOME).user == PACKAGE_USER


def test_jenkinslts_home_ownedbygroup(host):
    """
    Tests if jenkins home directory is owned by jenkins group.
    """
    assert host.file(PACKAGE_HOME).group == PACKAGE_GROUP


def test_jenkinslts_repofile_exists(host):
    """
    Tests if jenkins repo files for DEBIAN/EL systems exist.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
      host.file(EL_REPO_FILE).exists


def test_jenkinslts_repofile_isfile(host):
    """
    Tests if jenkins repo files for DEBIAN/EL systems is file type.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
      host.file(EL_REPO_FILE).is_file


def test_jenkinslts_package_installed(host):
    """
    Tests if jenkins is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_jenkinslts_binary_exists(host):
    """
    Tests if jenkins binary file exists.
    """
    assert host.file(DEBIAN_WAR_FILE).exists or \
      host.file(EL_WAR_FILE).exists


def test_jenkinslts_binary_directory_exists(host):
    """
    Tests if jenkins binary directory exists.
    """
    assert host.file(DEBIAN_BINARY_DIR).exists or \
      host.file(EL_BINARY_DIR).exists


def test_jenkinslts_binary_directory_check(host):
    """
    Tests if jenkins binary directory is directory type.
    """
    assert host.file(DEBIAN_BINARY_DIR).is_directory or \
      host.file(EL_BINARY_DIR).is_directory


def test_jenkinslts_binary_whereis(host):
    """
    Tests the output to confirm jenkins's binary location.
    """
    assert host.check_output('whereis jenkins') == DEBIAN_WHEREIS or \
        host.check_output('whereis jenkins') == EL_WHEREIS


def test_jenkinslts_service_is_running(host):
    """
    Tests if jenkins service is in running state.
    """
    assert host.service(PACKAGE_SERVICE).is_running


def test_jenkinslts_service_is_enabled(host):
    """
    Tests if jenkins service is in enabled state.
    """
    assert host.service(PACKAGE_SERVICE).is_enabled


def test_jenkinslts_process_is_running(host):
    """
    Tests if jenkins process is running.
    """
    assert host.process.get(user="jenkins", comm="java")


def test_jenkinslts_passwordfile_exists(host):
    """
    Tests if jenkins initial admin password file exists.
    """
    assert host.file(PACKAGE_ADMIN_PASS_FILE).exists


def test_jenkinslts_passwordfile_isfile(host):
    """
    Tests if jenkins initial admin password is file type.
    """
    assert host.file(PACKAGE_ADMIN_PASS_FILE).is_file


def test_jenkinslts_passwordfile_ownedbyuser(host):
    """
    Tests if jenkins initial admin password file is owned by jennkins user.
    """
    assert host.file(PACKAGE_ADMIN_PASS_FILE).user == PACKAGE_USER


def test_jenkinslts_passwordfile_ownedbygroup(host):
    """
    Tests if jenkins initial admin password file is owned by jennkins group.
    """
    assert host.file(PACKAGE_ADMIN_PASS_FILE).group == PACKAGE_GROUP
