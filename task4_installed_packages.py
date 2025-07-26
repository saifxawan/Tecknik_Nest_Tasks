# Task 4: List all installed pip packages
import pkg_resources

installed_packages = pkg_resources.working_set
for dist in installed_packages:
    print(dist.project_name, dist.version)
