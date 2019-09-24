import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


JENKINS_USER = 'jenkins'
JENKINS_GROUP = 'jenkins'
JENKINS_DEBIAN_REPO = '/etc/apt/sources.list.d/jenkins.list'
JENKINS_EL_REPO = '/etc/yum.repos.d/jenkins.repo'
JENKINS_DEBIAN_STABLE = 'debian-stable'
JENKINS_EL_STABLE = 'redhat'
JENKINS_BINARY_PATH = '/usr/lib/jenkins'
JENKINS_PACKAGE = 'jenkins'
JENKINS_HOME = '/var/lib/jenkins'
JENKINS_HTTP_PORT = 'HTTP_PORT=8080'
JENKINS_HEAPSIZE_MAX = 'JAVA_ARGS="-Xmx256m"'
JENKINS_SERVICE = 'jenkins'
JENKINS_URL = 'http://localhost:8080'
JENKINS_PASSWORD_FILE = '/var/lib/jenkins/secrets/initialAdminPassword'


def test_jenkinslts_user_exists(host):
    host.user('JENKINS_USER')


def test_jenkinslts_group_exists(host):
    host.group('JENKINS_GROUP')


def test_jenkinslts_home_exists(host):
    host.file('JENKINS_HOME').exists


def test_jenkinslts_home_isdirectory(host):
    host.file('JENKINS_HOME').is_directory


def test_jenkinslts_home_ownedbyuser(host):
    host.file('/var/lib/jenkins').user == JENKINS_USER


def test_jenkinslts_home_ownedbygroup(host):
    host.file('/var/lib/jenkins').group == JENKINS_GROUP


def test_jenkinslts_repofile_exists(host):
    host.file('JENKINS_DEBIAN_REPO').exists or \
      host.file('JENKINS_EL_REPO').exists


def test_jenkinslts_repofile_isfile(host):
    host.file('JENKINS_DEBIAN_REPO').is_file or \
      host.file('JENKINS_EL_REPO').is_file


def test_jenkinslts_repofile_stableurl(host):
    host.file('/etc/apt/sources.list.d/jenkins.list').contains == \
      JENKINS_DEBIAN_STABLE or \
      host.file('/etc/yum.repos.d/jenkins.repo').contains == JENKINS_EL_STABLE


def test_jenkinslts_package_installed(host):
    host.package("JENKINS_PACKAGE").is_installed


def test_jenkinslts_binary_exists(host):
    host.file('JENKINS_BINARY_PATH').exists


def test_jenkinslts_binary_directory(host):
    host.file('JENKINS_BINARY_PATH').is_directory


def test_jenkinslts_binary_whereis(host):
    host.check_output('whereis jenkins') == JENKINS_BINARY_PATH


def test_jenkinslts_http_port(host):
    host.file('/etc/default/jenkins').contains == JENKINS_HTTP_PORT or \
      host.file('/etc/sysconfig/jenkins').contains == JENKINS_HTTP_PORT


def test_jenkinslts_heapsize_max(host):
    host.file('/etc/default/jenkins').contains == JENKINS_HEAPSIZE_MAX or \
      host.file('/etc/sysconfig/jenkins').contains == JENKINS_HEAPSIZE_MAX


def test_jenkinslts_service_is_running(host):
    host.service('JENKINS_SERVICE').is_running


def test_jenkinslts_service_is_enabled(host):
    host.service('JENKINS_SERVICE').is_enabled


def test_jenkinslts_process_is_running(host):
    host.process.get(user="jenkins", comm="java")


def test_jenkinslts_url_is_reachable(host):
    host.addr('JENKINS_URL').is_reachable


def test_jenkinslts_passwordfile_exists(host):
    host.file('JENKINS_PASSWORD_FILE').exists


def test_jenkinslts_passwordfile_isfile(host):
    host.file('JENKINS_PASSWORD_FILE').is_file


def test_jenkinslts_passwordfile_ownedbyuser(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').user \
      == JENKINS_USER


def test_jenkinslts_passwordfile_ownedbygroup(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').group \
      == JENKINS_GROUP
