[![build-test](https://github.com/darkwizard242/ansible-role-jenkinslts/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-jenkinslts/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-jenkinslts/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-jenkinslts/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43603?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43603?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43603?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jenkinslts&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-jenkinslts) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jenkinslts&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jenkinslts) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jenkinslts&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jenkinslts) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jenkinslts&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jenkinslts) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-jenkinslts?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-jenkinslts?color=orange&style=flat-square)

# Ansible Role: jenkinslts

Role to install (_by default_) LTS version of [Jenkins](https://jenkins.io/download/lts/) for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

Java is required for Jenkins.

You can install Java using [darkwizard242.adoptopenjdk](https://galaxy.ansible.com/darkwizard242/adoptopenjdk) role.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
jenkinslts_user: jenkins
jenkinslts_group: jenkins
jenkinslts_group_desired_state: present
jenkinslts_user_home: "/var/lib/{{ jenkinslts_user }}"
jenkinslts_user_shell: /bin/false
jenkinslts_user_desired_state: present
jenkinslts_app_name: jenkins
jenkinslts_debian_gpg_key: https://pkg.jenkins.io/debian-stable/jenkins.io.key
jenkinslts_el_gpg_key: https://pkg.jenkins.io/redhat-stable/jenkins.io.key
jenkinslts_repo_debian: deb https://pkg.jenkins.io/debian-stable binary/
jenkinslts_repo_debian_filename: "{{ jenkinslts_app_name }}"
jenkinslts_repo_el_name: jenkins
jenkinslts_repo_el_description: Jenkins
jenkinslts_repo_el: http://pkg.jenkins.io/redhat-stable
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
jenkinslts_app_check_status_code: 200
jenkinslts_app_check_status_code_retries: 10
jenkinslts_app_check_status_code_delay: 5
jenkinslts_app_admin_password_file: "{{ jenkinslts_user_home }}/secrets/initialAdminPassword"
```

### Variables table:

Variable                                 | Description
---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jenkinslts_group                         | Name of the group that the jenkins owner will belong to. Jenkins Group argument is only required on Debian based systems, not on EL based systems.
jenkinslts_group_desired_state           | `present` indicates creating the group if it doesn't exist. Alternative is `absent`.
jenkinslts_user                          | Name of the user that the jenkins will be owned by.
jenkinslts_user_home                     | Home directory for jenkins user specified above as `jenkinslts_user`. Since Jenkins by default is installed in `/var/lib/jenkins`. It is recommended to use that directory as such.
jenkinslts_user_shell                    | Shell for `jenkinslts_user`. Typically, shell usage is not required. Hence set to `/bin/false`.
jenkinslts_user_desired_state            | `present` indicates creating the user if it doesn't exist. Atlernative is `absent`.
jenkinslts_debian_gpg_key                | Jenkins GPG required on Debian based systems.
jenkinslts_el_gpg_key                    | Jenkins GPG required on EL based systems.
jenkinslts_repo_debian                   | Repository marking to add for Debian based systems.
jenkinslts_repo_debian_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ jenkinslts_app_name }}" which is `jenkins` .
jenkinslts_repo_el_name                  | Repository name for Jenkins on EL based systems.
jenkinslts_repo_el_description           | Description to be added in EL based repository file for Jenkins.
jenkinslts_repo_el                       | Repository `baseurl` for Jenkins on EL based systems.
jenkinslts_repo_el_gpgcheck              | Boolean for whether to perform gpg check against Jenkins on EL based systems.
jenkinslts_repo_desired_state            | `present` indicates creating the repository file if it doesn't exist on Debian or EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **jenkins** pacakge).
jenkinslts_app_name                      | Name of Jenkins LTS (Long Term Support) application i.e. `jenkins`
jenkinslts_desired_state                 | State of the jenkinslts_app_name package (i.e. `jenkins` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
jenkinslts_default_debain_config_file    | Jenkins default configuration file on Debian based systems.
jenkinslts_default_el_config_file        | Jenkins default configuration file on EL based systems.
jenkinslts_app_port                      | Port to assign Jenkins to serve on.
jenkinslts_app_heapsize_max              | Maximum JVM heapsize to allocate to Jenkins.
jenkinslts_service_name                  | Default service name for Jenkins.
jenkinslts_service_desired_state         | Desired state for Jenkins service.
jenkinslts_service_desired_boot_enabled  | Desired enabled/disabled state for Jenkins service.
jenkinslts_app_check_status_code         | Desired status code to return in a handler that checks for Jenkins URL post installation and restart. It is set to 200 as /login path returns HTTP code 200.
jenkinslts_app_check_status_code_retries | URL curl retries set to 10 (as Jenkins may take some time to boot up.)
jenkinslts_app_check_status_code_delay   | Retries for URL curl set to 5.
jenkinslts_app_admin_password_file       | File that contains default admin password for Jenkins UI.

## Dependencies

Java is required for Jenkins.

You can install Java using [darkwizard242.adoptopenjdk](https://galaxy.ansible.com/darkwizard242/adoptopenjdk) role.

## Example Playbook

For default behaviour of role (i.e. installation of **jenkins** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.jenkinslts
```

For customizing behavior of role (i.e. installation of `darkwizard242.adoptopenjdk` role alongside **darkwizard242.jenkins** ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizar242.adoptopenjdk
    - darkwizard242.jenkinslts
  vars:
    adoptopenjdk_app_name: adoptopenjdk-11-hotspot
    adoptopenjdk_desired_state: present
    jenkinslts_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **jenkins** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.jenkinslts
  vars:
    jenkinslts_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-jenkinslts/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
