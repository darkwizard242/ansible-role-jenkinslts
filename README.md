[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-jenkinslts.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-jenkinslts) ![Ansible Role](https://img.shields.io/ansible/role/43603?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43603?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43603?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jenkinslts&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-jenkinslts) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-jenkinslts?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-jenkinslts?color=orange&style=flat-square)

# Ansible Role: jenkinslts

Role to install (_by default_) `jenkins` package (LTS Version) for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
jenkinslts_user: jenkins
jenkinslts_group: jenkins
jenkinslts_javadependency_debian: openjdk-8-jdk
jenkinslts_javadependency_el: java-1.8.0-openjdk-devel
jenkinslts_javadependency_debian_desired_state: present
jenkinslts_javadependency_el_desired_state: present
jenkinslts_group_desired_state: present
jenkinslts_user_home: "/var/lib/{{ jenkinslts_user }}"
jenkinslts_user_shell: /bin/false
jenkinslts_user_desired_state: present
jenkinslts_app_name: jenkins
jenkinslts_debian_gpg_key: https://pkg.jenkins.io/debian/jenkins.io.key
jenkinslts_el_gpg_key: https://jenkins-ci.org/redhat/jenkins-ci.org.key
jenkinslts_repo_debian: deb https://pkg.jenkins.io/debian-stable binary/
jenkinslts_repo_debian_filename: "{{ jenkinslts_app_name }}"
jenkinslts_repo_el_name: jenkins
jenkinslts_repo_el_description: Jenkins
jenkinslts_repo_el: http://pkg.jenkins.io/redhat
jenkinslts_repo_el_filename: "{{ jenkinslts_app_name }}"
jenkinslts_repo_el_gpgcheck: yes
jenkinslts_repo_desired_state: present
jenkinslts_desired_state: present
jenkinslts_default_debain_config_file: /etc/default/jenkins
jenkinslts_default_el_config_file: /etc/sysconfig/jenkins
jenkinslts_app_port: 8080
jenkinslts_app_heapsize_max: 256m
jenkinslts_service_name: jenkins
jenkinslts_service_desired_state: restarted
jenkinslts_service_desired_boot_enabled: yes
jenkinslts_app_check_status_code: 403
jenkinslts_app_check_status_code_retries: 10
jenkinslts_app_check_status_code_delay: 5
jenkinslts_app_admin_password_file: "{{ jenkinslts_user_home }}/secrets/initialAdminPassword"
```

### Variables table:

Variable                                       | Value (default)                                           | Description
---------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jenkinslts_group                               | jenkins                                                   | Name of the group that the jenkins owner will belong to. Jenkins Group argument is only required on Debian based systems, not on EL based systems.
jenkinslts_group_desired_state                 | present                                                   | `present` indicates creating the group if it doesn't exist. Alternative is `absent`.
jenkinslts_user                                | jenkins                                                   | Name of the user that the jenkins will be owned by.
jenkinslts_user_home                           | "/var/lib/{{ jenkinslts_user }}"                          | Home directory for jenkins user specified above as `jenkinslts_user`. Since Jenkins by default is installed in `/var/lib/jenkins`. It is recommended to use that directory as such.
jenkinslts_user_shell                          | /bin/false                                                | Shell for `jenkinslts_user`. Typically, shell usage is not required. Hence set to `/bin/false`.
jenkinslts_user_desired_state                  | present                                                   | `present` indicates creating the user if it doesn't exist. Atlernative is `absent`.
jenkinslts_javadependency_debian               | openjdk-8-jdk                                             | Java 8 package to install on Debian based systems. Jenkins LTS support OpenJDK8.
jenkinslts_javadependency_el                   | java-1.8.0-openjdk-devel                                  | Java 8 package to install on EL based systems. Jenkins LTS support OpenJDK8.
jenkinslts_javadependency_debian_desired_state | present                                                   | State of the jenkinslts_javadependency_debian package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
jenkinslts_javadependency_el_desired_state     | present                                                   | State of the jenkinslts_javadependency_el package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
jenkinslts_debian_gpg_key                      | <https://pkg.jenkins.io/debian/jenkins.io.key>            | Jenkins GPG required on Debian based systems.
jenkinslts_el_gpg_key                          | <https://jenkins-ci.org/redhat/jenkins-ci.org.key>        | Jenkins GPG required on EL based systems.
jenkinslts_repo_debian                         | deb <https://pkg.jenkins.io/debian-stable> binary/        | Repository marking to add for Debian based systems.
jenkinslts_repo_debian_filename                | "{{ jenkinslts_app_name }}"                               | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ jenkinslts_app_name }}" which is `jenkins` .
jenkinslts_repo_el_name                        | jenkins                                                   | Repository name for Jenkins on EL based systems.
jenkinslts_repo_el_description                 | Jenkins                                                   | Description to be added in EL based repository file for Jenkins.
jenkinslts_repo_el                             | <http://pkg.jenkins.io/redhat>                            | Repository `baseurl` for Jenkins on EL based systems.
jenkinslts_repo_el_gpgcheck                    | yes                                                       | Boolean for whether to perform gpg check against Jenkins on EL based systems.
jenkinslts_repo_desired_state                  | present                                                   | `present` indicates creating the repository file if it doesn't exist on Debian or EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **jenkins** pacakge).
jenkinslts_app_name                            | jenkins                                                   | Name of Jenkins LTS (Long Term Support) application i.e. `jenkins`
jenkinslts_desired_state                       | present                                                   | State of the jenkinslts_app_name package (i.e. `jenkins` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
jenkinslts_default_debain_config_file          | /etc/default/jenkins                                      | Jenkins default configuration file on Debian based systems.
jenkinslts_default_el_config_file              | /etc/sysconfig/jenkins                                    | Jenkins default configuration file on EL based systems.
jenkinslts_app_port                            | 8080                                                      | Port to assign Jenkins to serve on.
jenkinslts_app_heapsize_max                    | 256m                                                      | Maximum JVM heapsize to allocate to Jenkins.
jenkinslts_service_name                        | jenkins                                                   | Default service name for Jenkins.
jenkinslts_service_desired_state               | restarted                                                 | Desired state for Jenkins service.
jenkinslts_service_desired_boot_enabled        | yes                                                       | Desired enabled/disabled state for Jenkins service.
jenkinslts_app_check_status_code               | 403                                                       | Desired status code to return in a handler that checks for Jenkins URL post installation and restart. It is set to 403 as Jenkins initially requires user to input Admin password for initial setup.
jenkinslts_app_check_status_code_retries       | 10                                                        | URL curl retries set to 10 (as Jenkins may take some time to boot up.)
jenkinslts_app_check_status_code_delay         | 5                                                         | Retries for URL curl set to 5.
jenkinslts_app_admin_password_file             | "{{ jenkinslts_user_home }}/secrets/initialAdminPassword" | File that contains default admin password for Jenkins UI.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **jenkins** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.jenkinslts
```

For customizing behavior of role (i.e. installation of latest **jenkins** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.jenkinslts
      vars:
        jenkinslts_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **jenkins** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.jenkinslts
      vars:
        jenkinslts_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-jenkinslts/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
