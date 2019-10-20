import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jenkinslts_user_exists(host):
    host.user('jenkins')


def test_jenkinslts_group_exists(host):
    host.group('JENKINS_GROUP')


def test_jenkinslts_home_exists(host):
    host.file('/var/lib/jenkins').exists


def test_jenkinslts_home_isdirectory(host):
    host.file('/var/lib/jenkins').is_directory


def test_jenkinslts_home_ownedbyuser(host):
    host.file('/var/lib/jenkins').user == 'jenkins'


def test_jenkinslts_home_ownedbygroup(host):
    host.file('/var/lib/jenkins').group == 'jenkins'


def test_jenkinslts_repofile_exists(host):
    host.file('/etc/apt/sources.list.d/jenkins.list').exists or \
      host.file('/etc/yum.repos.d/jenkins.repo').exists


def test_jenkinslts_repofile_isfile(host):
    host.file('/etc/apt/sources.list.d/jenkins.list').is_file or \
      host.file('/etc/yum.repos.d/jenkins.repo').is_file


def test_jenkinslts_repofile_stableurl(host):
    host.file('/etc/apt/sources.list.d/jenkins.list').contains == \
      'debian-stable' or \
      host.file('/etc/yum.repos.d/jenkins.repo').contains == 'redhat'


def test_java_package_installed(host):
    host.package("openjdk-8-jdk").is_installed or \
      host.package("java-1.8.0-openjdk-devel").is_installed


def test_java_binary_exists(host):
    host.file('/usr/bin/java').exists


def test_java_binary_symlink(host):
    host.file('/usr/bin/java').is_symlink


def test_jenkinslts_package_installed(host):
    host.package("jenkins").is_installed


def test_jenkinslts_binary_exists(host):
    host.file('/usr/lib/jenkins').exists


def test_jenkinslts_binary_directory(host):
    host.file('/usr/lib/jenkins').is_directory


def test_jenkinslts_binary_whereis(host):
    host.check_output('whereis jenkins') == '/usr/lib/jenkins'


def test_jenkinslts_http_port(host):
    host.file('/etc/default/jenkins').contains == 'HTTP_PORT=8080' or \
      host.file('/etc/sysconfig/jenkins').contains == 'JENKINS_PORT="8080"''


def test_jenkinslts_heapsize_max(host):
    host.file('/etc/default/jenkins').contains == 'JAVA_ARGS="-Xmx256m"' or \
      host.file('/etc/sysconfig/jenkins').contains == 'JAVA_ARGS="-Xmx256m"'


def test_jenkinslts_service_is_running(host):
    host.service('jenkins').is_running


def test_jenkinslts_service_is_enabled(host):
    host.service('jenkins').is_enabled


def test_jenkinslts_process_is_running(host):
    host.process.get(user="jenkins", comm="java")


def test_jenkinslts_url_is_reachable(host):
    host.addr('http://localhost:8080').is_reachable


def test_jenkinslts_passwordfile_exists(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').exists


def test_jenkinslts_passwordfile_isfile(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').is_file


def test_jenkinslts_passwordfile_ownedbyuser(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').user \
      == 'jenkins'


def test_jenkinslts_passwordfile_ownedbygroup(host):
    host.file('/var/lib/jenkins/secrets/initialAdminPassword').group \
      == 'jenkins'
