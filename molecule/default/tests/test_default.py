import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jenkinslts_user_exists(host):
    assert host.user('jenkins')


def test_jenkinslts_group_exists(host):
    assert host.group('JENKINS_GROUP')


def test_jenkinslts_home_exists(host):
    assert host.file('/var/lib/jenkins').exists


def test_jenkinslts_home_isdirectory(host):
    assert host.file('/var/lib/jenkins').is_directory


def test_jenkinslts_home_ownedbyuser(host):
    assert host.file('/var/lib/jenkins').user == 'jenkins'


def test_jenkinslts_home_ownedbygroup(host):
    assert host.file('/var/lib/jenkins').group == 'jenkins'


def test_jenkinslts_repofile_exists(host):
    assert host.file('/etc/apt/sources.list.d/jenkins.list').exists or \
      host.file('/etc/yum.repos.d/jenkins.repo').exists


def test_jenkinslts_repofile_isfile(host):
    assert host.file('/etc/apt/sources.list.d/jenkins.list').is_file or \
      host.file('/etc/yum.repos.d/jenkins.repo').is_file


def test_jenkinslts_repofile_stableurl(host):
    assert host.file('/etc/apt/sources.list.d/jenkins.list').contains == \
      'debian-stable' or \
      host.file('/etc/yum.repos.d/jenkins.repo').contains == 'redhat'


def test_java_package_installed(host):
    assert host.package("openjdk-8-jdk").is_installed or \
      host.package("java-1.8.0-openjdk-devel").is_installed


def test_java_binary_exists(host):
    host.file('/usr/bin/java').exists


def test_java_binary_symlink(host):
    assert host.file('/usr/bin/java').is_symlink


def test_jenkinslts_package_installed(host):
    assert host.package("jenkins").is_installed


def test_jenkinslts_binary_exists(host):
    assert host.file('/usr/lib/jenkins').exists


def test_jenkinslts_binary_directory(host):
    assert host.file('/usr/lib/jenkins').is_directory


def test_jenkinslts_binary_whereis(host):
    assert host.check_output('whereis jenkins') == '/usr/lib/jenkins'


def test_jenkinslts_http_port(host):
    assert host.file('/etc/default/jenkins').contains == 'HTTP_PORT=8080' or \
      host.file('/etc/sysconfig/jenkins').contains == 'JENKINS_PORT="8080"'


def test_jenkinslts_heapsize_max(host):
    assert host.file('/etc/default/jenkins').contains == 'JAVA_ARGS="-Xmx256m"' or \
      host.file('/etc/sysconfig/jenkins').contains == 'JAVA_ARGS="-Xmx256m"'


def test_jenkinslts_service_is_running(host):
    assert host.service('jenkins').is_running


def test_jenkinslts_service_is_enabled(host):
    assert host.service('jenkins').is_enabled


def test_jenkinslts_process_is_running(host):
    assert host.process.get(user="jenkins", comm="java")


def test_jenkinslts_url_is_reachable(host):
    assert host.addr('http://localhost:8080').is_reachable


def test_jenkinslts_passwordfile_exists(host):
    assert host.file('/var/lib/jenkins/secrets/initialAdminPassword').exists


def test_jenkinslts_passwordfile_isfile(host):
    assert host.file('/var/lib/jenkins/secrets/initialAdminPassword').is_file


def test_jenkinslts_passwordfile_ownedbyuser(host):
    assert host.file('/var/lib/jenkins/secrets/initialAdminPassword').user \
      == 'jenkins'


def test_jenkinslts_passwordfile_ownedbygroup(host):
    assert host.file('/var/lib/jenkins/secrets/initialAdminPassword').group \
      == 'jenkins'
