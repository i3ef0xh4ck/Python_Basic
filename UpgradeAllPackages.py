# coding=utf-8
def upgradeall():
    import pip
    from subprocess import call
    for dist in pip.get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)
    return 0


upgradeall()
